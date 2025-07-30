FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY clado_agent.py .

EXPOSE 5001

CMD ["python", "clado_agent.py"] 