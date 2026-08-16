# Jira Automation Tool (Python)

A simple, standalone Python application that authenticates with Atlassian Jira Cloud REST API v3 using an API Token and creates issues programmatically.

## Features
- **HTTP Basic Authentication**: Authenticates via Atlassian User Email and API Token.
- **Environment Management**: Stores sensitive credentials in `.env` (ignored in Git).
- **REST API v3 Compatible**: Formats descriptions using Atlassian Document Format (ADF).

---

## Getting Started

### 1. Prerequisites
- Python 3.8+
- Jira Cloud account with project access

### 2. Installation
Clone the repository and install dependencies:

```bash
git clone <repository_url>
cd jira-automation
pip install -r requirements.txt
