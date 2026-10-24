from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import json

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length)

        try:
            payload = json.loads(data)
            alerts = payload.get("alerts", [])

            if any(
                alert.get("labels", {}).get("alertname") == "NginxDown"
                and alert.get("status") == "firing"
                for alert in alerts
            ):
                result = subprocess.run(
                    ["ansible-playbook", "ansible/restart-nginx.yml"],
                    cwd="/home/" + subprocess.check_output(
                        ["whoami"], text=True
                    ).strip() + "/self-healing-infrastructure",
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                print(result.stdout, flush=True)
                print(result.stderr, flush=True)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Webhook processed")

        except Exception as error:
            print(error, flush=True)
            self.send_response(500)
            self.end_headers()

HTTPServer(("0.0.0.0", 5001), WebhookHandler).serve_forever()
