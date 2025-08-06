import os
import json
import time
import logging
import psutil
import requests
import base64
from dotenv import load_dotenv, find_dotenv
from prometheus_client import start_http_server, Counter, Gauge, Histogram

load_dotenv(find_dotenv() or "C:/Users/leoxb/OneDrive/Desktop/tf_spotify_proj/exporter/.env")

# Prometheus metrics
spotify_auth_requests = Counter("spotify_auth_requests_total", "Total Spotify Auth Requests")
cpu_usage = Gauge("app_cpu_usage", "CPU usage of the app")
playlist_track_count = Gauge("playlist_track_count", "Number of tracks in the playlist")
playlist_total_duration = Gauge("playlist_total_duration_seconds", "Total duration of playlist in seconds")

# Logging setup
logging.basicConfig(level=logging.INFO)

def load_spotify_credentials():
    client_id = os.getenv("SPOTIPY_CLIENT_ID", "").strip()
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET", "").strip()
    return client_id, client_secret

def get_token():
    client_id, client_secret = load_spotify_credentials()
    auth_bytes = f"{client_id}:{client_secret}".encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

    try:
        response.raise_for_status()
        json_result = response.json()
        access_token = json_result.get("access_token")

        if not access_token:
            raise ValueError(f"No access_token in response: {json_result}")

        logging.info("Spotify access token retrieved successfully.")
        return access_token

    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error: {e}")
        logging.error(f"Response content: {response.text}")
        raise

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise

def fetch_playlist_data(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f"https://api.spotify.com/v1/playlists/4YbcZWhtndWoil3CmADrYi"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def update_playlist_metrics():
    token = get_token()
    playlist_data = fetch_playlist_data(token)

    tracks = playlist_data.get("tracks", {}).get("items", [])
    total_duration = sum(
        item["track"]["duration_ms"] for item in tracks if item.get("track")
    )

    playlist_track_count.set(len(tracks))
    playlist_total_duration.set(total_duration / 1000)

    logging.info(f"Updated metrics: {len(tracks)} tracks, {total_duration / 1000:.2f} seconds")

if __name__ == "__main__":
    start_http_server(5000)
    logging.info("Prometheus metrics server started on port 5000.")

    while True:
        spotify_auth_requests.inc()
        cpu_usage.set(psutil.cpu_percent(interval=1))
        fetch_playlist_data(get_token())
        update_playlist_metrics()
        logging.info("Metrics updated.")
        time.sleep(10)