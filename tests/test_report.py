import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import generate_report


class TestReportGenerator(unittest.TestCase):

    def test_report_generation(self):
        articles = [
            {
                "source": "Google AI",
                "title": "New AI Research",
                "url": "https://example.com/research"
            },
            {
                "source": "TechCrunch AI",
                "title": "AI Technology Update",
                "url": "https://example.com/update"
            }
        ]

        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            input_file = folder / "news.json"
            output_file = folder / "report.md"

            input_file.write_text(
                json.dumps(articles),
                encoding="utf-8"
            )

            with patch.object(generate_report, "INPUT_FILE", input_file), \
                 patch.object(generate_report, "OUTPUT_FILE", output_file):

                generate_report.generate_report()

            self.assertTrue(output_file.exists())

            report = output_file.read_text(encoding="utf-8")

            self.assertIn("New AI Research", report)
            self.assertIn("AI Technology Update", report)
            self.assertIn("Google AI", report)
            self.assertIn("TechCrunch AI", report)
            self.assertIn("https://example.com/research", report)


if __name__ == "__main__":
    unittest.main()
