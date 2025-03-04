import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextToHTML(unittest.TestCase):
    def test_text_to_text(self):
        text_node = TextNode("test text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)

        self.assertListEqual([None, "test text"], [html_node.tag, html_node.value])

    def test_text_to_bold(self):
        text_node = TextNode("test text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)

        self.assertListEqual(["b", "test text"], [html_node.tag, html_node.value])

    def test_text_to_italic(self):
        text_node = TextNode("test text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)

        self.assertListEqual(["i", "test text"], [html_node.tag, html_node.value])

    def test_text_to_code(self):
        text_node = TextNode("test text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)

        self.assertListEqual(["code", "test text"], [html_node.tag, html_node.value])

    def test_text_to_link(self):
        text_node = TextNode("test text", TextType.LINK, "url.com")
        html_node = text_node_to_html_node(text_node)

        self.assertListEqual(
            ["a", "test text", "url.com"],
            [
                html_node.tag,
                html_node.value,
                html_node.props["href"],
            ],
        )

    def test_text_to_img(self):
        text_node = TextNode("test text", TextType.IMAGE, "url.com")
        html_node = text_node_to_html_node(text_node)

        self.assertListEqual(
            ["img", "", "test text", "url.com"],
            [
                html_node.tag,
                html_node.value,
                html_node.props["alt"],
                html_node.props["src"],
            ],
        )
