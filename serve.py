"""Serve the visualisation locally: `python serve.py [port]`."""
import http.server
import socketserver
import sys
import webbrowser
from functools import partial
from pathlib import Path

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
handler = partial(http.server.SimpleHTTPRequestHandler, directory=str(Path(__file__).parent))

with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
    url = f"http://localhost:{port}"
    print(f"Open {url}  (Ctrl+C to stop)")
    webbrowser.open(url)
    httpd.serve_forever()
