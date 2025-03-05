import unittest

from extract_markdown import (
    extract_markdown_images,
    extract_title,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_text_nodes,
)
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

    def test_split_images_no_matches(self):
        nodes = [
            TextNode("This is a text without a image", TextType.TEXT),
            TextNode("This is a text without a image", TextType.TEXT),
            TextNode("This is a text without a image", TextType.TEXT),
        ]
        new_nodes = split_nodes_image(nodes)

        self.assertListEqual(nodes, new_nodes)

    def test_split_only_one_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            split_nodes_image([node]),
        )

    def test_split_text_and_one_image(self):
        node = TextNode(
            "This is a text with ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("This is a text with ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            split_nodes_image([node]),
        )

    def test_split_text_and_one_image_and_more_text(self):
        node = TextNode(
            "This is a text with ![image](https://i.imgur.com/zjjcJKZ.png) and more text",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("This is a text with ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and more text", TextType.TEXT),
            ],
            split_nodes_image([node]),
        )

    def test_split_only_two_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            split_nodes_image([node]),
        )

    def test_split_text_with_two_images_one_after_another(self):
        node = TextNode(
            "This is text with images ![image](https://i.imgur.com/zjjcJKZ.png) ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("This is text with images ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            split_nodes_image([node]),
        )

    def test_split_text_with_two_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_link_no_matches(self):
        nodes = [
            TextNode("This is a text without a link", TextType.TEXT),
            TextNode("This is a text without a link", TextType.TEXT),
            TextNode("This is a text without a link", TextType.TEXT),
        ]
        new_nodes = split_nodes_link(nodes)

        self.assertListEqual(nodes, new_nodes)

    def test_split_only_one_link(self):
        node = TextNode(
            "[to google](https://www.google.com)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("to google", TextType.LINK, "https://www.google.com"),
            ],
            split_nodes_link([node]),
        )

    def test_split_text_and_one_link(self):
        node = TextNode(
            "This is a text with a [to google](https://www.google.com)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("to google", TextType.LINK, "https://www.google.com"),
            ],
            split_nodes_link([node]),
        )

    def test_split_text_and_one_image_and_more_text(self):
        node = TextNode(
            "This is a text with a [to google](https://www.google.com) and more text",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("to google", TextType.LINK, "https://www.google.com"),
                TextNode(" and more text", TextType.TEXT),
            ],
            split_nodes_link([node]),
        )

    def test_split_text_with_two_images(self):
        node = TextNode(
            "This is text with a [to google](https://www.google.com) and another [to youtube](https://www.youtube.com)",
            TextType.TEXT,
        )

        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("to google", TextType.LINK, "https://www.google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com"),
            ],
            split_nodes_link([node]),
        )

    def test_text_to_text_nodes_bold(self):
        text = "This is **bold text** with some other words in it"

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(" with some other words in it", TextType.TEXT),
            ],
            text_to_text_nodes(text),
        )

    def test_text_to_text_nodes_bold_and_italic(self):
        text = "This is **bold text** with some _italic words_ in it"

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(" with some ", TextType.TEXT),
                TextNode("italic words", TextType.ITALIC),
                TextNode(" in it", TextType.TEXT),
            ],
            text_to_text_nodes(text),
        )

    def test_text_to_text_nodes_bold_and_italic_and_code(self):
        text = "This is **bold text** with some _italic words_ in it, and a `code block` too"

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(" with some ", TextType.TEXT),
                TextNode("italic words", TextType.ITALIC),
                TextNode(" in it, and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" too", TextType.TEXT),
            ],
            text_to_text_nodes(text),
        )

    def test_text_to_text_nodes_bold_and_italic_and_code_and_image(self):
        text = "This is **bold text** with some _italic words_ in it, and a `code block` too, and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(" with some ", TextType.TEXT),
                TextNode("italic words", TextType.ITALIC),
                TextNode(" in it, and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" too, and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
            ],
            text_to_text_nodes(text),
        )

    def test_text_to_text_nodes_bold_and_italic_and_code_and_image_and_link(self):
        text = "This is **bold text** with some _italic words_ in it, and a `code block` too, and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(" with some ", TextType.TEXT),
                TextNode("italic words", TextType.ITALIC),
                TextNode(" in it, and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" too, and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            text_to_text_nodes(text),
        )

    def test_extract_title(self):
        markdown = "# Tolkien Fan Club"

        self.assertEqual("Tolkien Fan Club", extract_title(markdown))

    def test_extract_title_from_multi_line(self):
        markdown = """
# Tolkien Fan Club

Other stuff in the markdown
"""

        self.assertEqual("Tolkien Fan Club", extract_title(markdown))