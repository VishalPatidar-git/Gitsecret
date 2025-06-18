import json
from jinja2 import Environment, FileSystemLoader

def load_json(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
            elif isinstance(data, list):
                return {"results": data}
    except Exception as e:
        print(f"[!] Failed to load {path}: {e}")
    return {"results": []}

def main():
    bandit = load_json("reports/bandit_report.json")
    semgrep = load_json("reports/semgrep_report.json")
    trufflehog = load_json("reports/trufflehog_report.json")

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("dashboard_template.html")
    html = template.render(
        bandit=bandit,
        semgrep=semgrep,
        trufflehog=trufflehog
    )

    with open("reports/dashboard.html", "w") as f:
        f.write(html)
    print("[+] HTML dashboard generated: reports/dashboard.html")

if __name__ == "__main__":
    main()

