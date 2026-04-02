# GymPT — AI-Based Posture Analysis and Personalized Coaching System

> Real-time exercise posture analysis, bilateral imbalance tracking, session logging, and LLM-assisted feedback for strength training

[![Paper](https://img.shields.io/badge/IEEE-ISMAR%202025-blue)](https://doi.org/10.1109/ISMAR-Adjunct68609.2025.00245)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?logo=flask)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Pose-4285F4?logo=google&logoColor=white)

---

## Overview

GymPT is a Flask-based fitness analysis platform built around the idea that left-right movement imbalance can be measured, stored, visualized, and turned into actionable coaching.

The project combines a browser-based workout interface, posture analysis logic, user/session management, chart-based review pages, and optional OpenAI-powered narrative feedback. It sits between a research prototype and a deployable training tool, with both local execution and Render deployment configuration included in the repository.

## What the App Covers

| Area | Details |
| --- | --- |
| Authentication | Sign-up and login flows for individual users |
| Exercise flows | Guided pages for squat, incline press, shoulder press, and related variations |
| Analysis | Per-session imbalance metrics, diagnostic summaries, and chart views |
| Storage | SQLite-backed user and exercise records via SQLAlchemy |
| Feedback | Optional OpenAI-generated text coaching |
| Media handling | Static demo assets plus optional Cloudflare R2 upload flow for videos |
| Deployment | `render.yaml` included for cloud deployment |

## Application Flow

```text
User Login / Signup
        |
        v
Exercise Selection Page
        |
        v
Workout Page (camera / exercise-specific flow)
        |
        v
Metric Logging + Session Save
        |
        +--> Analysis Dashboard (charts, imbalance trends)
        |
        +--> Ranking / history views
        |
        `--> Optional LLM coaching summary
```

## Repository Layout

```text
GymPT/
|- app.py                         # Main Flask app, routes, charts, session logic
|- storage.py                     # Cloudflare R2 upload helper
|- config.py                      # App configuration
|- requirements.txt               # Python dependencies
|- render.yaml                    # Render deployment config
|- migrations/                    # Flask-Migrate / Alembic migration files
|- templates/
|  |- index.html                  # Login / landing
|  |- signup.html                 # Registration
|  |- select.html                 # Exercise selection
|  |- squat.html                  # Lower-body analysis flow
|  |- inclinepress.html           # Press variation flow
|  |- shoulderpress.html          # Shoulder press flow
|  `- anal.html                   # Analysis view
|- static/
|  |- images/                     # UI assets
|  `- videos/3DexerciseVIdeo/     # Exercise guide videos
`- scripts/
   `- upload_guide_videos.py      # Media upload helper
```

## Implementation Notes

### Flask application

`app.py` currently contains most of the product logic:

- authentication and session handling
- exercise routing
- workout result storage
- ranking and scoring
- analysis-page rendering with Plotly charts
- image, QR, and utility flows

### Data model

The current schema stores:

- users
- exercise metadata such as count, set, weight, and duration
- imbalance-related measurements
- serialized log data for charting
- optional uploaded video URLs

### Storage and deployment

The repository includes:

- local SQLite development support
- Flask-Migrate migrations
- Render deployment settings
- optional Cloudflare R2 upload support through environment variables

## Tech Stack

- Python 3.10+
- Flask, Flask-SQLAlchemy, Flask-Migrate
- SQLite
- MediaPipe
- Plotly
- OpenAI API
- Cloudflare R2 (optional)
- Render

## Getting Started

### Install

```bash
git clone https://github.com/sejun42/GymPT.git
cd GymPT
python -m venv venv
source venv/bin/activate
# Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Environment variables

Set the variables you need before running:

- `OPENAI_API_KEY` for LLM feedback
- `R2_ACCOUNT_ID`
- `R2_ACCESS_KEY`
- `R2_SECRET_KEY`
- `R2_BUCKET_NAME`
- `R2_PUBLIC_URL`

If you only want local development without AI or cloud uploads, the core app can still run with a simpler environment.

### Database setup

```bash
flask db upgrade
```

If you are starting from scratch and need a new migration flow:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Run locally

```bash
flask run
```

Open `http://localhost:5000`.

## Research Output

**AI-Based Posture Analysis and Personalized Feedback System for Weight Training: Real-Time Imbalance Detection and LLM-Assisted Coaching**

Sejun Yoon, Jeongha Lee, Jae-In Hwang

Poster, IEEE ISMAR-Adjunct 2025

DOI: [10.1109/ISMAR-Adjunct68609.2025.00245](https://doi.org/10.1109/ISMAR-Adjunct68609.2025.00245)

## Related Projects

- [egoGym](https://github.com/sejun42/egoGym) — earlier pose-estimation prototype
- [GymPTwebsite](https://github.com/sejun42/GymPTwebsite) — landing page for the project

## Contact

- Sejun Yoon — [sejun1324@gmail.com](mailto:sejun1324@gmail.com)
- GitHub — [@sejun42](https://github.com/sejun42)
