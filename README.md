## 🚀 CodeQuest — Local Setup

> A simple, friendly README to get CodeQuest running on your machine. Follow these steps to clone, install, migrate, and run the project locally.

---

## ✨ Prerequisites

- ✅ Windows, macOS or Linux
- ✅ Python 3.8+ (3.10+ recommended)
- ✅ Git
- ✅ (Optional) A code editor like VS Code

Pro tip: Use a virtual environment to avoid polluting your system Python.

---

## 📦 Quick setup (Windows PowerShell)

1. Clone the repo

```powershell
git clone https://github.com/Rohan-Suryawanshi/CodeQuest.git
# or (SSH)
git clone git@github.com:Rohan-Suryawanshi/CodeQuest.git
```

2. Change into the project root

```powershell
cd CodeQuest
```

3. Create a virtual environment

```powershell
python -m venv .venv
```

4. Activate the virtual environment

- PowerShell (recommended):

```powershell
.\.venv\Scripts\Activate.ps1
```

- Command Prompt (cmd.exe):

```cmd
.\.venv\Scripts\activate
```

- Bash (WSL / macOS / Linux):

```bash
source .venv/bin/activate
```

5. Install dependencies

```powershell
pip install -r .\requirements.txt
```

6. Apply Django migrations

```powershell
python manage.py migrate
```

7. (Optional) Create a superuser for admin access

```powershell
python manage.py createsuperuser
```

Guest credentials (for quick local testing):

- username: `admin`
- password: `admin`

Note: These guest credentials are for quick testing only. Do not use them in production.

8. Run the development server

```powershell
python manage.py runserver
```

9. Open your browser

Visit: http://127.0.0.1:8000/

---

## 🧰 Useful commands

- Run tests:

```powershell
python manage.py test
```

- Create initial data / fixtures (if you have any fixtures):

```powershell
python manage.py loaddata <fixture-file>
```

---

## ❗ Troubleshooting

- ModuleNotFoundError: No module named 'requests'

  - If you see an error about `requests` or another package, install it manually:

  ```powershell
  pip install requests
  # then re-run: python manage.py migrate
  ```

- Can't activate venv on PowerShell: Execution policy error

  - Run PowerShell as Administrator and allow script execution (temporary):

  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
  .\.venv\Scripts\Activate.ps1
  ```

---

## 🔒 Security & notes

- This project uses a local SQLite database by default (`db.sqlite3`) for convenience in development.
- Do not commit secrets or production settings to the repository.

---

## 🙌 Contributing

If you'd like to contribute:

1. Fork → create a feature branch → open a PR.
2. Keep changes small and focused. Add tests where possible.

---

## ❤️ Thanks

Thanks for trying out CodeQuest — happy hacking! If you want help running the app locally, paste any terminal errors and I’ll help you fix them.
