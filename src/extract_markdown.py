import re
from textnode import TextNode, TextType

accepted_delimiters = ["**", "_", "`"]


def text_to_text_nodes(text):
    big_node = [TextNode(text, TextType.TEXT)]

    big_node = split_nodes_delimiter(big_node, accepted_delimiters[0], TextType.BOLD)
    big_node = split_nodes_delimiter(big_node, accepted_delimiters[1], TextType.ITALIC)
    big_node = split_nodes_delimiter(big_node, accepted_delimiters[2], TextType.CODE)
    big_node = split_nodes_image(big_node)
    big_node = split_nodes_link(big_node)

    return big_node


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    if delimiter not in accepted_delimiters:
        raise Exception(f"->{delimiter}<- not in accepted delimiters")

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            chunks = node.text.split(delimiter)

            inner_nodes = []

            for i in range(len(chunks)):
                if i % 2 != 0:
                    inner_nodes.append(TextNode(chunks[i], text_type))
                elif i % 2 == 0 and len(chunks[i]) > 0:
                    inner_nodes.append(TextNode(chunks[i], TextType.TEXT))
                else:
                    continue

            new_nodes.extend(inner_nodes)
        else:
            new_nodes.append(node)

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        matches = extract_markdown_images(node.text)

        if len(matches) == 0:
            new_nodes.append(node)
        elif len(matches) == 1:
            match = matches[0]
            chunks = node.text.split(f"![{match[0]}]({match[1]})")

            new_nodes.extend(split_by_one_match(match, chunks, TextType.IMAGE))
        else:
            new_nodes.extend(
                split_by_multiple_matches(matches, node.text, TextType.IMAGE)
            )

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        matches = extract_markdown_links(node.text)

        if len(matches) == 0:
            new_nodes.append(node)
        elif len(matches) == 1:
            match = matches[0]
            chunks = node.text.split(f"[{match[0]}]({match[1]})")

            new_nodes.extend(split_by_one_match(match, chunks, TextType.LINK))
        else:
            new_nodes.extend(
                split_by_multiple_matches(matches, node.text, TextType.LINK)
            )

    return new_nodes


def split_by_multiple_matches(matches, text, text_type):
    nodes = []

    for i in range(len(matches)):
        splitter = ""
        if text_type == TextType.LINK:
            splitter = f"[{matches[i][0]}]({matches[i][1]})"
        else:
            splitter = f"![{matches[i][0]}]({matches[i][1]})"

        chunks = text.split(splitter)
        nodes.extend(
            [
                TextNode(chunks[0], TextType.TEXT),
                TextNode(matches[i][0], text_type, matches[i][1]),
            ]
        )

        text = text.split(f"{chunks[0]}{splitter}")[1]
        if i == len(matches) - 1 and len(text) > 0:
            nodes.append(TextNode(text, TextType.TEXT))

    return nodes


def split_by_one_match(match, chunks, text_type):
    nodes = []

    if len(chunks[0]) == 0 and len(chunks[1]) == 0:
        nodes.append(TextNode(match[0], text_type, match[1]))
    elif len(chunks[0]) > 0 and len(chunks[1]) == 0:
        nodes.extend(
            [
                TextNode(chunks[0], TextType.TEXT),
                TextNode(match[0], text_type, match[1]),
            ]
        )
    else:
        nodes.extend(
            [
                TextNode(chunks[0], TextType.TEXT),
                TextNode(match[0], text_type, match[1]),
                TextNode(chunks[1], TextType.TEXT),
            ]
        )

    return nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_title(markdown):
    return list(filter(None, markdown.split("\n")))[0].replace("# ", "")
