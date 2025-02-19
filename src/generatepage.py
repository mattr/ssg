import os

from extracttitle import extract_title
from markdowntohtmlnode import markdown_to_html_node


def generate_page(from_path, template_path, to_path):
    if not os.path.exists(to_path):
        os.makedirs(to_path)

    with open(from_path, "r") as source:
        with open(template_path, "r") as template:
            with open(to_path, "w") as target:
                markdown = source.read()
                title = extract_title(markdown)
                content = markdown_to_html_node(markdown).to_html()

                html = template.read()
                html = html.replace("{{ Title }}", title)
                html = html.replace("{{ Content }}", content)
                target.write(html)
