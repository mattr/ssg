import re

from blocktoblocktype import block_to_block_type
from leafnode import LeafNode
from markdowntoblocks import markdown_to_blocks
from parentnode import ParentNode
from textnodetohtmlnode import text_node_to_html_node
from texttotextnodes import text_to_text_nodes


def text_nodes_to_html_nodes(nodes):
    return list(map(lambda x: text_node_to_html_node(x), nodes))

def create_heading(block):
    elements = re.match(r"\A(#{1,6}) (.*)", block)
    heading_size = len(elements.group(1))
    nodes = text_to_text_nodes(elements.group(2))
    return ParentNode(f"h{heading_size}", text_nodes_to_html_nodes(nodes))

def create_code(block):
    text = block.replace("```", "")
    return ParentNode("pre", [LeafNode("code", text.strip())])

def create_paragraph(block):
    nodes = text_to_text_nodes(block.replace("\n", " "))
    return ParentNode("p", text_nodes_to_html_nodes(nodes))

def create_list_item(text):
    nodes = text_to_text_nodes(text)
    return ParentNode("li", text_nodes_to_html_nodes(nodes))

def create_unordered_list(block):
    lines = block.split("\n")
    list_items = list(map(lambda x: create_list_item(x.replace("* ", "", 1)), lines))
    return ParentNode("ul", list_items)

def create_ordered_list(block):
    lines = block.split("\n")
    list_items = []
    for line in lines:
        text = re.match(r"\A\d+\. (.*)", line).group(1)
        list_items.append(create_list_item(text))
    return ParentNode("ol", list_items)

def create_quote(block):
    lines = block.split("\n")
    texts = []
    for line in lines:
        text = re.match(r"\A>(.*)", line).group(1)
        texts.append(text.lstrip())
    nodes = text_to_text_nodes(" ".join(texts))
    return ParentNode("blockquote", text_nodes_to_html_nodes(nodes))

def convert_block_to_node(block):
    block_type = block_to_block_type(block)
    if block_type == "heading":
        return create_heading(block)
    elif block_type == "code":
        return create_code(block)
    elif block_type == "unordered_list":
        return create_unordered_list(block)
    elif block_type == "ordered_list":
        return create_ordered_list(block)
    elif block_type == "quote":
        return create_quote(block)
    else:
        return create_paragraph(block)

def markdown_to_html_node(text):
    root = ParentNode("div", [], None)

    blocks = markdown_to_blocks(text)
    for block in blocks:
        root.children.append(convert_block_to_node(block))
    return root
