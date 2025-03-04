import unittest

from blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestBlocks(unittest.TestCase):

    def test_markdown_to_blocks_one_block(self):
        markdown = "# This is a heading"

        self.assertListEqual(["# This is a heading"], markdown_to_blocks(markdown))

    def test_markdown_to_blocks_two_blocks(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
"""

        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            ],
            markdown_to_blocks(markdown),
        )

    def test_markdown_to_blocks_three_blocks(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- List item
- List item
- List item
"""

        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- List item\n- List item\n- List item",
            ],
            markdown_to_blocks(markdown),
        )

    def test_block_to_heading_block_type(self):
        block = "# Heading"

        self.assertEqual(BlockType.HEADING, block_to_block_type(block))
    
    def test_block_to_double_heading_block_type(self):
        block = "## Heading"

        self.assertEqual(BlockType.HEADING, block_to_block_type(block))
    
    def test_block_to_triple_heading_block_type(self):
        block = "### Heading"

        self.assertEqual(BlockType.HEADING, block_to_block_type(block))
    
    def test_block_to_quadruple_heading_block_type(self):
        block = "#### Heading"

        self.assertEqual(BlockType.HEADING, block_to_block_type(block))
    
    def test_block_to_quintuple_heading_block_type(self):
        block = "##### Heading"

        self.assertEqual(BlockType.HEADING, block_to_block_type(block))
    
    def test_block_to_sextuple_heading_block_type(self):
        block = "###### Heading"

        self.assertEqual(BlockType.HEADING, block_to_block_type(block))
    
    def test_block_to_invalid_heading_block_type(self):
        block = "######## Heading"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_block_to_code_block_type(self):
        block = "``` code block ```"

        self.assertEqual(BlockType.CODE, block_to_block_type(block))

    def test_block_to_invalid_code_block_type(self):
        block = "--``` code block ```"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_block_to_quote_block_type(self):
        block = ">quote block"

        self.assertEqual(BlockType.QUOTE, block_to_block_type(block))

    def test_block_to_quote_block_type(self):
        block = ">quote block\n>quote block\n>quote block"

        self.assertEqual(BlockType.QUOTE, block_to_block_type(block))

    def test_block_to_invalid_quote_block_type(self):
        block = "<quote block\n>quote block\n>quote block"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_block_to_unordered_list_block_type(self):
        block = "- list item"

        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(block))

    def test_block_to_unordered_list_block_type(self):
        block = "- list item\n- list item\n- list item"

        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(block))

    def test_block_to_invalid_unordered_list_block_type(self):
        block = " list item\n- list item\n- list item"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_block_to_ordered_list_block_type(self):
        block = "1. list item\n2. list item\n3. list item"

        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(block))

    def test_block_to_invalid_ordered_list_block_type(self):
        block = "2. list item\n2. list item\n3. list item"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_block_to_invalid_ordered_list_block_type(self):
        block = "2. list item\n3. list item\n3. list item"

        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))