#!/usr/bin/python3
"""Simple HTTP server implementation using http.server module"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Custom handler for HTTP requests"""

    def _set_headers(self, status_code=200, content_type='application/json'):
        """Set response headers"""
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _send_json_response(self, data, status_code=200):
        """Send JSON response to client"""
        self._set_headers(status_code)
        response = json.dumps(data).encode('utf-8')
        self.wfile.write(response)

    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self._set_headers(200, 'text/plain')
            self.wfile.write("Hello, this is a simple API!".encode())

        elif self.path == '/data':
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self._send_json_response(data)

        elif self.path == '/info':
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._send_json_response(info_data)

        else:
            error_data = {
                "error": "Endpoint not found",
                "status": 404
            }
            self._send_json_response(error_data, 404)


def run_server(port=8000):
    """Start the HTTP server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on port {port}...")
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
