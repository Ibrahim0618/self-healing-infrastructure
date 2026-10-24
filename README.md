# Self-Healing Infrastructure

## Project Overview
A self-healing infrastructure project that monitors NGINX availability and automatically recovers the service when it goes down.

## Tech Stack
- Docker & Docker Compose
- Prometheus
- Blackbox Exporter
- Alertmanager
- Ansible
- Python
- Ubuntu (WSL)

## Architecture
1. Blackbox Exporter checks NGINX HTTP availability.
2. Prometheus collects probe metrics and evaluates alert rules.
3. Alertmanager sends alerts to a Python webhook.
4. The webhook triggers an Ansible playbook.
5. Ansible restarts the stopped NGINX container.
6. NGINX becomes available again.

## Project Structure
```text
self-healing-infrastructure/
├── alertmanager/
├── ansible/
├── prometheus/
├── scripts/
└── docker-compose.yml
```

## How to Run
1. Start Docker Desktop.
2. Navigate to the project directory.
3. Start the services:

```bash
docker compose up -d
```

4. Open Prometheus: http://localhost:9090
5. Open Alertmanager: http://localhost:9093
6. Access NGINX: http://localhost:8081

## Recovery Test
Stop NGINX to simulate a failure:

```bash
docker stop self-healing-nginx
```

When the `NginxDown` alert fires, Alertmanager sends a webhook request that triggers Ansible to restart NGINX.

Verify recovery:

```bash
curl http://localhost:8081
```

## Learning Outcomes
- Monitoring service availability
- Configuring Prometheus alert rules
- Integrating Alertmanager webhooks
- Automating recovery with Ansible
- Container management using Docker Compose

## Author
Muhamed Ibrahim

GitHub: https://github.com/Ibrahim0618
