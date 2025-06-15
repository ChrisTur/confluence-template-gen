# Contributing to Confluence Template Generator

Thank you for your interest in contributing! This project helps automate the creation of consistent Confluence documentation using templates and a simple CLI. Your feedback, ideas, and code contributions are always welcome.

---

## 🚀 How to Contribute

### 1. Fork the Repository

Click the **Fork** button on the top right of the [GitHub repo](https://github.com/<your-username>/confluence-template-generator) and clone your fork locally:

```bash
git clone https://github.com/<your-username>/confluence-template-generator.git
cd confluence-template-generator
```

### 2. Create a Feature Branch
Use a clear and descriptive branch name:

```bash
git checkout -b feature/add-new-template
```
### 3. Install Dependencies

Use Python 3.8+ and install the required packages:

```bash
pip install -r requirements.txt
```
### 4. Make Your Changes
Common contribution types:

Add new templates to config.sample.yaml

Enhance CLI functionality or error handling

Improve template rendering logic in generate_confluence_page.py

Update documentation (README.md, comments, etc.)

### 5. Lint and Test
Ensure the code is clean and functional. Optionally, use tools like black, flake8, or pytest for formatting and testing.

### 6. Commit and Push
```bash

git add .
git commit -m "Add: new release notes template"
git push origin feature/add-new-template
```

### 7. Open a Pull Request
Go to your fork and open a Pull Request (PR) to the main branch of this repository.

Include:

What you changed

Why the change is useful

Any screenshots or examples (if applicable)

✅ Contribution Guidelines
Keep secrets out: Never commit actual Confluence credentials. Use config.sample.yaml to provide examples only.

Use descriptive commit messages.

Follow the project’s structure: Keep templates inside config.sample.yaml, logic in generate_confluence_page.py, and dependencies in requirements.txt.

If adding a new template, consider documenting its purpose in the README.md.
