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
