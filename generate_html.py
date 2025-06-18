import json
from jinja2 import Environment, FileSystemLoader

def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return []

def main():
    bandit = load_json("reports/bandit_report.json").get("results", [])
    semgrep = load_json("reports/semgrep_report.json").get("results", [])
    trufflehog = load_json("reports/trufflehog_report.json")

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("dashboard_template.html")
    html = template.render(bandit=bandit, semgrep=semgrep, trufflehog=trufflehog)

    with open("reports/dashboard.html", "w") as f:
        f.write(html)
    print("[+] HTML report generated.")

if __name__ == "__main__":
    main()

