# SecGuard
Hey foks This tool is a source code scanner which can test the source code locally as well as on the github just make a directory and push the Secguard in the repository that you want to scan and create a workflow that's all.

##How to run the scan locally to test the source code.

Step1:
Git clone the repo 
Step2: 
Place this Gitsecret folder in the source code folder.
Step3:
'''cd Gitsecret'''
'''pip3 install -r requirements.txt'''
'''python3 scan.py'''
'''xdg-open reports/dashboard.html''' # You can directly open the report from gui

There is a  test directory in which bad.py is available to test the tool.

How to run the scan if the source code is available on Git hub and you want to run the scan on git hub only.

Step1:
Upload the Gitsecret folder to the repository you want to scan
Step2:
Go to your repo → Actions tab
Step3:
Create a workflow and copy paste the contents of secguard.yml in your wlorflow file and commite chages.
Step4: 
You can run the scan from actions tab from there only you can download the scan results.

