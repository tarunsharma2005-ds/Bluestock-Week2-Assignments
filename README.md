# Bluestock Fintech — Week 2 Prerequisite Project

**Prepared for:** Data Analytics Internship  
**Level:** Beginner  
**Device instructions:** macOS / MacBook

## Project overview

This repository contains six Week 2 deliverables:

1. Stock-market fundamentals summary
2. Listed-company financial-statement analysis framework
3. REST API → JSON → CSV practical
4. Git & GitHub workflow
5. Software data-flow architecture diagram
6. Indian FinTech research report

> Educational project only. This is not investment advice. Verify company figures against the latest official annual report before submission. The financial analysis document uses a clearly marked template so unverified figures are not presented as facts.

## Folder structure

```text
Bluestock_Week2_Project/
├── README.md
├── stock_market/
│   ├── stock_market_summary.md
│   └── financial_statement_analysis.md
├── api_project/
│   ├── api_data_extraction.py
│   ├── data/
│   │   └── api_data_sample.csv
│   └── README.md
├── software_architecture/
│   └── data_flow_diagram.md
├── fintech_research/
│   └── fintech_platform_analysis.md
├── git_github/
│   └── git_github_guide.md
└── references/
    └── sources.md
```

## Run the API assignment on a Mac

1. Download and unzip this project.
2. Open Terminal.
3. Type `cd ` (include a space), then drag the unzipped `Bluestock_Week2_Project` folder into Terminal and press Return.
4. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```
5. Activate it:
   ```bash
   source .venv/bin/activate
   ```
6. Install the one required library:
   ```bash
   python -m pip install requests
   ```
7. Run the script:
   ```bash
   python api_project/api_data_extraction.py
   ```
8. The downloaded CSV is saved in `api_project/data/api_posts.csv`.

If your Mac says `python3: command not found`, install Python 3 from https://www.python.org/downloads/macos/ and reopen Terminal.

## Recommended order

1. Read `stock_market/stock_market_summary.md`.
2. Complete `stock_market/financial_statement_analysis.md` using the latest official annual report for your chosen listed company.
3. Run the API script and inspect the CSV.
4. Read and draw the software architecture diagram.
5. Read the FinTech research report.
6. Follow `git_github/git_github_guide.md` to upload your work.

## Before submitting

- Replace all `[FILL IN]` fields in the financial analysis.
- Add your name, date and mentor details if required.
- Run the API script and confirm the CSV exists.
- Add screenshots of the API response and CSV if requested.
- Push the folder to your GitHub repository.
