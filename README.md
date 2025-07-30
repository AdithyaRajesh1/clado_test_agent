# Clado Test Agent

A Python A2A agent that provides people search services using the Clado API.

## Features

- Search for people using the Clado API
- RESTful health check endpoint
- Docker containerization support
- Ready for cloud deployment

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables**:
   ```bash
   export CLADO_API_KEY=your_clado_api_key_here
   ```

3. **Run locally**:
   ```bash
   python clado_agent.py
   ```

The agent will be available at `http://localhost:5001`

## API Endpoints

- **Health Check**: `GET /health` - Returns service status
- **Agent Endpoint**: Root endpoint for A2A protocol communication

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions to various cloud platforms including Render, Railway, Heroku, and DigitalOcean.

## Environment Variables

- `CLADO_API_KEY`: Your Clado API key (required)
- `PORT`: Port to run the server on (default: 5001)

## Docker

Build and run with Docker:

```bash
docker build -t clado-agent .
docker run -p 5001:5001 -e CLADO_API_KEY=your_key clado-agent
```

## License

MIT 