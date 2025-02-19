import re

def test_heading(text):
    return re.match("\A#{1,6}\s.*", text) is not None

def test_code(text):
    return text.startswith("```") and text.endswith("```")

def test_quote(text):
    lines = text.split("\n")
    # got to be a better way
    for line in lines:
        if not line.startswith(">"):
            return False
    return True

def test_unordered_list(text):
    lines = text.split("\n")
    for line in lines:
        if not (line.startswith("* ") or line.startswith("- ")):
            return False
    return True

def test_ordered_list(text):
    lines = text.split("\n")
    for index, line in enumerate(lines):
        if not line.startswith(f"{index + 1}. "):
            return False
    return True

def block_to_block_type(block):
    if test_heading(block):
        return "heading"
    elif test_code(block):
        return "code"
    elif test_quote(block):
        return "quote"
    elif test_unordered_list(block):
        return "unordered_list"
    elif test_ordered_list(block):
        return "ordered_list"
    else:
        return "paragraph"

