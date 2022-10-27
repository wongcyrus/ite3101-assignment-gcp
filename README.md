# Python Assignment 2022

## Windows
### Change Powershell execution policy

Demo of setting up the Execution Policy.
https://youtu.be/R11kUjafVEo?list=PLtgJR0xD2TPdBfg5oIKseNuN0tX_DgPkH&t=1738

Open a Powershell window as administrator and type the following:
```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```
Then respond y to any questions.

You need to use create virtual environment as you should not corrupt your default Python in Windows PC.
```
python -m venv .venv
.venv/Scripts/Activate.ps1
pip install -r requirements.txt
```

## Codespace
You do not need to do anything! 
It will install Python Add-on, create new virtual environment, and install Python dependencies for you automaically.
You can review devcontainer.json and DockerFile in ./devcontainer folder for more details.

![Open in Codespaces](https://classroom.github.com/assets/open-in-codespaces-abfff4d4e15f9e1bd8274d9a39a0befe03a0632bb0f153d0ec72ff541cedbe34.svg)
