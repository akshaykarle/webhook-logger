# Webhook Receiver

A simple Flask application that receives webhook payloads, logs them to a file, and prints them to the console.

## Prerequisites

- [Nix package manager](https://nixos.org/download.html) installed on your system
- Flakes enabled in your Nix configuration

## Getting Started

### 1. Set up the development environment

This project uses Nix for reproducible development environments. To enter the development shell:

```bash
nix develop
```

This will set up all required dependencies (Flask and ngrok) as specified in `flake.nix`.

### 2. Running the Flask application

Once inside the Nix development shell, you can run the Flask application:

```bash
python app.py
```

The application will start a web server on port 8080.

### 3. Exposing your local server with ngrok

To receive webhooks from external services, you need to expose your local server to the internet. ngrok provides a secure tunnel to your localhost:

```bash
ngrok http 8080
```

ngrok will provide you with a public URL (e.g., `https://a1b2c3d4.ngrok.io`) that you can use as your webhook endpoint.

### 4. Configure your webhook provider

Use the ngrok URL as your webhook URL in the service you're receiving webhooks from. All requests to this URL will be forwarded to your local application.

## How it works

- The Flask application listens for POST requests at the root endpoint (`/`)
- When a webhook payload is received, it:
  - Logs the payload to a file named `payload_log.txt`
  - Prints the payload to the console in a pretty-printed format
  - Returns a 200 OK response

## Development

- The application code is in `app.py`
- Dependencies and development environment are managed in `flake.nix`
