import unittest

from extractmarkdownimages import extract_markdown_images


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "![alt text](https://example.com/image.png) or ![](https://example.com/alt.png)"
        expected = [("alt text", "https://example.com/image.png"),
                    ("", "https://example.com/alt.png")]
        actual = extract_markdown_images(text)
        self.assertEqual(expected, actual)
