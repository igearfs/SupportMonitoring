---

## 🛠️ CONTRIBUTING.md — _SupportMonitoring System_

Welcome! This document outlines how to set up a local development environment, contribute code, file issues, and follow project standards.

---

### 🧰 Local Development Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/your/repo.git
cd your-repo
```

#### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the Server

```bash
python manage.py runserver
```

> Default port: `http://127.0.0.1:8000/`

---

### 📋 Contribution Guidelines

#### Code Style

- Follow [PEP8](https://peps.python.org/pep-0008/) for Python
- Use 4-space indentation
- Prefer clear, verbose variable names (e.g., `check_api_health()` over `chk_api()`)

#### Pull Requests

- Use a feature branch: `feature/your-feature-name`
- Submit to `master` or `develop`, depending on team flow
- Include a clear PR description
- Reference issue IDs in your commits and PRs (e.g., `Fixes #42`)

#### Commits

- Keep commits atomic and descriptive  
  ✅ `Fix TCP timeout handling for non-responding hosts`  
  ❌ `stuff`

---

### 📌 Filing Issues / Reporting Bugs

When reporting a bug, include:

- ✅ What you expected to happen  
- ❌ What actually happened  
- 🪵 Logs or traceback (if available)  
- 💻 Your environment (OS, Python version, etc.)

---

### 📦 Feature Ideas

If you're submitting a new feature:

- Check `KNOWN_ISSUES.md` or the GitHub [Issues](https://github.com/your/repo/issues)
- Start with a GitHub issue or a discussion before opening a PR
- Include any relevant config or UX implications

---

### 🚧 Known Development Limitations

_Tracked in [`KNOWN_ISSUES.md`](KNOWN_ISSUES.md)_ — Commonly known issues, limitations, and areas under active development include:

- Alerting integrations (Twilio, Jira) are minimally tested
- Dashboard lacks login/authentication
- No user interface to configure targets — currently hardcoded
- HTTPS not implemented (internal-only usage assumed)

---

### ✅ Contribution Checklist

Before opening a pull request:

- [ ] Run local tests via `python manage.py test`
- [ ] If alert logic was touched, test alert paths with dummy data
- [ ] Update docs or inline comments if relevant
- [ ] Add yourself to `CONTRIBUTORS.md` (if applicable)

---

Thank you for contributing to **SupportMonitoring**!  
For questions, please reach out to the maintainers or open a GitHub Discussion.

---
### ❤️ Support This Project

If you find this project useful or want to support continued development:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/igearfs)

Your support fuels prototypes, uptime tools, and indie infrastructure builds.
