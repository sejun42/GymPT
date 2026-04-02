# GymPT - AI-Based Posture Analysis & Personalized Coaching System

Real-time bilateral imbalance detection and LLM-assisted feedback for weight training

[![Paper](https://img.shields.io/badge/IEEE-ISMAR%202025-blue)](https://doi.org/10.1109/ISMAR-Adjunct68609.2025.00245)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?logo=flask)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Pose-4285F4?logo=google&logoColor=white)

---

## Overview

GymPT is a web-based system that analyzes exercise posture **in real time** using a single RGB camera. It detects left-right muscular imbalances during weight training, generates per-frame quantitative metrics, and delivers **LLM-powered personalized coaching reports**.
### Key Capabilities

| Feature | Description |
|---|---|
| **Real-time Pose Estimation** | MediaPipe Pose landmark extraction at 30 fps from a single webcam |
| **Bilateral Imbalance Detection** | Vector-based joint angle comparison between left/right limbs per frame |
| **LLM-Assisted Feedback** | OpenAI GPT integration for natural-language coaching reports |
| **Session Logging** | Frame-level data stored in SQLite with automatic report generation |
| **Multi-Exercise Support** | Configurable analysis pipelines for squat, bench press, deadlift, etc. |

## Architecture

```
+---------------+     +------------------+     +----------------+
|  Webcam Feed  |---->|  MediaPipe Pose   |---->| Imbalance      |
|  (Browser)    |     |  Landmark Extract |     | Analysis Engine|
+---------------+     +------------------+     +-------+--------+
                                                       |
                                                       v
                      +------------------+     +----------------+
                      |  OpenAI GPT API  |<----|  Report        |
                      |  (LLM Coaching)  |     |  Generator     |
                      +------------------+     +-------+--------+
                                                       |
                                                       v
                                               +----------------+
                                               |  SQLite DB     |
                                               |  + Visualizer  |
                                               +----------------+
```

## Tech Stack

- Backend: Flask, SQLAlchemy, Flask-Migrate
- - Frontend: HTML/CSS/JavaScript (vanilla)
  - - Pose Estimation: Google MediaPipe Pose
    - - AI Feedback: OpenAI GPT API
      - - Database: SQLite
        - - Deployment: Render (cloud) / local
         
          - ## Getting Started
         
          - ```bash
            # 1. Clone
            git clone https://github.com/sejun42/GymPT.git
            cd GymPT

            # 2. Virtual environment
            python -m venv venv
            source venv/bin/activate
            # Windows: venv\Scripts\activate

            # 3. Install dependencies
            pip install -r requirements.txt

            # 4. Environment variables
            cp .env.example .env
            # Edit .env - set SECRET_KEY, OPENAI_API_KEY

            # 5. Initialize database
            flask db init
            flask db migrate -m "Initial migration"
            flask db upgrade

            # 6. Run
            flask run
            ```

            Open http://localhost:5000 in your browser.

            ## Publication

            AI-Based Posture Analysis and Personalized Feedback System for Weight Training: Real-Time Imbalance Detection and LLM-Assisted Coaching

            Sejun Yoon*, Jeongha Lee, Jae-In Hwang

            *Poster, 2025 IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct 2025)*

            DOI: [10.1109/ISMAR-Adjunct68609.2025.00245](https://doi.org/10.1109/ISMAR-Adjunct68609.2025.00245)

            ## Related Projects

            - [GymPTwebsite](https://github.com/sejun42/GymPTwebsite) - Landing page introducing the GymPT project
            - - [egoGym](https://github.com/sejun42/egoGym) - Early prototype: pose-estimation-based MR fitness program
             
              - ## Contact
             
              - - Sejun Yoon - [sejun1324@gmail.com](mailto:sejun1324@gmail.com)
                - - GitHub: [@sejun42](https://github.com/sejun42)
                  - 
