import unittest

from splitnodesdelimiter import split_nodes_delimiter, DelimiterMismatchError
from textnode import TextType, TextNode


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_bold_ignores_italic_and_code(self):
        node = TextNode("**Bold words** are often `coded` to be *fancy*", TextType.TEXT)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [TextNode("Bold words", TextType.BOLD),
                    TextNode(" are often `coded` to be *fancy*", TextType.TEXT)]
        self.assertEqual(actual, expected)

    # NOTE: We have to parse bold before italic to prevent ** being triggered as contiguous italics
    def test_split_italic_ignores_code(self):
        node = TextNode("Code words are *just* like `code` words", TextType.TEXT)
        actual = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [TextNode("Code words are ", TextType.TEXT),
                    TextNode("just", TextType.ITALIC),
                    TextNode(" like `code` words", TextType.TEXT)]
        self.assertEqual(actual, expected)

    def test_code_ignores_bold_and_italic(self):
        node = TextNode("**Bold words** are often `coded` to be *fancy*", TextType.TEXT)
        actual = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("**Bold words** are often ", TextType.TEXT),
                    TextNode("coded", TextType.CODE),
                    TextNode(" to be *fancy*", TextType.TEXT)]
        self.assertEqual(actual, expected)

    def test_non_text_nodes_are_added_without_change(self):
        node = TextNode("Bold words", TextType.BOLD)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(actual, [node])

    def test_mismatched_delimiters_throws_an_exception(self):
        with self.assertRaises(DelimiterMismatchError):
            split_nodes_delimiter([TextNode("Mismatched **delimiter", TextType.TEXT)], "**", TextType.BOLD)