import unittest

from markdowntohtml import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_single_paragraph_markdown(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here
"""

        self.assertEqual(
            "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_single_double_paragraph_markdown_with_link_and_image(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here and [to google](https://www.google.com)

This is _italic paragraph
text in a p
tag here and ![image](https://i.imgur/3Jqtuw.png)
"""
        self.assertEqual(
            '<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here and <a href="https://www.google.com">to google</a></p><p>This is italic paragraph\ntext in a p\ntag here and <img src="https://i.imgur/3Jqtuw.png" alt="image"></img></p></div>',
            markdown_to_html_node(markdown).to_html(),
        )

    def test_single_double_paragraph_markdown(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here

This is _italic_ paragraph
text in a p
tag here
"""

        self.assertEqual(
            "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is <i>italic</i> paragraph\ntext in a p\ntag here</p></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_single_triple_paragraph_markdown(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here

This is _italic_ paragraph
text in a p
tag here

This is `code` paragraph
text in a p
tag here
"""

        self.assertEqual(
            "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is <i>italic</i> paragraph\ntext in a p\ntag here</p><p>This is <code>code</code> paragraph\ntext in a p\ntag here</p></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_single_double_paragraph_with_different_nodes_markdown(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here

This is _italic_ and `code` paragraph
text in a p
tag here

"""
        self.assertEqual(
            "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is <i>italic</i> and <code>code</code> paragraph\ntext in a p\ntag here</p></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_single_heading_markdown(self):
        markdown = """
# Heading

This is **bolded** paragraph
text in a p
tag here

This is _italic_ and `code` paragraph
text in a p
tag here

"""
        self.assertEqual(
            "<div><h1>Heading</h1><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is <i>italic</i> and <code>code</code> paragraph\ntext in a p\ntag here</p></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_double_heading_markdown_with_some_bold_text(self):
        markdown = """
## Heading **bold** text

This is **bolded** paragraph
text in a p
tag here

This is _italic_ and `code` paragraph
text in a p
tag here

"""
        self.assertEqual(
            "<div><h2>Heading <b>bold</b> text</h2><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is <i>italic</i> and <code>code</code> paragraph\ntext in a p\ntag here</p></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_triple_heading_markdown_with_some_bold_and_italic_text(self):
        markdown = """
### Heading **bold** text and _italic_ text

This is **bolded** paragraph
text in a p
tag here

This is _italic_ and `code` paragraph
text in a p
tag here

"""
        self.assertEqual(
            "<div><h3>Heading <b>bold</b> text and <i>italic</i> text</h3><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is <i>italic</i> and <code>code</code> paragraph\ntext in a p\ntag here</p></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_quadruple_heading_markdown_with_some_bold_and_italic_text(self):
        markdown = """
#### Heading **bold** text and _italic_ text

This is **bolded** paragraph
text in a p
tag here

This is _italic_ and `code` paragraph
text in a p
tag here

"""
        self.assertEqual(
            "<div><h4>Heading <b>bold</b> text and <i>italic</i> text</h4><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is <i>italic</i> and <code>code</code> paragraph\ntext in a p\ntag here</p></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_quintuple_heading_markdown_with_some_bold_and_italic_text(self):
        markdown = """
##### Heading **bold** text and _italic_ text

This is **bolded** paragraph
text in a p
tag here

This is _italic_ and `code` paragraph
text in a p
tag here

"""
        self.assertEqual(
            "<div><h5>Heading <b>bold</b> text and <i>italic</i> text</h5><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is <i>italic</i> and <code>code</code> paragraph\ntext in a p\ntag here</p></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_sextuple_heading_markdown_with_some_bold_and_italic_text(self):
        markdown = """
###### Heading **bold** text and _italic_ text

This is **bolded** paragraph
text in a p
tag here

This is _italic_ and `code` paragraph
text in a p
tag here

"""
        self.assertEqual(
            "<div><h6>Heading <b>bold</b> text and <i>italic</i> text</h6><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is <i>italic</i> and <code>code</code> paragraph\ntext in a p\ntag here</p></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_should_be_paragraph_heading_markdown_with_some_bold_and_italic_text(self):
        markdown = """
####### Heading **bold** text and _italic_ text

This is **bolded** paragraph
text in a p
tag here

This is _italic_ and `code` paragraph
text in a p
tag here

"""
        self.assertEqual(
            "<div><p>####### Heading <b>bold</b> text and <i>italic</i> text</p><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is <i>italic</i> and <code>code</code> paragraph\ntext in a p\ntag here</p></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_codeblock(self):
        markdown = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        self.assertEqual(
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_unordered_list_block(self):
        markdown = """
- List item one
- List item two
- List item three
"""
        self.assertEqual(
            "<div><ul><li>List item one</li><li>List item two</li><li>List item three</li></ul></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_unordered_list_block_with_bold_and_italic(self):
        markdown = """
- `List` **item** _one_
- **List** _item_ `two`
- _List_ `item` **three**
"""
        self.assertEqual(
            "<div><ul><li><code>List</code> <b>item</b> <i>one</i></li><li><b>List</b> <i>item</i> <code>two</code></li><li><i>List</i> <code>item</code> <b>three</b></li></ul></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_unordered_list_block_with_bold_and_italic_and_image_and_link(self):
        markdown = """
- `List` **item** _one_ and an ![image](https://i.imgur.3JuqTl.png)
- **List** _item_ `two` and a [to google](https://www.google.com)
"""
        self.assertEqual(
            '<div><ul><li><code>List</code> <b>item</b> <i>one</i> and an <img src="https://i.imgur.3JuqTl.png" alt="image"></img></li><li><b>List</b> <i>item</i> <code>two</code> and a <a href="https://www.google.com">to google</a></li></ul></div>',
            markdown_to_html_node(markdown).to_html(),
        )

    def test_ordered_list_block(self):
        markdown = """
1. List item one
2. List item two
3. List item three
"""
        self.assertEqual(
            "<div><ol><li>List item one</li><li>List item two</li><li>List item three</li></ol></div>",
            markdown_to_html_node(markdown).to_html(),
        )

    def test_ordered_list_block_with_bold_and_italic_and_image_and_link(self):
        markdown = """
1. `List` **item** _one_ and an ![image](https://i.imgur.3JuqTl.png)
2. **List** _item_ `two` and a [to google](https://www.google.com)
"""
        self.assertEqual(
            '<div><ol><li><code>List</code> <b>item</b> <i>one</i> and an <img src="https://i.imgur.3JuqTl.png" alt="image"></img></li><li><b>List</b> <i>item</i> <code>two</code> and a <a href="https://www.google.com">to google</a></li></ol></div>',
            markdown_to_html_node(markdown).to_html(),
        )

    def test_ordered_list_block_with_bold_and_italic_and_image_and_link(self):
        markdown = """
1. `List` **item** _one_ and an ![image](https://i.imgur.3JuqTl.png)
2. **List** _item_ `two` and a [to google](https://www.google.com)
"""
        self.assertEqual(
            '<div><ol><li><code>List</code> <b>item</b> <i>one</i> and an <img src="https://i.imgur.3JuqTl.png" alt="image"></img></li><li><b>List</b> <i>item</i> <code>two</code> and a <a href="https://www.google.com">to google</a></li></ol></div>',
            markdown_to_html_node(markdown).to_html(),
        )
