from blocks import BlockType, block_to_block_type, markdown_to_blocks
from extract_markdown import text_to_text_nodes
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match (block_type):
            case BlockType.PARAGRAPH:
                nodes.append(get_block_parent_node(block, "p"))
            case BlockType.HEADING:
                heading_count = block.count("#")
                text = block.replace(f"{heading_count * "#"} ", "")

                nodes.append(get_block_parent_node(text, f"h{heading_count}"))
            case BlockType.CODE:
                nodes.append(get_code_block_node(block))
            case BlockType.UNORDERED_LIST:
                nodes.append(get_unordered_list_block_node(block))
            case BlockType.ORDERED_LIST:
                nodes.append(get_ordered_list_block_node(block))
            case _:
                return ValueError(f"->{block_type}<- unsupported block type")

    return ParentNode("div", nodes)


def get_block_parent_node(text, tag):
    text_nodes = text_to_text_nodes(text)
    html_nodes = list(map(lambda node: text_node_to_html_node(node), text_nodes))

    return ParentNode(tag, html_nodes)


def get_code_block_node(text):
    return ParentNode(
        "pre",
        [
            text_node_to_html_node(
                TextNode(text.split("```")[1].lstrip(), TextType.CODE)
            )
        ],
    )


def get_unordered_list_block_node(text):
    return ParentNode(
        "ul",
        list(
            map(
                lambda item: get_block_parent_node(item.replace("- ", ""), "li"),
                text.split("\n"),
            )
        ),
    )


def get_ordered_list_block_node(text):
    return ParentNode(
        "ol",
        list(
            map(
                lambda item: get_block_parent_node(item[3:], "li"),
                text.split("\n"),
            )
        ),
    )
