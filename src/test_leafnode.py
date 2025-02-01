import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_with_empty_value(self):
        node = LeafNode()
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_empty_tag(self):
        node = LeafNode(None, "some text")
        self.assertEqual("some text", node.to_html())

    def test_to_html_with_tag(self):
        node = LeafNode("p", "text me")
        self.assertEqual('<p>text me</p>', node.to_html())

    def test_to_html_with_tag_and_props(self):
        node = LeafNode("a", "click here", {"href": "https://example.com"})
        self.assertEqual('<a href="https://example.com">click here</a>', node.to_html())
