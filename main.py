import subprocess

subprocess.call("'C:\Windows\System32\powershell.exe iwr -useb https://raw.githubusercontent.com/spicetify/cli/main/install.ps1 | iex", shell=True)
subprocess.call("'C:\Windows\System32\powershell.exe iwr -useb https://raw.githubusercontent.com/spicetify/marketplace/main/resources/install.ps1 | iex", shell=True)