# Confluence Template Generator

Generate and publish structured Confluence pages using YAML-based templates and a simple CLI powered by `docopt`.

This tool is great for SRE teams, release managers, and engineering orgs that want consistent, automatable documentation workflows.

---

## ✨ Features

- 🔧 Template-driven Confluence page creation
- 🧾 YAML-based configuration
- 🚀 Direct publishing via Confluence REST API
- 📚 Supports multiple templates (e.g. incident reports, runbooks, releases)
- ⚙️ CLI interface using `docopt`

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/ChrisTur/confluence-template-gen.git
cd confluence-template-generator
pip install -r requirements.txt
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

⚙️ Configuration
Copy the sample config and edit your credentials and templates:

```bash
Edit config.yaml to match your Confluence space and templates.
```

```yaml
confluence:
  base_url: "https://your-domain.atlassian.net/wiki"
  username: "your.email@company.com"
  api_token: "your_api_token"
  space_key: "SRE"

templates:
  incident_report:
    parent_page_id: "123456"
    template: |
      h1. Incident - {{ title }}
      ...
    context:
      title: "Placeholder Title"
      ...
Each template can have its own parent_page_id.
```
Usage:
```bash
python generate_confluence_page.py --template=incident_report
```

Optional:
``` bash
python generate_confluence_page.py --template=runbook --config=custom_config.yaml
```

✅ Safety Checks
The script warns you if config.yaml still contains placeholder values like your-domain or your_api_token.

🧠 Contributing
See CONTRIBUTING.md for details on how to contribute new templates or improvements.

📜 License
This project is licensed under the MIT License.

📣 Acknowledgments
docopt for CLI parsing

Jinja2 for template rendering

Atlassian Confluence REST API

```yaml
---
Let me know if you'd like it customized further with badges (build status, license, etc.) or if you want a logo/header designed for branding.
```








