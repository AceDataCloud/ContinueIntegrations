import json
import re
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]


class ServiceBlockCatalogTests(unittest.TestCase):
    def test_independent_services_reuse_existing_runtime_without_token_values(self):
        catalog = json.loads((ROOT / "catalog.json").read_text())
        self.assertEqual(
            {service["slug"] for service in catalog["services"]},
            {"suno", "seedance", "happyhorse", "gpt-image", "nano-banana"},
        )
        for service in catalog["services"]:
            directory = ROOT / "blocks" / service["slug"]
            block = (directory / "block.yaml").read_text()
            self.assertEqual(block.count("  - name:"), 1)
            self.assertIn("type: streamable-http", block)
            self.assertIn(service["endpoint_url"], block)
            self.assertIn("${{ secrets.ACEDATACLOUD_API_TOKEN }}", block)
            self.assertNotIn("platform-", block)
            self.assertIsNone(service["official_listing"])
            for filename in ("README.md", "README_zh-CN.md"):
                text = (directory / filename).read_text()
                self.assertIn("General application", text)
                self.assertIn("Initialize General Application", text)
                self.assertIn("task_id", text)
                self.assertIn(service["generate_tool"], text)
                self.assertIn(service["query_tool"], text)
                self.assertIn("Hub", text)
                urls = re.findall(r"https://platform\.acedata\.cloud/[^)\s]+", text)
                self.assertGreaterEqual(len(urls), 2)
                for url in urls:
                    query = parse_qs(urlparse(url).query)
                    self.assertEqual(query.get("utm_source"), ["continue"])
                    self.assertTrue(
                        {"utm_source", "utm_medium", "utm_campaign", "utm_content"}.issubset(query)
                    )

    def test_gpt_image_does_not_claim_its_shared_endpoint_filters_tools(self):
        text = (ROOT / "blocks/gpt-image/README.md").read_text()
        self.assertIn("not a tool or permission filter", text)
        self.assertIn("restrict allowed APIs", text)


if __name__ == "__main__":
    unittest.main()
