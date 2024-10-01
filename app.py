import os
import requests
import time

URL = os.getenv("REQUEST_URL", "http://127.0.0.1")
INTERVAL = int(os.getenv("REQUEST_INTERVAL", 5))
PAYLOAD_SIZE = int(os.getenv("REQUEST_PAYLOAD_SIZE", 100 * 1024))
TIMEOUT = 5
PAYLOAD = "X" * PAYLOAD_SIZE

def send_request():
    try:
        response = requests.post(URL, data=PAYLOAD, timeout=TIMEOUT)
        print(f"Sent request to {URL}, response status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send request to {URL}: {e}")

if __name__ == "__main__":
    while True:
        send_request()
        time.sleep(INTERVAL)
        