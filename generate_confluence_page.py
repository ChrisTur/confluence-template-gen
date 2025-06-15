"""
Confluence Template Generator

Usage:
  generate_confluence_page.py --template=<name> [--config=<file>]
  generate_confluence_page.py (-h | --help)

Options:
  -t --template=<name>   Template key to generate (e.g., incident_report)
  -c --config=<file>     YAML config file path [default: config.yaml]
  -h --help              Show this help message
"""

import yaml
import requests
import sys
from docopt import docopt
from jinja2 import Template
from requests.auth import HTTPBasicAuth


def load_config(path):
    try:
        with open(path, "r") as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f"❌ Failed to load config file: {e}")
        sys.exit(1)


def validate_config(config):
    confluence_cfg = config.get("confluence", {})
    placeholders = ["your-domain", "your.email@company.com", "your_api_token"]

    for key in ["base_url", "username", "api_token"]:
        value = confluence_cfg.get(key, "")
        if any(ph in value for ph in placeholders):
            print(f"⚠️  WARNING: Config key '{key}' contains a placeholder value.")
            print("Please update your config.yaml with real Confluence credentials.\n")
            break


def render_template(template_str, context):
    try:
        return Template(template_str).render(**context)
    except Exception as e:
        print(f"❌ Template rendering failed: {e}")
        sys.exit(1)


def post_to_confluence(base_url, username, api_token, space_key, title, content, parent_id=None):
    url = f"{base_url}/rest/api/content"
    headers = {"Content-Type": "application/json"}
    body = {
        "type": "page",
        "title": title,
        "space": {"key": space_key},
        "body": {
            "wiki": {
                "value": content,
                "representation": "wiki"
            }
        }
    }

    if parent_id:
        body["ancestors"] = [{"id": parent_id}]

    try:
        response = requests.post(
            url,
            auth=HTTPBasicAuth(username, api_token),
            headers=headers,
            json=body
        )
        if response.status_code not in (200, 201):
            print(f"❌ Failed to post page. Status: {response.status_code}")
            print("Response:", response.text)
            sys.exit(1)
        return response.status_code, response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Confluence API call failed: {e}")
        sys.exit(1)


def main():
    args = docopt(__doc__)
    template_key = args["--template"]
    config_path = args["--config"]

    config = load_config(config_path)
    validate_config(config)

    templates = config.get("templates", {})
    if template_key not in templates:
        print(f"❌ Template '{template_key}' not found in config.")
        print("Available templates:")
        for key in templates:
            print(f" - {key}")
        sys.exit(1)

    template_block = templates[template_key]
    template_str = template_block.get("template", "")
    context = template_block.get("context", {})
    parent_page_id = template_block.get("parent_page_id")

    rendered = render_template(template_str, context)
    title = context.get("title", template_key)

    conf = config["confluence"]
    status_code, result = post_to_confluence(
        base_url=conf["base_url"],
        username=conf["username"],
        api_token=conf["api_token"],
        space_key=conf["space_key"],
        title=title,
        content=rendered,
        parent_id=parent_page_id
    )

    print("✅ Page posted successfully!")
    print(f"Title: {result.get('title')}")
    print(f"ID: {result.get('id')}")
    print(f"URL: {conf['base_url']}/pages/viewpage.action?pageId={result.get('id')}")


if __name__ == "__main__":
    main()