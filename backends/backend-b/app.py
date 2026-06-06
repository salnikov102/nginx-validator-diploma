#!/usr/bin/env python3
"""mock-бэкенд B для тестирования конфигурации Nginx."""

import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

SERVICE_NAME = os.getenv("SERVICE_NAME", "backend-b")
PORT = int(os.getenv("PORT", "5002"))  # Порт 5002

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "service": SERVICE_NAME}).encode())
        else:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("X-Backend-Server", SERVICE_NAME)
            self.end_headers()
            response = {"message": f"Ответ от {SERVICE_NAME}", "path": self.path}
            self.wfile.write(json.dumps(response).encode())

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), RequestHandler)
    print(f" {SERVICE_NAME} запущен на порту {PORT}")
    server.serve_forever()