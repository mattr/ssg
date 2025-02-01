import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("this has different text", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)

    def test_repr(self):
        node = TextNode("This is a link node", TextType.LINK, "https://example.com")
        self.assertEqual(f"{node}", "TextNode(This is a link node, link, https://example.com)")

    def test_init(self):
        node = TextNode("Code node", TextType.CODE)
        self.assertEqual("Code node", node.text)
        self.assertEqual(TextType.CODE, node.text_type)
        self.assertIsNone(node.url)


if __name__ == "__main__":
    unittest.main()
