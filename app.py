from flask import Flask, request, jsonify
import re
import os
from jira_client import JiraClient

app = Flask(__name__)
jira_client = JiraClient()

@app.route("/webhook", methods=["POST"])
def github_webhook():
    payload = request.get_json()
    
    # Check if the event is an issue comment creation
    comment_body = payload.get("comment", {}).get("body", "")
    action = payload.get("action", "")

    if action == "created" and comment_body.startswith("/issue"):
        # Extract custom summary from comment (e.g., "/issue Fix DB connection bug")
        # Default to GitHub comment body if no custom summary provided
        summary_text = comment_body.replace("/issue", "").strip()
        if not summary_text:
            summary_text = f"Issue reported via GitHub by @{payload['comment']['user']['login']}"

        # Get original GitHub issue link for context
        github_issue_url = payload.get("issue", {}).get("html_url", "N/A")
        description_text = f"Automated ticket created from GitHub comment.\n\nGitHub Issue: {github_issue_url}\nComment: {comment_body}"

        try:
            # Call your JiraClient to create the issue
            response = jira_client.create_issue(
                summary=summary_text,
                description=description_text
            )
            return jsonify({"status": "success", "jira_key": response.get("key")}), 201
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    return jsonify({"status": "ignored", "reason": "Not a /issue command"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
