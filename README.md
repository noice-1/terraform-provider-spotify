Forked the original provider repo and modified the redirect URI in the auth app by changing all instances of localhost since Spotify API no longer allows it.
Wrote a playlist metrics exporter which Prometheus will scrape and will be displayed as Grafana dashboards.
Playlist link - https://open.spotify.com/playlist/4YbcZWhtndWoil3CmADrYi
Prometheus shows only graphs and isn't flexible:
<img width="1850" height="987" alt="prometheus1" src="https://github.com/user-attachments/assets/20a45757-bb0c-45a0-96ea-596f8325e090" />
<img width="1846" height="983" alt="prometheus2" src="https://github.com/user-attachments/assets/1d32fde2-b50a-42c3-ae93-38a8681aa477" />
Hence we use Grafana for visualizations:
<img width="1851" height="982" alt="grafana1" src="https://github.com/user-attachments/assets/8d1f8f0d-2de3-4083-9572-0b6d0fff9fe0" />
