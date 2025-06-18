
# 🔐 SecGuard

**SecGuard** is a lightweight and developer-friendly source code security scanner for Python projects. It uses trusted tools like `Bandit`, `Semgrep`, and `TruffleHog` to detect:

- Hardcoded secrets (API keys, tokens, passwords)
- Insecure code patterns (e.g. `eval()`, `exec()`, weak crypto)
- Dangerous logic and vulnerabilities in source code

Scan your code either **locally** or via **GitHub Actions CI**, with a clean HTML dashboard report generated at the end.

---

## 🚀 Features

- ✅ Scans for secrets and vulnerabilities using:
  - [Bandit](https://github.com/PyCQA/bandit)
  - [Semgrep](https://semgrep.dev/)
  - [TruffleHog](https://github.com/trufflesecurity/trufflehog)
- 📊 Generates a user-friendly HTML dashboard
- 💡 Includes sample vulnerable code for testing
- ☁️ Fully integrates with GitHub Actions for automated CI scans

---

## 📥 Local Setup & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/your-repo.git
cd your-repo
```

### 2. Place the `Gitsecret` (SecGuard) Folder

Copy the entire `Gitsecret` folder into the repo you want to scan.

### 3. Install Requirements

```bash
cd Gitsecret
pip3 install -r requirements.txt
```

### 4. Run the Scan

```bash
python3 scan.py
```

### 5. View the Report

```bash
xdg-open reports/dashboard.html
```

Or open `reports/dashboard.html` manually in your browser.

> ✅ A `test/bad.py` file is included to verify the scanner works correctly.

---

## ⚙️ GitHub Actions (CI Integration)

To automatically run scans on every push/PR via GitHub Actions:

### 1. Upload the `Gitsecret` Folder

Commit the full `Gitsecret` folder (scanner) into the repository you want to scan.

### 2. Create GitHub Actions Workflow

Create a file at:

```bash
.github/workflows/secguard.yml
```

Paste the contents of the provided `secguard.yml` workflow file (see `Gitsecret` folder).

### 3. Commit & Trigger the Scan

- Go to your repo → **Actions** tab
- Trigger a scan by pushing a commit or opening a PR
- Download the generated HTML report from **Artifacts**

---

## 📂 Project Structure

```
Gitsecret/
├── scan.py                    # Main scanner script
├── generate_html.py          # Combines all reports into an HTML dashboard
├── requirements.txt          # Dependencies
├── semgrep-rules/            # Custom Semgrep rules
│   └── custom.yml
├── templates/
│   └── dashboard_template.html
├── test/
│   └── bad.py                # Intentionally buggy test file
└── reports/                  # Auto-generated scan results
```

---

## 📌 Requirements

- Python 3.7+
- Git
- pip (Python package manager)

---

## 📣 Credits

SecGuard combines the power of:
- [Bandit](https://github.com/PyCQA/bandit)
- [Semgrep](https://semgrep.dev/)
- [TruffleHog](https://github.com/trufflesecurity/trufflehog)
- [Jinja2](https://jinja.palletsprojects.com/)

---

## 🛠️ License

MIT License – free for personal and commercial use.

---

## 💬 Feedback or Issues?

Feel free to [open an issue](https://github.com/your-org/your-repo/issues) or contribute to the tool!
