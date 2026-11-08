<div align="center">

# ITI GANS-AI

### My journey through the ITI Generative AI track

Coursework, labs, and small projects, added week by week as I learn.

![Week 1](https://img.shields.io/badge/Week%201-Finished-success?style=for-the-badge)
![Progress](https://img.shields.io/badge/Progress-1%2F14%20weeks-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NASA API](https://img.shields.io/badge/NASA-NeoWs%20API-0B3D91?style=for-the-badge&logo=nasa&logoColor=white)
![Platform](https://img.shields.io/badge/Windows-PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)

[About](#about) · [Progress](#course-progress) · [Week 1](#week-1-nasa-asteroid-report) · [Getting started](#getting-started) · [Troubleshooting](#troubleshooting) · [Roadmap](#roadmap) · [Repository guide](#repository-guide)

</div>

---

## About

Hi, and welcome! This repository is where I keep my work from the ITI Generative AI track. The course starts with Python basics and builds all the way up to agents, retrieval, and evaluation, so I'm adding one project per week as I go.

A few things you'll find here:

- Finished, runnable projects with setup steps you can actually follow
- Safe handling of secrets, so API keys never end up on GitHub
- Short notes on what each week covered
- An honest roadmap of what's still ahead

Finished weeks are marked **Finished**, and the week I'm working on is marked **In progress**.

---

## Course progress

```text
[█░░░░░░░░░░░░░] 1 of 14 weeks finished
```

| Week | Topic | Status |
| :--: | :---- | :----: |
| **W1** | Python foundations | **Finished** |
| W2 | The generative AI landscape | Upcoming |
| W3 | Generative AI for the developer | Upcoming |
| W4 | AI-assisted coding | Upcoming |
| W5 | Building Gen-AI powered apps | Upcoming |
| W7 | Agent foundations | Upcoming |
| W8 | Frameworks and orchestration | Upcoming |
| W9 | Multi-agent teams and landscape | Upcoming |
| W10 | From chains to graphs | Upcoming |
| W11 | Tool-use and MCP | Upcoming |
| W12 | Retrieval science | Upcoming |
| W13 | Agentic RAG | Upcoming |
| W14 | Defensive engineering | Upcoming |
| W15 | Evaluation and observability | Upcoming |

W6 isn't in the course outline I have, so I'll add it once the topic is confirmed.

---

## Week 1: NASA asteroid report

**Status: Finished**

The first assignment was a Python program that talks to a public REST API, reads the JSON it sends back, stores each result in a small class, and prints a tidy report. I used NASA's asteroid data, which made it a fun one.

### What it does

- Fetches live data from NASA's NeoWs (Near Earth Object Web Service) feed
- Turns every asteroid into an `Asteroid` object
- Uses a `show()` method to print a readable summary for each one
- Loads the API key from a local `.env` file, so it never sits in the code
- Looks at one fixed day: **September 7, 2025**

### What each report shows

| Field | Description |
| :---- | :---------- |
| Name | The asteroid's designation |
| Max diameter | Its estimated maximum diameter, in kilometres |
| Hazard status | Whether NASA classifies it as potentially hazardous |

### Example output

This is just an illustration. The real values and the number of entries depend on what the API returns.

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

<!-- When you have a real screenshot, save it as docs/output.png and uncomment the line below.
![Program output](docs/output.png)
-->

### What I practiced

| Concept | Where it shows up |
| :------ | :---------------- |
| HTTP requests | Calling the NASA REST endpoint |
| JSON parsing | Working through nested dictionaries and lists |
| Object-oriented programming | The `Asteroid` class and its `show()` method |
| Environment variables | Keeping the API key out of the source code |
| Virtual environments | Isolated, repeatable dependencies |

### How it works

```text
  .env  -->  load the API key
                  |
                  v
     NASA NeoWs feed (GET request)
                  |
                  v
   JSON  -->  data["near_earth_objects"][date]
                  |
                  v
   Asteroid objects  -->  show()  -->  terminal report
```

### Using a different date

The date is fixed for this assignment. If you want another day, change these three things in `main.py`:

- `start_date`
- `end_date`
- the date used to access `data["near_earth_objects"]`

---

## Getting started

You'll need Python 3 and a free [NASA API key](https://api.nasa.gov/). The commands below are for **Windows PowerShell**, run from the project folder.

### 1. Create and activate the environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install the dependencies

```powershell
pip install -r requirements.txt
```

### 3. Add your API key

Copy the example file:

```powershell
Copy-Item .env.example .env
```

Then open `.env` and replace the placeholder with your own NASA key:

```dotenv
NASA_API_KEY=your_nasa_api_key_here
```

Your real `.env` stays on your machine and is excluded from Git.

### 4. Run it

```powershell
python main.py
```

The terminal prints the HTTP status first, then the asteroid report.

### Quick run

If your `.env` is already set up:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

---

## Troubleshooting

<details>
<summary><b><code>python</code> is not recognized</b></summary>

Try the Python launcher when creating the environment:

```powershell
py -m venv venv
```

</details>

<details>
<summary><b>PowerShell blocks the activation script</b></summary>

You can skip activation and run Python straight from the environment:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe main.py
```

</details>

<details>
<summary><b>The status code isn't 200</b></summary>

Check that `.env` exists, that the variable is named exactly `NASA_API_KEY`, and that the key is valid. Make sure there are no quotes or extra spaces around it.

</details>

---

## Roadmap

- [x] **W1**: Python foundations (NASA asteroid report)
- [ ] **W2**: The generative AI landscape
- [ ] **W3**: Generative AI for the developer
- [ ] **W4**: AI-assisted coding
- [ ] **W5**: Building Gen-AI powered apps
- [ ] **W7**: Agent foundations
- [ ] **W8**: Frameworks and orchestration
- [ ] **W9**: Multi-agent teams and landscape
- [ ] **W10**: From chains to graphs
- [ ] **W11**: Tool-use and MCP
- [ ] **W12**: Retrieval science
- [ ] **W13**: Agentic RAG
- [ ] **W14**: Defensive engineering
- [ ] **W15**: Evaluation and observability

---

## Repository guide

```text
ITI/
├── main.py             # W1: NASA asteroid report
├── requirements.txt    # Python dependencies
├── .env.example        # API key template
├── .gitignore          # Files excluded from Git
├── LICENSE             # MIT license
└── README.md           # You are here
```

Virtual environments, Python cache files, and the local API key are all excluded from the repository.

---

## Security

- Never commit your real `.env` file.
- Only `.env.example`, with its placeholder, is tracked by Git.
- If a key ever gets pushed by mistake, revoke it and generate a new one from the NASA API portal.

---

## Saving changes to GitHub

Once the remote is connected, this is the workflow I use to upload updates:

```powershell
git status
git add README.md main.py requirements.txt .env.example .gitignore LICENSE
git diff --cached
git commit -m "Update week 1 coursework"
git push
```

It's worth reviewing the staged changes before committing. As new coursework gets added, include its files too.

---

## About me

**Your Name**
ITI Generative AI track student

- GitHub: [github.com/your-username](https://github.com/your-username)
- LinkedIn: [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)
- Email: your.email@example.com

---

## License

This project is released under the [MIT License](LICENSE). Feel free to learn from it, reuse it, and build on it.

---

## Acknowledgements

- [NASA Open APIs](https://api.nasa.gov/) for the NeoWs asteroid data
- The ITI instructors and everyone running the Generative AI track

---

<div align="center">

If this repo helped you, a star would make my day.

Built week by week, and still growing.

</div>
