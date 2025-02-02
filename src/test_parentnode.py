import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_no_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_empty_children(self):
        node = ParentNode("p", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_only_leaf_children(self):
        node = ParentNode("p",
                          [LeafNode(None, "plain"),
                           LeafNode("strong", "is strong"),
                           LeafNode(None, "and"),
                           LeafNode("em", "is fast")])
        self.assertEqual("<p>plain<strong>is strong</strong>and<em>is fast</em></p>", node.to_html())

    def test_to_html_with_parent_node_props(self):
        children = [LeafNode("p", "text"),
                    ParentNode("p", [
                        LeafNode(None, "plain"),
                        LeafNode("strong", "is strong"),
                        LeafNode(None, "and"),
                        LeafNode("em", "is fast")
                    ]),
                    LeafNode("p", "more text", {"class": "text"})]
        node = ParentNode("div", children)
        self.assertEqual(
            '<div><p>text</p><p>plain<strong>is strong</strong>and<em>is fast</em></p><p class="text">more text</p></div>',
            node.to_html()
        )
