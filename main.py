"""
This script generates a static website from markdown files and jinja2 templates.
The context.json file contains the configuration and data for the website.
The templates_dir contains the jinja2 templates.
The posts_dir contains the markdown files.
The site_dir is the output directory.
The static_dirs contain static files to be copied to the site_dir.
Author: Wolf Paulus
"""
from pathlib import Path
from shutil import rmtree, copytree
from json import load
from jinja2 import Template
from markdown import markdown


class Site_Generator:
    """ Generate a static website from markdown files and jinja2 templates. """

    def __init__(self, context_file: str):
        """Initialize the site generator
        Args: context_file: name of the context file
        """
        with open(context_file, encoding="utf-8") as json_file:
            self.context = load(json_file)
            self.templates = Path.cwd().joinpath(self.context.get("templates_dir"))
            self.posts = Path.cwd().joinpath(self.context.get("posts_dir"))

    def jinja_to_html(self, jinja_file: str, html_file: str) -> None:
        """ Render a jinja template 
            Args:   jinja_file: name of the template file
                    html_file: name of the target file
        """
        with self.templates.joinpath(jinja_file).open(encoding="utf-8") as src:
            code = Template(src.read(),
                            trim_blocks=True,   # remove whitespace
                            lstrip_blocks=True,  # remove leading whitespace
                            extensions=["jinja2.ext.do"],  # allow do sttmnts
                            ).render(self.context)
            trg_path = Path.cwd().joinpath(self.context.get("site_dir"), html_file)
            trg_path.parent.mkdir(parents=True, exist_ok=True)
            with trg_path.open(mode="w", encoding="utf-8") as trg:
                trg.write(code)
                print(f"Generated: {trg_path}")

    def md_to_html(self, file_name: str) -> str:
        """Convert a markdown file to html.
        Args: file_name: name of the markdown file
        Returns: html: the html content
        """
        with self.posts.joinpath(file_name).open(encoding="utf-8") as file:
            return markdown(file.read().strip(), extensions=['fenced_code', 'codehilite'])

    def generate_site(self):
        """Generate the static website.
        1. Remove the site_dir and re-create it
        2. Copy the static directories
        3. Render the index page
        4. Render the posts
        """
        site_dir = Path.cwd().joinpath(self.context.get("site_dir"))
        rmtree(site_dir, ignore_errors=True)
        site_dir.mkdir()
        for dir in self.context["static_dirs"]:
            copytree(dir, site_dir.joinpath(dir))
        self.jinja_to_html("index.jinja", "index.html")  # render index page
        # render posts
        posts = self.context["content"]["posts"]
        k = len(posts)
        for i, post in enumerate(posts):
            post["text"] = self.md_to_html(f"{post['name']}.md")
            post["prev"] = posts[i - 1]["name"] if i > 0 else None
            post["next"] = posts[i + 1]["name"] if i < k-1 else None
            self.context["post"] = post
            self.jinja_to_html("post.jinja", f"{post['name']}.html")
        self.context["post"] = None


if __name__ == "__main__":
    Site_Generator("context.json").generate_site()