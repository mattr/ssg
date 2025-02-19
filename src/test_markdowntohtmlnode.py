import textwrap
from unittest import TestCase

from leafnode import LeafNode
from markdowntohtmlnode import markdown_to_html_node
from parentnode import ParentNode


def parent_node_with(children):
    return ParentNode("div", children)


class Test(TestCase):
    def test_create_heading(self):
        text = "# Heading 1"
        actual = markdown_to_html_node(text)
        expected = parent_node_with([ParentNode("h1", [LeafNode(None, "Heading 1")])])
        self.assertEqual(actual, expected)

    def test_create_code(self):
        text = textwrap.dedent("""\
            ```
            code block
            ```
            """)
        actual = markdown_to_html_node(text)
        expected = ParentNode("div", [
            ParentNode("pre", [LeafNode("code", "code block")])
        ])
        self.assertEqual(expected, actual)

    def test_create_blockquote(self):
        text = textwrap.dedent("""\
        > This is a **quote** with
        > *some* internal formatting.
        """)
        actual = markdown_to_html_node(text)
        expected = parent_node_with([
            ParentNode("blockquote", [
                LeafNode(None, "This is a "),
                LeafNode("b", "quote"),
                LeafNode(None, " with "),
                LeafNode("i", "some"),
                LeafNode(None," internal formatting.")
            ])
        ])
        self.assertEqual(expected, actual)

    def test_create_unordered_list(self):
        text = textwrap.dedent("""\
        * item 1
        * item 2 is **great**
        * item 3 is *fine*
        """)
        actual = markdown_to_html_node(text)
        expected = parent_node_with([
            ParentNode("ul", [
                ParentNode("li", [LeafNode(None, "item 1")]),
                ParentNode("li", [LeafNode(None, "item 2 is "), LeafNode("b", "great")]),
                ParentNode("li", [LeafNode(None, "item 3 is "), LeafNode("i", "fine")]),
            ])
        ])
        self.assertEqual(expected, actual)

    def test_create_ordered_list(self):
        text = textwrap.dedent("""\
                1. item 1
                2. item 2 is **great**
                3. item 3 is *fine*
                """)
        actual = markdown_to_html_node(text)
        expected = parent_node_with([
            ParentNode("ol", [
                ParentNode("li", [LeafNode(None, "item 1")]),
                ParentNode("li", [LeafNode(None, "item 2 is "), LeafNode("b", "great")]),
                ParentNode("li", [LeafNode(None, "item 3 is "), LeafNode("i", "fine")]),
            ])
        ])
        self.assertEqual(expected, actual)

    def test_create_paragraph(self):
        text = textwrap.dedent("""\
        A paragraph can span multiple lines,
        and may have **explicit** line breaks
        throughout the *text*.
        """)
        actual = markdown_to_html_node(text)
        expected = parent_node_with([
            ParentNode("p", [
                LeafNode(None, "A paragraph can span multiple lines, and may have "),
                LeafNode("b", "explicit"),
                LeafNode(None, " line breaks throughout the "),
                LeafNode("i", "text"),
                LeafNode(None, ".")
            ])
        ])
        self.assertEqual(expected, actual)
