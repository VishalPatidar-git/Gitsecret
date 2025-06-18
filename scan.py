import os
import sys

def run_trufflehog():
    os.system("trufflehog filesystem --fail --no-update --json . > reports/trufflehog_report.json")

def run_bandit():
    os.system("bandit -r . -f json -o reports/bandit_report.json")

def run_semgrep():
    os.system("semgrep --config ./semgrep-rules/ --json > reports/semgrep_report.json")

def main():
    os.makedirs("reports", exist_ok=True)
    run_trufflehog()
    run_bandit()
    run_semgrep()
    os.system("python generate_html.py")

if __name__ == "__main__":
    main()

with open("reports/bandit_report.json") as f:
    if '"issue_severity": "HIGH"' in f.read():
        print("[!] High severity Bandit issue found.")
        sys.exit(1)

