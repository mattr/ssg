import unittest
from textnodetohtmlnode import text_node_to_html_node
from textnode import TextType, TextNode


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_to_html(self):
        node = TextNode("some text", TextType.TEXT)
        self.assertEqual("some text", text_node_to_html_node(node).to_html())

    def test_bold_to_html(self):
        node = TextNode("some text", TextType.BOLD)
        self.assertEqual("<b>some text</b>", text_node_to_html_node(node).to_html())

    def test_italic_to_html(self):
        node = TextNode("some text", TextType.ITALIC)
        self.assertEqual("<i>some text</i>", text_node_to_html_node(node).to_html())

    def test_code_to_html(self):
        node = TextNode("some text", TextType.CODE)
        self.assertEqual("<code>some text</code>", text_node_to_html_node(node).to_html())

    def test_link_to_html(self):
        node = TextNode("some text", TextType.LINK, "https://example.com")
        self.assertEqual('<a href="https://example.com">some text</a>', text_node_to_html_node(node).to_html())

    def test_image_to_html(self):
        node = TextNode("some text", TextType.IMAGE, "https://example.com/image.png")
        self.assertEqual('<img src="https://example.com/image.png" alt="some text"/>',
                         text_node_to_html_node(node).to_html())
