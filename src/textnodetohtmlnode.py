from leafnode import LeafNode
from textnode import TextType

def text_node_to_html_node(node):
    """
    :type node: TextNode
    """
    if node.text_type == TextType.TEXT:
        return LeafNode(None, node.text)
    elif node.text_type == TextType.BOLD:
        return LeafNode("b", node.text)
    elif node.text_type == TextType.ITALIC:
        return LeafNode("i", node.text)
    elif node.text_type == TextType.CODE:
        return LeafNode("code", node.text)
    elif node.text_type == TextType.LINK:
        return LeafNode("a", node.text, {"href": node.url})
    elif node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": node.url, "alt": node.text})
    else:
        raise Exception("unknown text node type")