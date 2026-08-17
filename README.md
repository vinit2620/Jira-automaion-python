# GitHub to Jira Automation (Flask + AWS EC2 + Jira REST API)

A Python-based event-driven automation bridge hosted on AWS EC2. This application listens to GitHub issue comment webhooks and automatically creates structured tickets in Atlassian Jira Cloud using the Jira REST API v3.

---

## Architecture Overview

```text
┌─────────────────┐       Issue Comment        ┌───────────────────────┐
│                 │ ─────────────────────────> │                       │
│  GitHub Repo    │  POST /webhook (JSON)      │  AWS EC2 Instance     │
│                 │                            │  (Flask Server:5000) │
└─────────────────┘                            └───────────┬───────────┘
                                                           │
                                                           │ Creates Ticket
                                                           ▼
                                               ┌───────────────────────┐
                                               │                       │
                                               │  Jira Cloud Workspace │
                                               │                       │
                                               └───────────────────────┘

Jira-automaion-python/
├── app.py              # Flask web server handling incoming GitHub webhooks
├── jira_client.py      # Jira API wrapper and payload builder (ADF format)
├── config.py           # Configuration loader for environment variables
├── requirements.txt    # Python dependencies
├── .env.example        # Template for environment variables
├── .gitignore          # Excludes virtualenv, sensitive tokens, and cache files
└── README.md           # Project documentation

This project is an event-driven automation middleware designed to integrate GitHub repository activity directly with Atlassian Jira Cloud. Built with Python and Flask, the application runs on an AWS EC2 instance and listens for real-time HTTP POST requests sent by GitHub Webhooks. When a user posts a comment on any GitHub Issue or Pull Request containing the designated command (e.g., /issue <summary>), GitHub triggers a payload containing comment details, user metadata, and contextual issue links to the Flask endpoint listening on port 5000.

Upon receiving the payload, the Flask application (app.py) parses the incoming JSON request, extracts the relevant summary text, and constructs a structured payload using the Atlassian Document Format (ADF) required by Jira REST API v3. Through a dedicated client module (jira_client.py), the app authenticates against Jira Cloud using HTTP Basic Authentication with an API token stored securely in environment variables. It then creates a new ticket in the specified Jira project board (DA), setting the ticket title to the requested summary and embedding a direct backlink to the original GitHub comment within the description for full traceability across systems.

From an infrastructure perspective, the setup is deployed on an Ubuntu EC2 instance configured with custom security group inbound rules for port 5000. Environment variables—including the Jira workspace URL, account email, API token, and project key—are managed locally via a .env file to ensure sensitive credentials remain out of source control. For production readiness, the Flask service can be daemonized using a Linux systemd service unit, ensuring automatic process management, continuous background execution, and immediate restarts in case of failure or instance reboots.
