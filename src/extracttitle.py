import re

def extract_title(text):
    lines = text.splitlines()
    for line in lines:
        heading = re.match("^# (.*?)$", line)
        if heading:
            return heading.group(1).strip()
    raise Exception("Title not found")