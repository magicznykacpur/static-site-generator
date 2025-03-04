import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_create_parent_node(self):
        node = ParentNode("p", [])

        self.assertListEqual(["p", []], [node.tag, node.children])

    def test_create_parent_node_with_children(self):
        node_children = [LeafNode("test value", "div"), LeafNode("test value", "div")]
        node = ParentNode("p", node_children)

        self.assertListEqual(["p", node_children], [node.tag, node.children])

    def test_should_raise_error_if_tag_not_defined(self):
        node = ParentNode(None, [])

        try:
            self.assertRaises(ValueError, node.to_html())
        except:
            pass

    def test_should_return_html_with_simple_children(self):
        node_children = [LeafNode("test value", "p"), LeafNode("test value", "p")]
        node = ParentNode("div", node_children)

        self.assertEqual(
            "<div><p>test value</p><p>test value</p></div>", node.to_html()
        )

    def test_should_return_html_with_many_children(self):
        node_children = [
            LeafNode("test value", "p"),
            LeafNode("test value", "div"),
            LeafNode("test value", "a"),
            LeafNode("test value", "article"),
            LeafNode("test value", "h2"),
        ]
        node = ParentNode("div", node_children)

        self.assertEqual(
            "<div><p>test value</p><div>test value</div><a>test value</a><article>test value</article><h2>test value</h2></div>",
            node.to_html(),
        )

    def test_should_return_html_with_nested_parents(self):
        node_children = [
            LeafNode("test value", "p"),
            ParentNode(
                "div", [LeafNode("test value", "p"), LeafNode("test value", "p")]
            ),
            LeafNode("test value", "a"),
            ParentNode(
                "article", [LeafNode("test value", "p"), LeafNode("test value", "p")]
            ),
            LeafNode("test value", "h2"),
        ]
        node = ParentNode("div", node_children)

        self.assertEqual(
            "<div><p>test value</p><div><p>test value</p><p>test value</p></div><a>test value</a><article><p>test value</p><p>test value</p></article><h2>test value</h2></div>",
            node.to_html(),
        )

    def test_should_return_html_with_double_nested_parents(self):
        node_children = [
            LeafNode("test value", "p"),
            ParentNode(
                "div",
                [
                    LeafNode("test value", "p"),
                    ParentNode(
                        "div",
                        [LeafNode("test value", "p"), LeafNode("test value", "p")],
                    ),
                ],
            ),
            LeafNode("test value", "a"),
            ParentNode(
                "article",
                [
                    LeafNode("test value", "p"),
                    ParentNode(
                        "div",
                        [LeafNode("test value", "p"), LeafNode("test value", "p")],
                    ),
                ],
            ),
            LeafNode("test value", "h2"),
        ]
        node = ParentNode("div", node_children)

        self.assertEqual(
            "<div><p>test value</p><div><p>test value</p><div><p>test value</p><p>test value</p></div></div><a>test value</a><article><p>test value</p><div><p>test value</p><p>test value</p></div></article><h2>test value</h2></div>",
            node.to_html(),
        )
