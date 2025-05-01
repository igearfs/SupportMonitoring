
---

## 🐞 KNOWN_ISSUES.md — _SupportMonitoring System_

This document tracks known issues, caveats, and limitations in the current prototype state of the project. It also outlines upcoming improvements and enhancements.

---

### 🚧 Current Limitations (Prototype Phase)

| Area | Description | Priority |
|------|-------------|----------|
| 🔒 **No HTTPS support** | The system is intended for internal environments only. HTTPS support is not configured. | 🔥 High |
| 👤 **No Authentication** | The dashboard is publicly accessible. User authentication is not implemented yet. | ⚠️ Medium |
| 🧠 **Hardcoded Targets** | Monitoring targets are defined directly in `views.py`. No UI or config-based input yet. | ⚠️ Medium |
| 📊 **Frontend is basic** | No real-time updates beyond auto-refresh. Dashboard has minimal interactivity. | ⚪ Low |
| 🚨 **Alerting not fully wired** | Jira, Twilio, and Email alerts are stubbed but not fully enabled or tested. | 🔥 High |
| 🧪 **Test Coverage** | Limited or no automated test coverage for alerting flows or SFTP checks. | 🔥 High |
| 🗂️ **Missing Dockerization** | Project is not containerized. Setup requires local Python/Django environment. | ⚠️ Medium |
| 📁 **No persistent state** | No DB logging or persistence for check history, alerts, or failures. | ⚪ Low |

---

### 🧱 Planned Improvements

- [ ] Move target configuration to a `targets.json` file or DB model
- [ ] Add simple admin authentication via Django Auth
- [ ] Implement HTTPS using Let’s Encrypt or reverse proxy
- [ ] Enable alert toggles (email/SMS/Jira) from UI or config
- [ ] Dockerfile for local and prod deployment
- [ ] Frontend enhancements (real-time websocket updates, filters)
- [ ] Alert retry logic & error deduplication

---

### ❤️ Support This Project

If you find this project useful or want to support continued development:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/igearfs)

Your support fuels prototypes, uptime tools, and indie infrastructure builds.


---
