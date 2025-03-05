import os
import shutil

from extract_markdown import extract_markdown_links
from markdowntohtml import generate_page
from textnode import TextNode, TextType


def copy_static_content_recursive(from_path, to_path):
    if not os.path.exists(from_path):
        print(f"Cannot copy from {from_path}, directory doesn't exist...")
        return
    if not os.path.exists(to_path):
        print(f"Cannot copy to {to_path}, directory doesn't exist...")
        return

    to_dir_list = os.listdir(to_path)
    for item in to_dir_list:
        to_remove_path = f"{to_path}/{item}"
        if os.path.isfile(to_remove_path):
            os.remove(to_remove_path)
        else:
            shutil.rmtree(to_remove_path)

    dir_list = os.listdir(from_path)
    for item in dir_list:
        src_path = os.path.join(from_path, item)
        target_path = os.path.join(to_path, item)

        if os.path.isfile(src_path):
            print(f"copying from {src_path} to {target_path}")

            shutil.copy(src_path, os.path.join(to_path))
        else:
            print(f"creating {target_path}")

            os.mkdir(target_path)
            copy_static_content_recursive(src_path, target_path)


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        matches = extract_markdown_links(node.text)

        if len(matches) == 0:
            new_nodes.append(node)
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
        nodes.extend([TextNode(chunks[0], TextType.TEXT), TextNode(matches[i][0], text_type, matches[i][1])])

        text = text.split(f"{chunks[0]}{splitter}")[1]
        if i == len(matches) - 1 and len(text) > 0:
            nodes.append(TextNode(text, TextType.TEXT))

    return nodes


def main():
    copy_static_content_recursive("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
