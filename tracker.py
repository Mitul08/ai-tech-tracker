import json
import urllib.request
from pathlib import Path
from datetime import datetime, timezone
import xml.etree.ElementTree as ET

FEEDS = {
    "Google AI": "https://blog.google/technology/ai/rss/",
    "TechCrunch AI": "https://techcrunch.com/category/artificial-intelligence/feed/",
}

OUTPUT = Path("data/latest_news.json")


def fetch_news():
    articles = []

    for source, url in FEEDS.items():
        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "AI-Tech-Tracker/1.0"}
            )

            with urllib.request.urlopen(request, timeout=20) as response:
                root = ET.fromstring(response.read())

            for item in root.findall(".//item")[:10]:
                title = item.findtext("title")
                link = item.findtext("link")

                if title and link:
                    articles.append({
                        "source": source,
                        "title": title,
                        "url": link
                    })

        except Exception as error:
            print(f"Error fetching {source}: {error}")

    return sorted(
        articles,
        key=lambda article: (
            article["source"],
            article["title"]
        )
    )


def main():
    articles = fetch_news()

    if not articles:
        print("No articles fetched. Keeping existing data.")
        return

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    new_content = json.dumps(
        articles,
        indent=2,
        ensure_ascii=False
    ) + "\n"

    old_content = (
        OUTPUT.read_text(encoding="utf-8")
        if OUTPUT.exists()
        else ""
    )

    if new_content != old_content:
        OUTPUT.write_text(new_content, encoding="utf-8")
        print(f"Updated {len(articles)} articles.")
    else:
        print("No changes detected.")


if __name__ == "__main__":
    main()
