from textnode import TextType, TextNode

class DelimiterMismatchError(Exception):
    def __init__(self, message):
        self.message = f"Delimiter mismatch: {message}"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits each node in the list of old nodes into separate nodes
    based on the content. We create new bold, italic and code TextNode
    instances based on the provided text type and delimiter.

    Assumptions:
    - Types can't be nested (for now)
    - An even number of nodes results in a delimiter mismatch error

    :param old_nodes: list of TextNode
    :param delimiter: string delimiter for splitting the text of the node
    :param text_type: enum value for what element we want to split on
    :return: list of TextNode
    """
    new_nodes = []
    for node in old_nodes:
        # TODO we need to parse these if we want to support nested elements
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        chunks = node.text.split(delimiter)
        # split will give us an empty string if the delimiter occurs at the beginning
        # or end of the text; as a result, we always expect an odd number of chunks.
        # As a result, if we have an even number of chunks, we have a delimiter mismatch.
        if len(chunks) % 2 == 0:
            raise DelimiterMismatchError(delimiter)

        # An empty string indicates that the next chunk MUST be within the delimiter;
        # If it is at the beginning of the text, we have a starting delimiter; if it
        # occurs in the middle, we have two adjacent delimiters; and if it occurs at the
        # end, we have a closing delimiter, so we can close switch back.
        current_text_type = TextType.TEXT
        for chunk in chunks:
            if len(chunk) == 0: # two contiguous entries of the same type
                current_text_type = text_type
                continue # don't add the empty node?

            new_nodes.append(TextNode(chunk, current_text_type))
            if current_text_type == TextType.TEXT:
                current_text_type = text_type
            else:
                current_text_type = TextType.TEXT
    return new_nodes




