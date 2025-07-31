from python_a2a import A2AServer, skill, agent, run_server, TaskStatus, TaskState
import os
import httpx
from flask import Flask, jsonify

@agent(
    name="Clado Agent",
    description="Provides people search services",
    version="1.0.0"
)
class CladoAgent(A2AServer):
    
    def __init__(self):
        super().__init__()
        # Add a simple health check endpoint
        self.app = Flask(__name__)
        
        @self.app.route('/health')
        def health_check():
            return jsonify({
                "status": "healthy",
                "agent": "Clado Agent",
                "version": "1.0.0"
            })
    
    @skill(
        name="Get users",
        description="Get users from a huge database",
        tags=["find", "people"]
    )
    def get_users(self, query):
        """Get users from a huge database."""
        print(f"Getting users for {query}")
        return self._run(query, limit=1, school=None, company=None, acceptance_threshold=30)
        
    def _run(self, query: str, limit: int = 1, school: list[str] = None, company: list[str] = None, acceptance_threshold: int = 30) -> str:
        api_key = os.getenv("CLADO_API_KEY")
        if not api_key:
            return "Clado API key not set. Please set CLADO_API_KEY in your environment."
        
        
        url = "https://search.clado.ai/api/search"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json"
        }
        
        # Prepare query parameters according to API spec
        params = {
            "query": query,
            "limit": limit
        }
        if school:
            params["school"] = school
        if company:
            params["company"] = company
            
        print(f"Sending GET request to {url}")
        print(f"Headers: {headers}")
        print(f"Query params: {params}")
        
        try:
            with httpx.Client(timeout=30) as client:
                # Let httpx handle the URL encoding automatically
                resp = client.get(url, headers=headers, params=params)
                print(f"Actual request URL: {resp.request.url}")
                print(f"Response status: {resp.status_code}")
                print(f"Response: {resp.text}")
                
                if resp.status_code != 200:
                    return f"Clado API error: {resp.status_code} {resp.text}"
                
                data = resp.json()
                print(f"Parsed data: {data}")
                results = data.get("results", [])
                print(f"Results: {results}")
                
                if not results:
                    return "No matching profiles found."
                
                summary = []
                for r in results:
                    p = r.get("profile", {})
                    summary.append(f"- {p.get('name')} ({p.get('headline', 'N/A')}) | {p.get('location', '')} | {p.get('linkedin_url', '')}")
                return "\n".join(summary)
        except Exception as e:
            print(f"Exception occurred: {e}")
            return f"Error calling Clado API: {e}"
    
    def handle_task(self, task):
        # Extract location from message
        message_data = task.message or {}
        content = message_data.get("content", {})
        text = content.get("text", "") if isinstance(content, dict) else ""
        
               
        # Get relevant users and create response
        users = self.get_users(text)
        task.artifacts = [{
            "parts": [{"type": "text", "text": users}]
        }]
        task.status = TaskStatus(state=TaskState.COMPLETED)
        return task

# Run the server
if __name__ == "__main__":
    agent = CladoAgent()
    port = int(os.environ.get("PORT", 5001))  # Render provides the port
    print(f"Starting Clado Agent on port {port}")
    print(f"Health check available at: http://localhost:{port}/health")
    run_server(agent, host="0.0.0.0", port=port)