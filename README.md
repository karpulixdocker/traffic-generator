# traffic-generator

This project creates a Docker container that sends HTTP requests every few seconds to a specified URL with a fixed-size request body. The container is deployed as a service in Kubernetes.

## Features

- Sends HTTP POST requests to the specified URL.
- Configurable interval between requests.
- Configurable request body size (default is 100 KB).
- Ability to set parameters via environment variables.
- Request timeout: 5 seconds.

## Environment Variables

You can configure the container behavior using the following environment variables:

- `REQUEST_URL` — The URL to which requests are sent. Default: `http://example.com`.
- `REQUEST_INTERVAL` — Interval between requests in seconds. Default: `5`.
- `REQUEST_PAYLOAD_SIZE` — The size of the request body in bytes. Default: `102400` (100 KB).

## How to Run

```sh
kubectl apply -f Deployment.yaml -n <namespace>
```

Or

```sh
kubectl apply -f https://raw.githubusercontent.com/karpulixdocker/traffic-generator/main/Deployment.yaml
```
