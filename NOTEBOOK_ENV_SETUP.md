# Notebook / project environment setup

Use this when you want a quick, repo-level setup for notebooks and scripts in this course.

## 1) Create and activate the virtual environment

PowerShell:

```powershell
cd "C:\Users\mehul\source\GitHub\AgenticAI_3.0_2026"
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 2) Install the project dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3) Create your local secrets file

Copy the example file and fill in only the keys you need:

```powershell
Copy-Item .env.example .env
```

Then edit `.env` locally and keep it out of git. The repo root already ignores `.env`.

## 4) Use the environment in notebooks

At the top of a notebook, load the environment variables:

```python
from dotenv import load_dotenv
load_dotenv()
```

This keeps the project notebook-friendly without committing real API keys.
