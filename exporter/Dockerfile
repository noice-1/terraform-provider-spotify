FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt psutil requests spotipy python-dotenv

COPY exporter.py .

CMD ["python", "exporter.py"]