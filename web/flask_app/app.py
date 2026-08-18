from datetime import datetime, timezone
import socket

from flask import Flask, jsonify


app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        service="kali-linux-service-lab",
        framework="Flask",
        message="Flask Web service is running",
        endpoints=["/health", "/server-info"],
    )


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/server-info")
def server_info():
    return jsonify(
        hostname=socket.gethostname(),
        utc_time=datetime.now(timezone.utc).isoformat(),
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=2025, debug=False)
