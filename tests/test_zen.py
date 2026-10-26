# pylint: disable-all
import unittest

ZEN_TEXT = """Beautiful is better than ugly.
Explicit is better than implicit."""

with open("zen.txt", "r") as f:
    zen = f.read().strip()

class TestZen(unittest.TestCase):
    def test_zen_txt_has_02_lines(self):
        self.assertGreaterEqual(len(zen.splitlines()), 2)

    def test_zen_txt_matches_original(self):
        # Strip leading/trailing whitespace from each line before comparison
        zen_lines = [line.strip() for line in ZEN_TEXT.splitlines()]
        content_lines = [line.strip() for line in zen.splitlines()]
        self.assertEqual(content_lines, zen_lines)
