# ITI GANS-AI

My coursework and small projects from the ITI generative AI track. I'll update this repository as I work through each week.

**Current week: W1 — Python foundations**

[Getting started](#getting-started) · [Week 1 project](#week-1--python-foundations) · [Timeline](#timeline) · [Repository guide](#repository-guide)

## Week 1 — Python foundations

The first assignment is a short Python program that calls a public REST API, reads its JSON response, stores the results in a small class, and prints a formatted summary.

### NASA asteroid report

The program uses NASA's NeoWs feed to fetch asteroid data for **September 7, 2025**. Each result becomes an `Asteroid` object. Its `show()` method prints:

- The asteroid's name.
- Its estimated maximum diameter in kilometres.
- Whether it is classified as potentially hazardous.

This exercise brings together HTTP requests, dictionaries, lists, classes, and environment variables. The API key is loaded from a local `.env` file.

The date is fixed for this assignment. To use another day, change `start_date`, `end_date`, and the date used to access `data["near_earth_objects"]` in `main.py`.

## Getting started

You need Python 3 and a NASA API key. Run the following commands from the project folder in **Windows PowerShell**.

### 1. Create and activate the environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install the dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure the API key

Copy the example file:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace the placeholder with your NASA key:

```dotenv
NASA_API_KEY=your_nasa_api_key_here
```

The real `.env` stays on your machine and is excluded from Git.

### 4. Run the report

```powershell
python main.py
```

The terminal prints the HTTP status, followed by the asteroid report. Values and the number of entries depend on the API response.

### Quick run

Once your `.env` is ready:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

If `python` isn't recognised, try `py` when creating the environment. If PowerShell blocks activation, run Python directly from the environment:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe main.py
```

## Timeline

W1 is in progress. The rest of the course is still ahead.

| Week | Topic | Progress |
| :--- | :--- | :--- |
| W1 | Python foundations | In progress |
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

W6 isn't listed in the course outline I have. I'll add it when the topic is confirmed.

## Repository guide

```text
ITI/
├── main.py             # W1: NASA asteroid report
├── requirements.txt    # Python dependencies
├── .env.example        # API key template
├── .gitignore          # Files excluded from Git
└── README.md
```

Virtual environments, Python cache files, and the local API key are excluded from the repository.

## Saving changes to GitHub

Once the remote is connected, this is the workflow for uploading updates:

```powershell
git status
git add README.md main.py requirements.txt .env.example .gitignore
git diff --cached
git commit -m "Update week 1 coursework"
git push
```

Review the staged changes before committing. As new coursework is added, include its files in the commit too.
