import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_should_create_empty_node(self):
        node = HTMLNode()

        self.assertListEqual(
            [None, None, None, None], [node.tag, node.value, node.children, node.props]
        )

    def test_should_create_node(self):
        node_children = [HTMLNode(), HTMLNode()]
        node_props = {"prop": "value", "prop2": "value2"}

        node = HTMLNode(
            "p",
            "paragraph",
            node_children,
            node_props,
        )

        self.assertListEqual(
            ["p", "paragraph", node_children, node_props],
            [node.tag, node.value, node.children, node.props],
        )

    def test_should_parse_props_to_html(self):
        node_props = {"prop": "value", "prop2": "value2"}
        node = HTMLNode(None, None, None, node_props)

        html_props = node.props_to_html()

        self.assertEqual(' prop="value" prop2="value2"', html_props)

    def test_should_return_empty_string_for_empty_props(self):
        node = HTMLNode(None, None, None, None)

        self.assertEqual("", node.props_to_html())

    def test_repr_for_empty_node(self):
        node = HTMLNode(None, None, None, None)

        self.assertEqual(
            "HTMLNode(tag=None, value=None, children=None, props=None)", repr(node)
        )

    def test_repr_for_non_empty_node(self):
        node_children = [HTMLNode(), HTMLNode()]
        node_props = {"prop": "value", "prop2": "value2"}
        node = HTMLNode("p", "paragraph", node_children, node_props)

        self.assertEqual(
            "HTMLNode(tag=p, value=paragraph, children=[HTMLNode(tag=None, value=None, children=None, props=None), HTMLNode(tag=None, value=None, children=None, props=None)], props={'prop': 'value', 'prop2': 'value2'})",
            repr(node),
        )
