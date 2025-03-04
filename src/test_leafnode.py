import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_create_leaf_node(self):
        node_props = {"prop": "value", "prop2": "value2"}
        node = LeafNode("test value", "p", node_props)

        self.assertListEqual(
            ["test value", "p", node_props], [node.value, node.tag, node.props]
        )

    def test_leaf_to_html(self):
        node = LeafNode("test value", "p")

        self.assertEqual("<p>test value</p>", node.to_html())

    def test_leaf_to_html_with_props(self):
        node_props = {"prop": "value", "prop2": "value2"}
        node = LeafNode("test value", "p", node_props)

        self.assertEqual(
            '<p prop="value" prop2="value2">test value</p>', node.to_html()
        )

    def test_leaf_raises_error_if_no_value(self):
        node = LeafNode(None, "p")

        try:
            self.assertRaises(ValueError, node.to_html())
        except:
            pass

    def test_leaf_to_html_only_value(self):
        node = LeafNode("test value", None)

        self.assertEqual("test value", node.to_html())

