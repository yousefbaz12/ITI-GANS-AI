<div align="center">

# 🚀 ITI GANS-AI

### Generative AI & Agentic Systems — Coursework, Labs & Projects

A week-by-week journey through the ITI generative AI track: from Python foundations to agents, RAG, and production-grade evaluation.

![Status](https://img.shields.io/badge/Week%201-Finished%20✅-success?style=for-the-badge)
![Progress](https://img.shields.io/badge/Progress-1%2F14%20weeks-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NASA API](https://img.shields.io/badge/NASA-NeoWs%20API-0B3D91?style=for-the-badge&logo=nasa&logoColor=white)
![Platform](https://img.shields.io/badge/Windows-PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)

[Overview](#-overview) · [Course Progress](#-course-progress) · [Week 1 Project](#-week-1--nasa-asteroid-report) · [Getting Started](#-getting-started) · [Troubleshooting](#-troubleshooting) · [Roadmap](#-roadmap) · [Repository Guide](#-repository-guide)

</div>

---

## 📖 Overview

This repository documents my work through the **ITI Generative AI track**. Each week adds a new project that builds on the previous one, moving from core Python skills to full multi-agent and retrieval-augmented systems.

**What you'll find here:**

- ✅ Finished, runnable projects with clear setup instructions
- 🔐 Safe handling of secrets (API keys never committed)
- 📚 Notes on what each week covers and what I learned
- 🗺️ A transparent roadmap of everything still to come

> **Updates:** this repo grows weekly. Completed weeks are marked **Finished**, the current one is marked **In progress**.

---

## 📊 Course Progress

```text
[█░░░░░░░░░░░░░] 1 / 14 weeks finished
```

| Week | Topic | Status |
| :--: | :---- | :----: |
| **W1** | Python foundations | ✅ **Finished** |
| W2 | The generative AI landscape | ⏳ Upcoming |
| W3 | Generative AI for the developer | ⏳ Upcoming |
| W4 | AI-assisted coding | ⏳ Upcoming |
| W5 | Building Gen-AI powered apps | ⏳ Upcoming |
| W7 | Agent foundations | ⏳ Upcoming |
| W8 | Frameworks and orchestration | ⏳ Upcoming |
| W9 | Multi-agent teams and landscape | ⏳ Upcoming |
| W10 | From chains to graphs | ⏳ Upcoming |
| W11 | Tool-use and MCP | ⏳ Upcoming |
| W12 | Retrieval science | ⏳ Upcoming |
| W13 | Agentic RAG | ⏳ Upcoming |
| W14 | Defensive engineering | ⏳ Upcoming |
| W15 | Evaluation and observability | ⏳ Upcoming |

> **Note:** W6 isn't listed in the course outline I have. I'll add it as soon as the topic is confirmed.

---

## ☄️ Week 1 — NASA Asteroid Report

**Status: ✅ Finished**

A Python program that calls a public REST API, parses the JSON response, stores each result in a custom class, and prints a clean formatted report.

### ✨ Features

- 🌐 Fetches live data from NASA's **NeoWs** (Near Earth Object Web Service) feed
- 🧱 Models every asteroid as an `Asteroid` object
- 🖨️ `show()` method prints a readable summary per asteroid
- 🔑 Loads the API key securely from a local `.env` file
- 📅 Targets a fixed date: **September 7, 2025**

### 📋 What each asteroid report shows

| Field | Description |
| :---- | :---------- |
| **Name** | The asteroid's designation |
| **Max diameter** | Estimated maximum diameter, in kilometres |
| **Hazard status** | Whether NASA classifies it as potentially hazardous |

### 🖥️ Example output

> Illustrative only — actual values and the number of entries depend on the live API response.

```text
Status code: 200

Name: (2020 XY)
Estimated max diameter: 0.152 km
Potentially hazardous: False
-----------------------------
Name: (2019 AB)
Estimated max diameter: 0.431 km
Potentially hazardous: True
-----------------------------
```

### 🧠 Concepts practiced

| Concept | How it's used |
| :------ | :------------ |
| HTTP requests | Calling the NASA REST endpoint |
| JSON parsing | Reading nested dictionaries and lists |
| OOP | The `Asteroid` class and its `show()` method |
| Environment variables | Keeping the API key out of source code |
| Virtual environments | Isolated, reproducible dependencies |

### 🔧 How it works

```text
  .env ──► load API key
                │
                ▼
   NASA NeoWs feed (GET request)
                │
                ▼
     JSON ──► data["near_earth_objects"][date]
                │
                ▼
   Asteroid objects ──► show() ──► terminal report
```

### 🗓️ Changing the date

The date is fixed for this assignment. To use another day, update these three places in `main.py`:

- `start_date`
- `end_date`
- the date key used to access `data["near_earth_objects"]`

---

## ⚡ Getting Started

**Requirements:** Python 3 and a free [NASA API key](https://api.nasa.gov/).

All commands below are for **Windows PowerShell**, run from the project folder.

### 1️⃣ Create and activate the environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2️⃣ Install the dependencies

```powershell
pip install -r requirements.txt
```

### 3️⃣ Configure your API key

Copy the example file:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace the placeholder with your NASA key:

```dotenv
NASA_API_KEY=your_nasa_api_key_here
```

> 🔒 Your real `.env` stays on your machine and is excluded from Git.

### 4️⃣ Run the report

```powershell
python main.py
```

The terminal prints the HTTP status, followed by the asteroid report.

### 🏃 Quick run

Once your `.env` is ready:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

---

## 🛠️ Troubleshooting

<details>
<summary><b><code>python</code> is not recognized</b></summary>

Try the Python launcher instead when creating the environment:

```powershell
py -m venv venv
```

</details>

<details>
<summary><b>PowerShell blocks the activation script</b></summary>

Skip activation and run Python directly from the environment:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe main.py
```

</details>

<details>
<summary><b>Status code is not 200</b></summary>

Check that `.env` exists, the variable is named exactly `NASA_API_KEY`, and the key is valid. The key must not contain quotes or extra spaces.

</details>

---

## 🗺️ Roadmap

- [x] **W1** — Python foundations (NASA asteroid report)
- [ ] **W2** — The generative AI landscape
- [ ] **W3** — Generative AI for the developer
- [ ] **W4** — AI-assisted coding
- [ ] **W5** — Building Gen-AI powered apps
- [ ] **W7** — Agent foundations
- [ ] **W8** — Frameworks and orchestration
- [ ] **W9** — Multi-agent teams and landscape
- [ ] **W10** — From chains to graphs
- [ ] **W11** — Tool-use and MCP
- [ ] **W12** — Retrieval science
- [ ] **W13** — Agentic RAG
- [ ] **W14** — Defensive engineering
- [ ] **W15** — Evaluation and observability

---

## 📁 Repository Guide

```text
ITI/
├── main.py             # W1: NASA asteroid report
├── requirements.txt    # Python dependencies
├── .env.example        # API key template
├── .gitignore          # Files excluded from Git
└── README.md           # You are here
```

Virtual environments, Python cache files, and the local API key are excluded from the repository.

---

## 🔐 Security

- Never commit your real `.env` file.
- Only `.env.example` (with a placeholder) is tracked.
- If a key is ever pushed by mistake, revoke it and generate a new one from the NASA API portal.

---

## 💾 Saving Changes to GitHub

Once the remote is connected, use this workflow to upload updates:

```powershell
git status
git add README.md main.py requirements.txt .env.example .gitignore
git diff --cached
git commit -m "Update week 1 coursework"
git push
```

Review the staged changes before committing. As new coursework is added, include its files in the commit too.

---

## 🙌 Acknowledgements

- [NASA Open APIs](https://api.nasa.gov/) for the NeoWs asteroid data
- The **ITI** instructors and the Generative AI track

---

<div align="center">

**⭐ If you find this repo useful, consider giving it a star.**

Built week by week · Updated as the course progresses

</div>
