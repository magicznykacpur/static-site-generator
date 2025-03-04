from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf node has no value")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
