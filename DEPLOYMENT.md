# Deploying Clado Agent to Public Endpoint

## Option 1: Deploy to Render (Recommended)

1. **Create a Render account** at https://render.com

2. **Connect your repository** to Render

3. **Create a new Web Service**:
   - Choose your repository
   - Set the following configuration:
     - **Build Command**: `docker build -t clado-agent .`
     - **Start Command**: `docker run -p $PORT:5001 clado-agent`
     - **Environment Variables**:
       - `CLADO_API_KEY`: Your Clado API key
       - `PORT`: 5001 (Render will override this)

4. **Deploy** - Render will automatically build and deploy your service

## Option 2: Deploy to Railway

1. **Create a Railway account** at https://railway.app

2. **Connect your repository**

3. **Add environment variables**:
   - `CLADO_API_KEY`: Your Clado API key

4. **Deploy** - Railway will automatically detect and deploy your Python app

## Option 3: Deploy to Heroku

1. **Create a Heroku account** and install Heroku CLI

2. **Create a new app**:
   ```bash
   heroku create your-clado-agent
   ```

3. **Set environment variables**:
   ```bash
   heroku config:set CLADO_API_KEY=your_api_key_here
   ```

4. **Deploy**:
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

## Option 4: Deploy to DigitalOcean App Platform

1. **Create a DigitalOcean account**

2. **Create a new App**:
   - Connect your repository
   - Choose Python as the runtime
   - Set environment variables for `CLADO_API_KEY`

3. **Deploy** - DigitalOcean will handle the rest

## Testing Your Deployed Endpoint

Once deployed, your agent will be available at:
- Render: `https://your-app-name.onrender.com`
- Railway: `https://your-app-name.railway.app`
- Heroku: `https://your-app-name.herokuapp.com`
- DigitalOcean: `https://your-app-name.ondigitalocean.app`

## Security Considerations

1. **API Key Security**: Never commit your `CLADO_API_KEY` to version control
2. **Rate Limiting**: Consider implementing rate limiting for production use
3. **CORS**: If needed, configure CORS headers for web applications
4. **Monitoring**: Set up logging and monitoring for production deployments

## Local Testing

To test locally before deploying:

```bash
# Set your API key
export CLADO_API_KEY=your_api_key_here

# Run the agent
python clado_agent.py
```

The agent will be available at `http://localhost:5001` 