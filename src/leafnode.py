from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf node must have a value")

        if not self.tag:
            return self.value

        if len(self.value) == 0:
            """
            Assume an empty value is a self-closing tag (we only have `img`)
            """
            return f"<{self.tag}{self.props_to_html()}/>"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
