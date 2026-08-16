from jira_client import JiraClient

def main():
    print("Connecting to Jira...")
    client = JiraClient()

    summary = "System Maintenance Task"
    description = "Perform routine system cleanup and review application logs."
    issue_type = "Task"  # Options: Task, Bug, Story, Epic (depending on your Jira project settings)

    client.create_issue(
        summary=summary,
        description=description,
        issue_type=issue_type
    )

if __name__ == "__main__":
    main()