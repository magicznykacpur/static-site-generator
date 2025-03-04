import re
from textnode import TextNode, TextType

accepted_delimiters = ["**", "_", "`"]


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
        chunks = []

        if text_type == TextType.IMAGE:
            chunks = text.split(f"![{matches[i][0]}]({matches[i][1]})")
        else:
            chunks = text.split(f"[{matches[i][0]}]({matches[i][1]})")

        if len(chunks[0]) == 0:
            nodes.append(TextNode(matches[i][0], text_type, matches[i][1]))

        if len(chunks[0]) > 0 and i == 0:
            nodes.extend(
                [
                    TextNode(chunks[0], TextType.TEXT),
                    TextNode(matches[i][0], text_type, matches[i][1]),
                ]
            )

        if len(chunks[1]) == 0:
            nodes.append(TextNode(matches[i][0], text_type, matches[i][1]))
        else:
            remaining_splitter = ""
            in_between_splitter = ""

            if text_type == TextType.IMAGE:
                remaining_splitter = (
                    f"{nodes[i].text}![{matches[i][0]}]({matches[i][1]})"
                )
                in_between_splitter = f"![{matches[i + 1][0]}]({matches[i + 1][1]})"
            else:
                remaining_splitter = (
                    f"{nodes[i].text}[{matches[i][0]}]({matches[i][1]})"
                )
                in_between_splitter = f"[{matches[i + 1][0]}]({matches[i + 1][1]})"

            remaining = text.split(remaining_splitter)

            if len(remaining) == 1:
                continue

            in_between = remaining[1].split(in_between_splitter)

            nodes.append(
                TextNode(in_between[0], TextType.TEXT),
            )

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
