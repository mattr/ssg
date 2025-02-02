from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.children:
            raise ValueError("parent node must have children")

        elements = [f"<{self.tag}{self.props_to_html()}>"]
        for child in self.children:
            elements.append(child.to_html())
        elements.append(f"</{self.tag}>")
        return "".join(elements)
