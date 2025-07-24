# 🔌 Azure Auto-Shutdown Tool

This tool automatically shuts down **running Azure Virtual Machines** that are tagged with `auto-stop:true`. It's designed to help reduce cloud costs in dev/test environments, where VMs are often left running unintentionally.

The shutdown script runs daily using **GitHub Actions** or can be triggered manually. It’s simple, lightweight, and easy to extend with logging, notifications, or dashboards.

---

## ✨ Features

- 🔍 Scans all VMs across your subscription
- 🏷️ Only affects VMs tagged with `auto-stop:true`
- ⏱️ Runs automatically every day via GitHub Actions
- 🔌 Stops only VMs that are currently **running**
- 💰 Helps save money in test/dev environments
- 🧱 Fully open source and extensible

---

## ⚙️ Setup Instructions

### 🔐 1. Create an Azure Service Principal

Use Azure CLI:

```bash
az ad sp create-for-rbac --name AutoShutdownApp --role "Virtual Machine Contributor" --scopes /subscriptions/<YOUR_SUBSCRIPTION_ID>
```

Save the output (client ID, secret, tenant) and your subscription ID.

### 🔒 2. Add GitHub Secrets

In your GitHub repo, go to:  
**Settings → Secrets and variables → Actions → New repository secret**

Add the following:

| GitHub Secret Name        | Value                           |
|---------------------------|----------------------------------|
| `AZURE_CLIENT_ID`         | `appId` from CLI                 |
| `AZURE_CLIENT_SECRET`     | `password` from CLI              |
| `AZURE_TENANT_ID`         | `tenant` from CLI                |
| `AZURE_SUBSCRIPTION_ID`   | your Azure subscription ID       |

---

### 🏷️ 3. Tag VMs for Auto-Shutdown

Only VMs tagged with the following key/value pair will be affected:

```
Key:    auto-stop
Value:  true
```

You can add tags in the Azure portal or via CLI.

---

### 🐍 4. Python Script (`shutdown.py`)

This script scans your subscription and stops VMs with the tag `auto-stop:true`.

See `shutdown.py` in this repo.

---

### ⚙️ 5. GitHub Action Workflow (`.github/workflows/autoshutdown.yml`)

The included GitHub Action runs daily at 20:00 UTC or on demand.

See `.github/workflows/autoshutdown.yml` in this repo.

---

### 🧪 6. Sample Output

```
🔍 Scanning Azure VMs...
🟡 Stopping VM: dev-test-vm
✅ VM stopped: dev-test-vm
✔ Done.
```

---

## 🔧 Ideas for Extensions

- 📧 Email or Slack alerts
- 📊 Usage reports / cost savings log
- 🌐 Streamlit or FastAPI dashboard
- 🔁 Optional restart time
- 🧠 Machine-learning-based usage prediction (just for fun!)

---

## 📄 License

MIT License.  
Free to use, modify, and extend. Pull requests welcome!

---

## 👨‍💻 Author

Christian Snouno  
Cloud Automation | Python | DevOps  
github.com/ChristianSnouno
linkedin.com/in/christian-snouno-b2455921b/

---

## 💬 Feedback

If you find this useful or have ideas for improvement, feel free to open an issue or contact me.  
Let’s save some cloud costs together! 🚀
