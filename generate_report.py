import json
from pathlib import Path
from datetime import datetime, timezone

INPUT_FILE = Path("data/latest_news.json")
OUTPUT_FILE = Path("AI_NEWS_REPORT.md")


def generate_report():
    if not INPUT_FILE.exists():
        print("No news data found.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        articles = json.load(file)

    if not articles:
        print("No articles available.")
        return

    report = [
        "# AI & Technology News Report",
        "",
        "Automatically generated from public AI news feeds.",
        "",
        f"**Total Articles:** {len(articles)}",
        "",
    ]

    sources = sorted(set(article["source"] for article in articles))

    for source in sources:
        report.append(f"## {source}")
        report.append("")

        source_articles = [
            article for article in articles
            if article["source"] == source
        ]

        for article in source_articles:
            title = article["title"]
            url = article["url"]

            report.append(f"- [{title}]({url})")

        report.append("")

    OUTPUT_FILE.write_text(
        "\n".join(report) + "\n",
        encoding="utf-8"
    )

    print(f"Report generated with {len(articles)} articles.")


if __name__ == "__main__":
    generate_report()
