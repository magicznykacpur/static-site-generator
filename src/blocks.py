from enum import Enum


BlockType = Enum(
    "BlockType",
    ["PARAGRAPH", "HEADING", "CODE", "QUOTE", "UNORDERED_LIST", "ORDERED_LIST"],
)


def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    if all(list(map(lambda line: line.startswith(">"), block.split("\n")))):
        return BlockType.QUOTE
    
    if all(list(map(lambda line: line.startswith("- "), block.split("\n")))):
        return BlockType.UNORDERED_LIST
    
    if check_ordered_list_block_type(block):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def check_ordered_list_block_type(block):
    lines = block.split("\n")

    if not lines[0].startswith("1. "):
        return False
    
    checks = []
    for i in range(len(lines)):
        checks.append(lines[i].startswith(f"{i + 1}. "))
    
    return all(checks)


def markdown_to_blocks(markdown):
    blocks = list(map(lambda block: block.strip(), markdown.split("\n\n")))
    return list(filter(None, blocks))
