import os
import pickle
import subprocess
import hashlib
import base64
import requests

# 🚨 Hardcoded secrets (TruffleHog)
GITHUB_TOKEN = "ghp_examplehardcodedtoken1234567890"
AWS_SECRET_KEY = "AKIAEXAMPLEFAKEKEY12345"
DB_PASSWORD = "root123"

# 🚨 Dangerous eval
user_input = "print('Hacked!')"
eval(user_input)

# 🚨 Dangerous exec
exec("print('Executing shell...')")

# 🚨 Use of pickle (Bandit: insecure deserialization)
data = pickle.dumps({"user": "admin"})
user = pickle.loads(data)

# 🚨 Weak hash (Bandit)
password = "admin123"
hashed = hashlib.md5(password.encode()).hexdigest()

# 🚨 Command injection (Bandit)
filename = input("Enter filename to read: ")
os.system(f"cat {filename}")

# 🚨 Subprocess shell=True
subprocess.call("ls -la", shell=True)

# 🚨 Base64 misuse
print(base64.b64decode("U2VjcmV0IG1lc3NhZ2U="))

# 🚨 Hardcoded URL
requests.post("http://insecure-api.local/submit", data={"token": GITHUB_TOKEN})

