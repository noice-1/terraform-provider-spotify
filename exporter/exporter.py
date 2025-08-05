from prometheus_client import start_http_server, Counter
import time
import logging
logging.basicConfig(level=logging.INFO)


spotify_auth_requests = Counter("spotify_auth_requests_total", "Total Spotify Auth Requests")

if __name__ == "__main__":
    start_http_server(5000)  # Port Prometheus will scrape
    while True:
        # Dummy increment for example
        spotify_auth_requests.inc()
        logging.info("Incremented spotify_auth_requests")
        time.sleep(10)
