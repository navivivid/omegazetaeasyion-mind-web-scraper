import unittest
from src.scraper import scrape_website

class TestScraper(unittest.TestCase):
    def test_scrape_website(self):
        result = scrape_website('https://example.com')
        self.assertIsNotNone(result)