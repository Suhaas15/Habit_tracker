import os
import requests
from datetime import datetime, timezone

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
PIXELA_TOKEN = os.environ["PIXELA_TOKEN"]
USERNAME = "suhaas15"
GRAPH_ID = "graph1"

def get_today_contributions():
    today = datetime.now(timezone.utc).date().isoformat()
    query = """
    query ($login: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $login) {
        contributionsCollection(from: $from, to: $to) {
          contributionCalendar {
            totalContributions
          }
        }
      }
    }
    """
    variables = {
        "login": USERNAME,
        "from": f"{today}T00:00:00Z",
        "to":   f"{today}T23:59:59Z"
    }
    r = requests.post(
        "https://api.github.com/graphql",
        json={"query": query, "variables": variables},
        headers={"Authorization": f"Bearer {GITHUB_TOKEN}"}
    )
    r.raise_for_status()
    return r.json()["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]

def update_pixela(quantity: int):
    pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
    today_str = datetime.now().strftime("%Y%m%d")
    payload = {"date": today_str, "quantity": str(quantity)}
    r = requests.post(pixel_endpoint,
                      json=payload,
                      headers={"X-USER-TOKEN": PIXELA_TOKEN})
    r.raise_for_status()
    print("Pixela response:", r.text)

if __name__ == "__main__":
    count = get_today_contributions()
    update_pixela(count)