# Git & GitHub — Beginner Guide for Mac

## Basic terms
- **Repository (repo):** project files plus their version history.
- **Clone:** download a remote repository to your computer.
- **Commit:** save a named snapshot in local history.
- **Push:** upload local commits to GitHub.
- **Pull:** bring remote changes to your local repository.
- **Branch:** an independent line of work.
- **Pull request (PR):** propose changes for review before merging.

## One-time setup
Install Git if it is not already available. In Terminal:

```bash
git --version
```

If macOS offers to install Command Line Developer Tools, follow the prompt. Configure your commit identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Use the email associated with your GitHub account if you wish. Do not share passwords or access tokens.

## Create a repository locally
From the project folder:

```bash
git init
git status
git add README.md stock_market api_project software_architecture fintech_research git_github references
git commit -m "Add Bluestock Week 2 prerequisite assignments"
```

After creating an empty repository on GitHub, follow the repository page's instructions to add the remote and push. Example (replace the URL with your own repository URL):

```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

If GitHub asks you to authenticate, use its supported sign-in flow. Do not paste passwords or tokens into the project files.

## Daily workflow
```bash
git status
git add .
git commit -m "Describe the change clearly"
git push
```

To download changes made remotely:
```bash
git pull
```

## Branch and pull request
```bash
git switch -c improve-financial-analysis
# Edit files, then:
git add stock_market/financial_statement_analysis.md
git commit -m "Complete financial analysis"
git push -u origin improve-financial-analysis
```
Open GitHub in your browser and create a pull request from that branch if your assignment or mentor requires a PR.

## Safety checklist
- Never commit passwords, API keys, access tokens or private customer data.
- Review `git status` before committing.
- Use clear commit messages.
