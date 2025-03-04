import unittest

from extract_markdown import extract_markdown_images, split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitter(unittest.TestCase):
    def test_split_nodes_raises_exception_for_period(self):
        nodes = [
            TextNode("test text", TextType.TEXT),
            TextNode("test text", TextType.TEXT),
        ]

        try:
            self.assertRaises(
                Exception, split_nodes_delimiter(nodes, ".", TextType.TEXT)
            )
        except:
            pass

    def test_split_nodes_raises_exception_for_comma(self):
        nodes = [
            TextNode("test text", TextType.TEXT),
            TextNode("test text", TextType.TEXT),
        ]

        try:
            self.assertRaises(
                Exception, split_nodes_delimiter(nodes, ",", TextType.TEXT)
            )
        except:
            pass

    def test_split_nodes_splits_bold(self):
        nodes = [
            TextNode("This is a **bold** sample", TextType.TEXT),
            TextNode("This is a text sample", TextType.TEXT),
        ]

        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" sample", TextType.TEXT),
                TextNode("This is a text sample", TextType.TEXT),
            ],
            split_nodes_delimiter(nodes, "**", TextType.BOLD),
        )

    def test_split_nodes_splits_bold_between(self):
        nodes = [
            TextNode("This is a text sample", TextType.TEXT),
            TextNode("This is a **bold** sample", TextType.TEXT),
            TextNode("This is a text sample", TextType.TEXT),
        ]

        self.assertListEqual(
            [
                TextNode("This is a text sample", TextType.TEXT),
                TextNode("This is a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" sample", TextType.TEXT),
                TextNode("This is a text sample", TextType.TEXT),
            ],
            split_nodes_delimiter(nodes, "**", TextType.BOLD),
        )

    def test_split_nodes_splits_two_bold(self):
        nodes = [
            TextNode("This is a text sample", TextType.TEXT),
            TextNode("This is a **bold** sample", TextType.TEXT),
            TextNode("This is a **bold** sample", TextType.TEXT),
        ]

        self.assertListEqual(
            [
                TextNode("This is a text sample", TextType.TEXT),
                TextNode("This is a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" sample", TextType.TEXT),
                TextNode("This is a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" sample", TextType.TEXT),
            ],
            split_nodes_delimiter(nodes, "**", TextType.BOLD),
        )

    def test_split_nodes_splits_italic(self):
        nodes = [
            TextNode("This is a _italic_ sample", TextType.TEXT),
            TextNode("This is a text sample", TextType.TEXT),
        ]

        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" sample", TextType.TEXT),
                TextNode("This is a text sample", TextType.TEXT),
            ],
            split_nodes_delimiter(nodes, "_", TextType.ITALIC),
        )

    def test_split_nodes_splits_italic_between(self):
        nodes = [
            TextNode("This is a text sample", TextType.TEXT),
            TextNode("This is a _italic_ sample", TextType.TEXT),
            TextNode("This is a text sample", TextType.TEXT),
        ]

        self.assertListEqual(
            [
                TextNode("This is a text sample", TextType.TEXT),
                TextNode("This is a ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" sample", TextType.TEXT),
                TextNode("This is a text sample", TextType.TEXT),
            ],
            split_nodes_delimiter(nodes, "_", TextType.ITALIC),
        )

    def test_split_nodes_splits_two_italic(self):
        nodes = [
            TextNode("This is a text sample", TextType.TEXT),
            TextNode("This is a _italic_ sample", TextType.TEXT),
            TextNode("This is a text sample", TextType.TEXT),
            TextNode("This is a _italic_ sample", TextType.TEXT),
        ]

        self.assertListEqual(
            [
                TextNode("This is a text sample", TextType.TEXT),
                TextNode("This is a ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" sample", TextType.TEXT),
                TextNode("This is a text sample", TextType.TEXT),
                TextNode("This is a ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" sample", TextType.TEXT),
            ],
            split_nodes_delimiter(nodes, "_", TextType.ITALIC),
        )

    def test_split_nodes_splits_code(self):
        nodes = [
            TextNode("This is a text sample", TextType.TEXT),
            TextNode("This is a `code` sample", TextType.TEXT),
        ]

        self.assertListEqual(
            [
                TextNode("This is a text sample", TextType.TEXT),
                TextNode("This is a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" sample", TextType.TEXT),
            ],
            split_nodes_delimiter(nodes, "`", TextType.CODE),
        )

    def test_split_nodes_splits_code_between(self):
        nodes = [
            TextNode("This is a text sample", TextType.TEXT),
            TextNode("This is a `code` sample", TextType.TEXT),
            TextNode("This is a text sample", TextType.TEXT),
        ]

        self.assertListEqual(
            [
                TextNode("This is a text sample", TextType.TEXT),
                TextNode("This is a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" sample", TextType.TEXT),
                TextNode("This is a text sample", TextType.TEXT),
            ],
            split_nodes_delimiter(nodes, "`", TextType.CODE),
        )

    def test_split_nodes_splits_two_code(self):
        nodes = [
            TextNode("This is a text sample", TextType.TEXT),
            TextNode("This is a `code` sample", TextType.TEXT),
            TextNode("This is a `code` sample", TextType.TEXT),
            TextNode("This is a text sample", TextType.TEXT),
        ]

        self.assertListEqual(
            [
                TextNode("This is a text sample", TextType.TEXT),
                TextNode("This is a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" sample", TextType.TEXT),
                TextNode("This is a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" sample", TextType.TEXT),
                TextNode("This is a text sample", TextType.TEXT),
            ],
            split_nodes_delimiter(nodes, "`", TextType.CODE),
        )

    def test_split_nodes_three_bold_in_one(self):
        node = TextNode(
            "what if **one bold** and **two bold** and **three bold**, dang",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("what if ", TextType.TEXT),
                TextNode("one bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("two bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("three bold", TextType.BOLD),
                TextNode(", dang", TextType.TEXT),
            ],
            split_nodes_delimiter([node], "**", TextType.BOLD),
        )

    def test_split_nodes_one_bold(self):
        node = TextNode("**one bold**", TextType.TEXT)

        self.assertEqual(
            [TextNode("one bold", TextType.BOLD)],
            split_nodes_delimiter([node], "**", TextType.BOLD),
        )

    def test_split_nodes_three_italic_in_one(self):
        node = TextNode(
            "what if _one italic_ and _two italic_ and _three italic_, dang",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("what if ", TextType.TEXT),
                TextNode("one italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("two italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("three italic", TextType.ITALIC),
                TextNode(", dang", TextType.TEXT),
            ],
            split_nodes_delimiter([node], "_", TextType.ITALIC),
        )

    def test_split_nodes_one_bold_and_one_italic(self):
        node = TextNode("**one bold** and _one_ italic", TextType.TEXT)

        bold_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            [
                TextNode("one bold", TextType.BOLD),
                TextNode(" and _one_ italic", TextType.TEXT),
            ],
            bold_nodes,
        )

        italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
        self.assertEqual(
            [
                TextNode("one bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("one", TextType.ITALIC),
                TextNode(" italic", TextType.TEXT),
            ],
            italic_nodes,
        )

    def test_extract_one_image(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"

        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            extract_markdown_images(text),
        )

    def test_extract_two_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            extract_markdown_images(text),
        )

    def test_extract_one_link(self):
        text = "This is text with link ![to youtube](https://www.youtube.com)"

        self.assertListEqual(
            [("to youtube", "https://www.youtube.com")],
            extract_markdown_images(text),
        )

    def test_extract_two_links(self):
        text = "This is text with link ![to youtube](https://www.youtube.com) and ![to google](https://www.google.com)"

        self.assertListEqual(
            [
                ("to youtube", "https://www.youtube.com"),
                ("to google", "https://www.google.com"),
            ],
            extract_markdown_images(text),
        )
