import os

from extracttitle import extract_title
from markdowntohtmlnode import markdown_to_html_node


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def generate_page(from_path, template_path, to_path, base_path):
    path_parts = to_path.split("/")[0:-1]
    if len(path_parts) > 0:
        for i in range(len(path_parts)):
            path = "/".join(path_parts[0:i + 1])
            print(f"making the path: {path}")
            create_dir(path)

    with open(from_path, "r") as source:
        with open(template_path, "r") as template:
            with open(to_path, "w") as target:
                markdown = source.read()
                title = extract_title(markdown)
                content = markdown_to_html_node(markdown).to_html()

                html = template.read()
                html = html.replace("{{ Title }}", title)
                html = html.replace("{{ Content }}", content)
                html = html.replace('href="/', f'href="{base_path}')
                html = html.replace('src="/', f'src="{base_path}')
                target.write(html)


def generate_pages(from_path, template_path, to_path, base_path = "/"):
    for item in os.listdir(from_path):
        current_path = f"{from_path}/{item}"
        if os.path.isfile(current_path):
            if item.endswith(".md"):
                write_path = f"{to_path}/{item.replace(".md", ".html")}"
                generate_page(current_path, template_path, write_path, base_path)
        else:
            generate_pages(current_path, template_path, f"{to_path}/{item}", base_path)
