import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode("p", None, None, None)
        self.assertEqual("p", node.tag)

    def test_init_with_empty_args(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props_to_html(self):
        node = HTMLNode("a", "click here", None, {"href": "https://example.com", "class": "link"})
        self.assertEqual(' href="https://example.com" class="link"', node.props_to_html())

    def test_empty_props_to_html(self):
        node = HTMLNode()
        self.assertEqual("", node.props_to_html())

    def test_repr(self):
        node = HTMLNode()
        self.assertEqual('HTMLNode(None, None, None, None)', f"{node}")
