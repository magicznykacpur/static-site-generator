from blocks import BlockType, block_to_block_type, markdown_to_blocks
from extract_markdown import extract_title, text_to_text_nodes
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")

    markdown = open(from_path).read()
    template = open(template_path).read()

    html = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    page = open(dest_path, "w")
    page.write(template)
    page.close()


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match (block_type):
            case BlockType.PARAGRAPH:
                nodes.append(get_block_parent_node(block, "p"))
            case BlockType.HEADING:
                nodes.append(get_heading_block_node(block))
            case BlockType.QUOTE:
                nodes.append(get_quote_block_node(block))
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


def get_heading_block_node(text):
    heading_count = text.count("#")
    text = text.replace(f"{heading_count * "#"} ", "")

    return get_block_parent_node(text, f"h{heading_count}")


def get_quote_block_node(text):
    lines = text.split("\n")
    lines = list(map(lambda line: line.replace("> ", ""), lines))

    return ParentNode(
        "blockquote",
        [text_node_to_html_node(TextNode("\n".join(lines), TextType.TEXT))],
    )


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
