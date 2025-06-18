import os
import json
#import sys

def run_trufflehog():
    print("[*] Running TruffleHog...")
    os.system("trufflehog filesystem --json . > reports/trufflehog_report.json 2>/dev/null")

def run_bandit():
    print("[*] Running Bandit...")
    os.system("bandit -r . -f json -o reports/bandit_report.json")

def run_semgrep():
    print("[*] Running Semgrep...")
    os.system("semgrep --config ./semgrep-rules/ --json > reports/semgrep_report.json")

def main():
    os.makedirs("reports", exist_ok=True)
    run_trufflehog()
    run_bandit()
    run_semgrep()
    os.system("python generate_html.py")

    # Optional: fail if high severity issue in Bandit
   # try:
    #    with open("reports/bandit_report.json") as f:
     #       if '"issue_severity": "HIGH"' in f.read():
      #          print("[!] High severity Bandit issue found.")
       #         sys.exit(1)
    #except Exception as e:
     #   print(f"[!] Could not check Bandit severity: {e}")

if __name__ == "__main__":
    main()

