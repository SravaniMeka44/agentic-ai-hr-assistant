# agentic-ai-hr-assistant
AI-powered HR recruitment assistant using LangChain, LangGraph, Google Calendar and Docker



# Agentic AI HR Recruitment Assistant

An AI-powered HR recruitment assistant built using LangChain, LangGraph, OpenAI, Google Calendar API, and Docker.

## Features

- Natural-language interview scheduling
- Google Calendar integration
- Human-in-the-loop approval using LangGraph interrupts
- Professional interview invitation generation
- Calendar conflict detection
- Interview date and working-hours validation
- Conversation memory within an active session
- Docker containerization

## Tech Stack

- Python
- LangChain
- LangGraph
- OpenAI GPT-4.1-mini
- Google Calendar API
- Google OAuth 2.0
- Docker

## Project Architecture

```text
Recruiter
   |
   v
HR AI Agent
   |
   +-- Google Calendar Tools
   |      +-- View Events
   |      +-- View Date Range
   |      +-- Schedule Interview
   |
   v
Human Approval
   |
   v
Calendar Conflict Check
   |
   v
Google Calendar API
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/agentic-ai-hr-assistant.git
cd agentic-ai-hr-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure an OpenAI API key in `.env`.

Configure Google Calendar OAuth credentials locally using `credentials.json` and authorize the application to generate `token.json`.

Run locally:

```bash
python main.py
```

## Docker

Build the image:

```bash
docker build -t hr-assistant .
```

Run the container with your local environment variables and Google OAuth files mounted at runtime.

Do not copy API keys or OAuth tokens into the Docker image.

## Future Scope

### 1. Intelligent Scheduling
- Automatically find available interview slots
- Suggest alternative interview times
- Support rescheduling and cancellation
- Generate Google Meet links

### 2. Email Automation
- Integrate Gmail API
- Send interview reminders
- Track candidate responses
- Generate follow-up and rejection emails with recruiter approval

### 3. Candidate Management
- Resume parsing
- Candidate information extraction
- Job description matching
- Application status tracking

### 4. Multi-Agent Architecture
- Resume Screening Agent
- Interview Scheduling Agent
- Email Communication Agent
- Recruitment Workflow Orchestrator

### 5. Production Deployment
- FastAPI backend
- PostgreSQL database
- Persistent LangGraph memory
- Web dashboard
- CI/CD with GitHub Actions
- Cloud deployment
- Monitoring and audit logs

## Project Status

Working proof of concept with Google Calendar integration and human-in-the-loop scheduling.

## Disclaimer

NovaTech AI Solutions is a fictional company used for demonstration purposes.

