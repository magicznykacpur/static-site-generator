import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_should_eq(self):
        node = TextNode("text", TextType.TEXT)
        node2 = TextNode("text", TextType.TEXT)

        self.assertEqual(node, node2)
    
    def test_should_not_eq(self):
        node = TextNode("text", TextType.TEXT)
        node2 = TextNode("other text", TextType.TEXT)

        self.assertNotEqual(node, node2)
    
    def test_should_not_eq_different_type(self):
        node = TextNode("text", TextType.TEXT)
        node2 = TextNode("text", TextType.BOLD)

        self.assertNotEqual(node, node2)

    def test_should_not_have_url(self):
        node = TextNode("text", TextType.TEXT)

        self.assertEqual(None, node.url)

    def test_should_have_url(self):
        node = TextNode("text", TextType.TEXT, "url")

        self.assertEqual("url", node.url)

    def test_repr(self):
        node = TextNode("text", TextType.TEXT, "url")

        self.assertEqual("TextNode(text, TextType.TEXT, url)", repr(node))