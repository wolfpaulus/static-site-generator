# Static Web Site Generator
__"A Journey from WordPress to Markdown and Jinja"__

### Status ..
![License](https://img.shields.io/badge/License-MIT-green.svg)
![up badge](https://img.shields.io/website-up-down-green-red/http/webgenerator.pages.dev.svg)

### Abstract
Embark on a journey transitioning from a heavy CMS to a streamlined static site generator using Markdown and Jinja. This guide navigates the complexities of CMS, outlining benefits and drawbacks, and then transitions to the simplicity and efficiency of static site generation. By leveraging Markdown for content creation and Jinja for templating, this approach reduces overhead, improves site speed, and enhances customization. 

#### What you will learn
- Strengths and limitations of using a CMS like WordPress for web development
- Benefits of transitioning to static site generation for simpler content management
- How to write and manage content in Markdown
- Techniques for storing and using metadata with JSON
- Utilizing Jinja for powerful and flexible templating
- Steps to set up a local development environment for previewing changes
- Methods for converting Markdown content to HTML
- Tips for rendering source code beautifully within posts
- Workflow automation using GitHub for site rebuilding and republishing
- Deploying a fast, cost-effective static site using Cloudflare Pages

### Big Idea

The main idea is to publish markdown content in HTML, using Jinja Templates.  
[Github Repository](https://github.com/wolfpaulus/static-site-generator/) | [Posts in Markdown](https://github.com/wolfpaulus/static-site-generator/tree/main/posts) | [Demo Website](https://webgenerator.pages.dev)


## 1. WordPress

A long time ago, I manually coded my website in HTML, CSS, and JavaScript. Then, about 10 years ago, I started using [WordPress](https://wordpress.com/learn/), which allowed me to focus more on the content.

Even today, WordPress is a popular content management system (CMS) that uses PHP and MySQL to create and manage websites and blogs. Its core components are [PHP](https://www.w3schools.com/php/default.asp) and [SQL](https://www.w3schools.com/sql/default.asp):

### PHP
- **Purpose**: The scripting language used to build and run WordPress.
- **Functionality**: PHP files generate [HTML](https://www.w3schools.com/html/default.asp) __dynamically at runtime__, handling everything from displaying content to processing form data.
- **Customization**: Users can write custom PHP code to create themes and plugins, extending WordPress' functionality.

### Themes and Plugins
- **Themes**: PHP templates control the layout and design of a site. Custom themes can be created using PHP, HTML, and CSS.
- **Plugins**: Extend WordPress functionality. Plugins often contain PHP scripts that interact with the database using SQL queries.

### MySQL
- **Purpose**: The relational database management system is used to store and retrieve site data.
- **Functionality**: WordPress uses SQL queries to interact with the MySQL database, managing content, user information, and site settings.
- **Customization**: Users can write custom SQL queries for advanced data manipulation and retrieval.

## WordPress' Key Processes
### Content Management
- **Posts and Pages**: Stored in MySQL tables. PHP scripts retrieve and display this content on the website.
- **Media Library**: Images and other media files are referenced in the database and managed through PHP functions.

### Dynamic Content
- **PHP and SQL**: PHP scripts use SQL queries to fetch data from the MySQL database and display it to users.
- **Forms and Submissions**: PHP handles form submissions, interacting with the database to store or update information.

## Considerations Using WordPress
Despite the following drawbacks, WordPress remains a popular choice due to its flexibility and extensive ecosystem.

### Security Vulnerabilities
- Frequent target for hackers.
- Vulnerabilities in third-party plugins and themes.

### Performance Issues
- Can be slow if not optimized.
- May require higher server resources.

### Complexity
- Steep learning curve for beginners.
- Requires ongoing maintenance and updates.

### Compatibility Issues
- Plugin conflicts can cause functionality problems.
- Updates can break existing features.

### Customization Limitations
- Extensive customization needs coding skills.
- Design constraints without custom development.

### SEO Challenges
- Often relies on plugins for effective SEO.
- Improper settings can lead to duplicate content issues.

### Cost Considerations
- Premium themes and plugins can be expensive.
 
## 2. Static Site Generation

I'm maintaining two websites that I update maybe once a week. There are hardly any interactive parts, and all visitors get the same content. Considering this, the aforementioned process seems like overkill. So, __what would a reasonable workflow look like that I would actually enjoy and would encourage me to create more and better content?__

1. Write content in Markdown. Here is its [Basic Syntax](https://www.markdownguide.org/basic-syntax/) and a [tutorial](https://www.markdowntutorial.com).
2. Store content metadata (e.g., a post's category, whether it's featured or not, dates, etc.) in a single [JSON](https://www.w3schools.com/js/js_json_intro.asp) file.
3. Ensure the "presentation layer" is not limited by a small selection of templates.
4. Preview the website locally before pushing changes to the remote GitHub repository.
5. Render source code beautifully since I often write about computer programming.
6. Store the content in a GitHub repository rather than a SQL database.
7. Trigger a rebuild/republish of the website upon changes to the GitHub repository.
8. Ensure the public website loads fast while keeping hosting costs low.

## Popular Frameworks

There are several popular frameworks for building static websites, such as:

1. [Hugo](https://gohugo.io): A static site generator written in Go, optimized for speed, easy use, and configurability. It takes a directory with content and templates and renders them into a full HTML website.
2. [Gridsome](https://gridsome.org): A scalable generator that uses [Vue.js](https://vuejs.org) to help you create static pages.
3. [Gatsby](https://www.gatsbyjs.com): Great for building blazing-fast, modern apps and websites with [React](https://react.dev).

However, each comes with its own considerations:

### Hugo
- **Steeper Learning Curve**: Hugo has a steeper learning curve compared to some other static site generators, particularly due to its templating language and configuration options.
- **Complex Configuration**: Its configuration can become quite complex, especially for larger sites with many custom layouts and features.

### Gridsome
- **Vue-Specific**: Gridsome is tightly coupled with [Vue.js](https://vuejs.org), so it's not the best choice for developers who prefer or are more experienced with React or other frameworks.

### Gatsby
- **Complex Setup**: The setup and configuration of Gatsby can be complex and overwhelming for beginners, especially with its reliance on [React](https://react.dev) and [GraphQL](https://graphql.org).
- **Dependency Management**: Gatsby has many dependencies, and keeping them all updated and compatible can be a challenge.
- **High Resource Usage**: Developing with Gatsby can be resource-intensive, requiring more powerful hardware to run efficiently.

## Content Creation

Before starting to code, let's have some fun creating content for the website.  
Let's ask ChatGPT to create some cool stories (including summaries and cover images) for the blog. I used the following three prompts:

1. "Hey storyteller, please write 5 short stories about Python programming. Written in Markdown code that I can download."
2. "Can you write a one-sentence summary for each story?"
3. "Can you create an engaging cover image for each story that makes you really want to read the story?"

Of course, you can reuse the [stories and images](https://github.com/wolfpaulus/static-site-generator/) ChatGPT created for me, but it is important to arranged the content in a systematic way:

- Start a new Python project in VSCode and create a virtual environment.
- Create a `posts` directory and copy the 5 _Markdown_ files into it.
- I named those files: `triumph.md`, `dilemma.md`, `wizard.md`, `dream.md`, and `discovery.md`.
- Create an `assets/images` directory and copy the generated images into it.
- Create a `context.json` file with this initial content:
```json
{ 
  "content": {
    "posts" : []
  }
}
```
- Finally, create a dictionary like the one below for every story, and put it into the content's __posts__ list: 
```json
{
  "name": "triumph",
  "cover": "triumph.png",
  "title": "The Beginner's Triumph",
  "summary": "Emma embarks on her programming journey with Python and triumphs over her first coding challenges.",
  "cat": "software",
  "featured": true
}
```

# 3. DIY Static Site Generation

Choosing a static site generator can feel like picking a CMS a decade ago, with options like WordPress, Joomla, and Drupal. But the eight workflow requirements outlined earlier seem straightforward enough to tackle them one by one.

## 1. Writing content in Markdown

Writing content in Markdown is easy. Check out this post on [How to Use Markdown in VSCode](https://www.freecodecamp.org/news/how-to-use-markdown-in-vscode/). Create a new folder (e.g., `posts`) and start putting Markdown files into it.

## 2. Storing content metadata in a single JSON file

Let's add some site metadata to a `context.json` file. E.g.:

```json
{
  "site_dir": "public",
  "templates_dir": "templates",
  "posts_dir": "posts",
  "static_dirs": ["assets"],
  "copyright_year": "2024",
  "title": "Static Web Site Generator Demo",
  "description": "This site was generated by jinja templates.",

  "content": {
    "posts": [
      {
        "name": "triumph",
        "cover": "triumph.png",
        "title": "The Beginner's Triumph.",
        "summary": "Emma embarks on her programming journey with Python and triumphs over her first coding challenges.",
        "cat": "software",
        "featured": true
      },
      {
        "name": "dilemma",
        "cover": "dilemma.png",
        "title": "The Debugger's Dilemma",
        "summary": "Liam, a seasoned developer, solves a persistent bug by taking a step back and rethinking his approach.",
        "cat": "software",
        "featured": false
      }
    ]
  }
}
```

## 3. Ensuring access to a large selection of site templates

There are many websites offering HTML site templates. Here are a few examples:

1. [HTML5up](https://html5up.net) - Free, responsive HTML5 site templates.
1. [Lexington Themes](https://lexingtonthemes.com) - Free and premium multipage themes and UI kits.
1. [Code Stitch](https://www.codestitch.app) - HTML and CSS Template Library.
1. [Envato](https://themeforest.net/category/site-templates) - HTML Templates and Website Templates.
1. [Pure CSS](https://purecss.io) - Small, responsive CSS modules for every web project.
1. [W3.CSS Templates](https://www.w3schools.com/w3css/w3css_templates.asp) - Simple responsive W3.CSS website templates.


### Big Idea

The main idea is to modify an existing site template by replacing some HTML with Jinja code, essentially turning HTML files into Jinja files.

[Jinja](https://jinja.palletsprojects.com) is a templating language for Python developers. A template contains variables that are replaced by values when the template is rendered. Special placeholders in the template allow writing code similar to Python syntax. For example:

#### Delimiters

- {%....%} are for statements
- {{....}} are expressions used to print to template output

Here’s a simple example. After installing Jinja2 with `pip install jinja2`, the following Python program:

```python
from jinja2 import Template
from json import load

jinja_template = '''
<!DOCTYPE html>
<html>
<head>
 <title>{{ title }}</title>
</head>
<body>
  <ol>
    {% for post in content.posts if post.cat == "software" %}
      <li>{{ post.title }}</li>
    {% endfor %}
  </ol>
</body>
</html>
'''
with open('context.json') as json_file:
    context = load(json_file)
html = Template(jinja_template).render(context)
print(html)
```

prints this output:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Static Web Site Generator Demo</title>
  </head>
  <body>
    <ol>
      <li>The Beginner's Triumph.</li>
      <li>The Debugger's Dilemma</li>
    </ol>
  </body>
</html>
```

`jinja_template` is a muliline string, storing HTML code with some jinja expressions and statements. The `context` variable provides access to a dictionary, containing everything we previously put into the _context.json_ file. A Template is instantiated from the jinja_template string, and the render method is called with the context as an argument, providing access to the context dictionary.

#### Getting started with Jinja

Here is a link to the [Jinja Project](https://jinja.palletsprojects.com/en/3.1.x/) and a good [primer](https://realpython.com/primer-on-jinja-templating/)

Moving closer to production code, a `jinja_to_html` method might look something like this:

```python
from pathlib import Path
from json import load
from jinja2 import Template


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
                            extensions=("jinja2.ext.do")  # allow do sttmnts
                            ).render(self.context)
            trg_path = Path.cwd().joinpath(self.context.get("site_dir"), html_file)
            trg_path.parent.mkdir(parents=True, exist_ok=True)
            with trg_path.open(mode="w", encoding="utf-8") as trg:
                trg.write(code)
                print(f"Generated: {trg_path}")
```

### HTML to Jinja

I will admit it ain't pretty, but for demonstration purposes, the [W3.CSS Blog Template]( https://www.w3schools.com/w3css/tryw3css_templates_blog.htm) is rich enough to show how an HTML site template can be converted into Jinja templates. Save the HTML code as templates/index.jinja and replace some of the HTML with Jinja.

For instance, change the header to this:

```jinja
<!-- Header -->
<header class="w3-container w3-center w3-padding-32">
  <h1><b>{{ title }}</b></h1>
  <p>{{ description }}></p>
</header>
```

Replace the three Blog entry divs with this Jinja for-loop:

```jinja
<!-- Blog entries -->
<div class="w3-col l8 s12">
  {% for post in content.posts if post.featured %}
  <!-- Blog entry -->
  <div class="w3-card-4 w3-margin w3-white">
    {% if post.cover %}
    <img src="/assets/images/{{ post.cover }}" style="width:50%">
    {% endif %}
    <div class="w3-container">
      <h3><b>{{ post.title }}</b></h3>
      <h5>{{ post.cove }}</h5>
    </div>
    <div class="w3-container">
      <p>{{ post.summary }}</p>
      <div class="w3-row">
        <div class="w3-col m8 s12">
          <p><button class="w3-button w3-padding-large w3-white w3-border"
              onclick="location.href='/{{ post.name }}.html'" type="button"><b>READ MORE »</b></button></p>
        </div>
      </div>
    </div>
  </div>
  {% endfor %}
  <!-- END BLOG ENTRIES -->
</div>
```

Optionally, add three more key-value pairs (author_name, author_about, author_avatar) to the context.json file and modify the _About Card_ to this:

```jinja
<!-- About Card -->
<div class="w3-card w3-margin w3-margin-top">
  <img src="/assets/images/{{ author_avatar }}" style="width:50%">
  <div class="w3-container w3-white">
    <h4><b>{{ author_name }}</b></h4>
    <p>{{ author_about }}</p>
  </div>
</div>
<hr>
```

Replace the list of _featured posts_ with this Jinja loop:

```jinja
<!-- Posts -->
<div class="w3-card w3-margin">
  <div class="w3-container w3-padding">
    <h4>Popular Posts</h4>
  </div>
  <ul class="w3-ul w3-hoverable w3-white">
    {% for post in content.posts if not post.featured %}
    <li class="w3-padding-16" onclick="location.href='/{{ post.name }}.html'">
      {% if post.cover %}
      <img src="/assets/images/{{ post.cover }}" alt="Image" class="w3-left w3-margin-right" style="width:50px">
      {% endif %}
      <span class="w3-large">{{ post.title }}</span><br>
      <span>{{ post.summary }}</span>
    </li>
    {% endfor %}
  </ul>
</div>
```

You might be tempted, running this:

```python
Site_Generator("context.json").jinja_to_html("index.jinja", "index.html")
```

However, there is still a little bit of setup work required. Let's add a `generate_site` method to the `Site_Generator` class and run that instead.

```python
def generate_site(self):
    """Generate the static website.
    1. Remove the site_dir and re-create it
    2. Copy the static directories
    3. Render the index page
    """
    site_dir = Path.cwd().joinpath(self.context.get("site_dir"))
    rmtree(site_dir, ignore_errors=True)
    site_dir.mkdir()
    for dir in self.context["static_dirs"]:
        copytree(dir, site_dir.joinpath(dir))
    self.jinja_to_html("index.jinja", "index.html")  # render index page
```

```python
if __name__ == "__main__":
    Site_Generator("context.json").generate_site()
```

## 4. Local Preview

To preview the just generated `index.html` file, install the [ritwickdey.liveserver](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) VSCode extension, to _"launch a development local Server with live reload feature for static & dynamic pages"_.  
I also added this key/value pair to the ./.vscode/settings.json file: `"liveServer.settings.root": "/public"`, which points the local webserver to the site's root directory. For starting the server look at the bottom/right in VSCode.


Notice that this page contains only metadata, information stored in the _context.json_ file and there is still some work ahead of us. The markdown documents still need to be converted into HTML and for that we need another jinja template.  
Once again, I used with the _index.html_ file as a starting point and saved it as templates/post.jinja. At its core, it looks something like this now:

```jinja
<!-- Header -->
<header class="w3-container w3-center w3-padding-32">
  <h1><b>{{ post.title }}</b></h1>
  <p>{{ post.summary }}</p>
</header>

<!-- Grid -->
<div class="w3-row">

  <!-- Post -->
  <div class="w3-card-4 w3-margin w3-white">
     {% if post.cover %}
        <img src="/assets/images/{{ post.cover }}" style="width:100%">
     {% endif %}

    <div class="w3-container">
      {{ post.text }}
    </div>
  </div>
  <hr>
  <!-- END Post -->
</div>
```

### Markdown to html
Converting Markdown to HTML is straightforward, after pip installing the markdown module:
```shell
pip install markdown
```

```python 
def md_to_html(self, file_name: str) -> str:
    """Convert a markdown file to html.
    Args: file_name: name of the markdown file
    Returns: html: the html content
    """
    with self.posts.joinpath(file_name).open(encoding="utf-8") as file:
        return markdown(file.read().strip(), extensions=['fenced_code', 'codehilite'])

```

## 5. Rendering Source Code Beautifully

The Markdown module has a [Code Hilite](https://python-markdown.github.io/extensions/code_hilite/) extension, but it requires `Pygments`, a generic syntax highlighter, which is unfortunately not installed as a dependency, but is just one more pip install away.  
We also need a cool colortheme, which can be previewed [here](https://pygments.org/styles/). I liked `dracula` and therefore ran these commands in VSCode's terminal:

```shell
pip install Pygments
mkdir ./assets/css
pygmentize -S dracula -f html -a .codehilite > ./assets/css/dracula.css
```

A link to the newly created dracula.css file still needs to be put into the `post.jinja`, which at the very top, now looks like this:

```jinja
<!DOCTYPE html>
<html>
<head>
  <title>{{post.title}}</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/assets/css/dracula.css" />
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
  <style>
    body,h1,h2,h3,h4,h5 {font-family: "Raleway", sans-serif}
  </style>
</head>
```

To render all markdown posts, the Site_Generator's `generate_site` methods needs to be expanded, like shown below:
```python
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
```        
After re-running `Site_Generator("context.json").generate_site()`, html pages for all posts were generated and code snippets within those pages look beautiful.

## 6. Storing the content in a GitHub repository rather than a SQL database

I created a new repo on <https://github.com> and named it __static-site-generator__. Locally, I ran these commands inside VSCode's terminal:

```shell
git init
git branch -M main
git remote add origin git@github.com:wolfpaulus/static-site-generator.git
```

Not everything needs to be tracked in the repo. While the ./public folder contains the generated html files, it does not belong into the repo since the build process will generate those files. Therefore, I added this to the ./.gitignore file.

```text
.DS_Store
.venv/
public/
__pycache__/
*.pyc
```

## 7. Triggering a rebuild/republish of the website upon changes to the GitHub repository

The idea is that everytime a repo change is detected, `Site_Generator("context.json").generate_site()` is run. To prepare for that, I added this at the bottom of the `main.py` script:

```python
if __name__ == "__main__":
    Site_Generator("context.json").generate_site()
```

Running the main.py script remotely, requires a `requirements.txt` file that contains all the 3rd party modules that were _pip installed_ along the way. E.g.:

```text
jinja2
markdown
Pygments
```

Now it's time to add everything to git, commit, and push.
It's all in place now to build and host the site at [Cloudflare](https://www.cloudflare.com)

## 8. Fast, Cost-Effective Hosting with Cloudflare Pages

Deploy your site using Cloudflare Pages for fast and cost-effective hosting. Follow the instructions on [Cloudflare Pages](https://developers.cloudflare.com/pages/) to connect your GitHub repository and deploy the site.

Specifically, here is a link to Cloudflare's [Pages Git integration guide](https://developers.cloudflare.com/pages/get-started/git-integration/). After logging in to Cloudflare and navigating to _"Workers & Pages"_, I did the following:

1. Click the __Create__ button
1. Click on the __Pages__ tab
1. Click the __Connect to Git__ button
1. Add/connect your GitHub account
1. Select the `static-site-generator` repo
1. Click the __Begin setup__ button.
  1. Enter a Project name: `webgenerator` (Note the url, e.g: _Your project will be deployed to webgenerator.pages.dev._)
  1. Enter the git branch: `main`
  1. Framwork preset: `None`
  1. Build command: `python3 main.py`
  1. Build output directory: `public`
1. Click the __Save and Deploy__ button.

Initially, it takes a few minutes for the new domain name to propagate. From now on, every change pushed to Github will result in a regeneration of the site. My site is up and running here now: [webgenerator.pages.dev](https://webgenerator.pages.dev)

### Cloudflare Pages
Cloudflare Pages is very cost-effective, and it's very easy to deploy code. A free account comes with the following limits:

#### Limits
- Up to 100 sites per account
- To more than 20,000 files
- Each file needs to be smaller than 25MB
- The optional _headers file can have a maximum of 100 rules.
- A build needs to complete within 20 minutes
- Up to 500 builds per month


## Summary
Transitioning from WordPress to a static site generator using Markdown and Jinja offers a lightweight, efficient, and customizable approach to content management. This guide provides a comprehensive workflow to write content in Markdown, manage metadata with JSON, and leverage Jinja for flexible templating. By setting up a local development environment, automating workflow with GitHub, and deploying via Cloudflare, you can achieve a fast, cost-effective, and streamlined static site that encourages better content creation and management.
