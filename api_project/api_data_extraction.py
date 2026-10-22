"""Beginner REST API to JSON to CSV example.

Educational practice only: JSONPlaceholder returns demonstration data, not market data.
Run from the project root:
    python api_project/api_data_extraction.py
"""
import csv
import json
from pathlib import Path

import requests

API_URL = "https://api.jsonplaceholder.dev/posts"
OUTPUT_FILE = Path(__file__).parent / "data" / "api_posts.csv"


def main():
    try:
        response = requests.get(API_URL, timeout=20)
        print("HTTP status:", response.status_code)
        response.raise_for_status()
        records = response.json()
    except requests.exceptions.RequestException as error:
        print("Could not contact the API. Check your internet connection.")
        print("Technical details:", error)
        return
    except json.JSONDecodeError:
        print("The server response was not valid JSON.")
        return

    if not isinstance(records, list):
        print("Unexpected response: expected a JSON list.")
        return

    if not records:
        print("The API returned no records.")
        return

    # Keep a stable set of columns for this learning assignment.
    columns = ["userId", "id", "title", "body"]
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    try:
        with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=columns, extrasaction="ignore")
            writer.writeheader()
            for record in records:
                if isinstance(record, dict):
                    writer.writerow({column: record.get(column, "") for column in columns})
    except OSError as error:
        print("Could not save CSV:", error)
        return

    print(f"Records received: {len(records)}")
    print("First three records:")
    for record in records[:3]:
        print(record)
    print(f"\nCSV saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
