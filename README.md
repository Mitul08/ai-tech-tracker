# AI Tech Tracker

### Automated AI & Technology News Aggregator

A Python-based automation project that collects the latest AI and technology news from publicly available RSS feeds, processes the information, and generates a structured Markdown report using GitHub Actions.

The project runs automatically every day without requiring manual intervention.

## Features

- **Automated News Collection:** Retrieves recent AI-related articles from RSS feeds.
- **Multiple Sources:** Collects articles from Google AI and TechCrunch AI.
- **Structured Data Storage:** Saves article information in JSON format.
- **Automated Report Generation:** Converts collected articles into an easy-to-read Markdown report.
- **Change Detection:** Commits updated data only when file contents change.
- **Scheduled Execution:** Uses GitHub Actions to run daily.
- **Manual Execution:** Supports manually triggering the workflow.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Core automation |
| GitHub Actions | Workflow scheduling and execution |
| XML ElementTree | RSS feed parsing |
| JSON | Structured data storage |
| Markdown | Report generation |
| Git | Version control |

## Project Structure

```text
ai-tech-tracker/
│
├── .github/
│   └── workflows/
│       └── daily-tracker.yml
│
├── data/
│   └── latest_news.json
│
├── tracker.py
├── generate_report.py
├── AI_NEWS_REPORT.md
├── README.md
└── LICENSE
```

## How It Works

1. GitHub Actions triggers the workflow daily.
2. `tracker.py` fetches recent articles from configured RSS feeds.
3. Articles are extracted and saved to `data/latest_news.json`.
4. `generate_report.py` organizes the collected articles by source.
5. A Markdown report is generated as `AI_NEWS_REPORT.md`.
6. GitHub Actions automatically commits updated files when changes are detected.

## Latest AI News Report

View the automatically generated report:

**[Read Latest AI News](AI_NEWS_REPORT.md)**

## Running Locally

Clone the repository:

```bash
git clone https://github.com/Mitul08/ai-tech-tracker.git
```

Navigate to the project directory:

```bash
cd ai-tech-tracker
```

Run the news collection script:

```bash
python3 tracker.py
```

Generate the Markdown report:

```bash
python3 generate_report.py
```

No additional third-party Python packages are required.

## Automation Schedule

The GitHub Actions workflow is scheduled to run daily at approximately **9:00 AM IST**.

You can also manually execute the workflow from the repository's **Actions** tab.

## Future Improvements

- Add additional AI and technology news sources.
- Implement persistent article history.
- Improve duplicate article detection.
- Introduce article filtering and search.
- Add automated tests.
- Build a web dashboard.

## Author

**Mitul Sharma**

GitHub: [@Mitul08](https://github.com/Mitul08)

## License

This project is licensed under the MIT License.
