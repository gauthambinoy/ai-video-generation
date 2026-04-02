# AI Video Generation Platform

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)

Enterprise-grade AI video generation platform. Text-to-video pipeline with LLM storyboarding, AI voiceover, auto-captioning, and one-click publishing.

## Features

- **Text-to-Video Pipeline** — Describe your video, get a polished result
- **AI Storyboarding** — GPT-4o breaks concepts into scenes with visual descriptions
- **Voice Synthesis** — ElevenLabs premium or edge-tts free fallback
- **Auto-Captioning** — Whisper-powered word-level subtitles
- **Video Assembly** — MoviePy + FFmpeg for professional editing
- **Job Queue** — Celery/Redis with real-time progress tracking
- **Asset Library** — Pexels/Pixabay integration for B-roll

## Architecture

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│    React UI   │────▶│   FastAPI    │────▶│   Workers    │
│  (Vite + TS)  │◀────│   Gateway    │◀────│  (Celery)    │
└──────────────┘     └──────┬───────┘     └──────┬───────┘
                            │                     │
                     ┌──────┴──────┐        ┌─────┴──────┐
                     │   Postgres   │        │   Redis    │
                     └─────────────┘        └────────────┘
```

## Quick Start

```bash
git clone https://github.com/gauthambinoy/ai-video-generation.git
cd ai-video-generation && cp .env.example .env
docker-compose up
```

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/videos` | Create video generation job |
| GET | `/api/v1/videos/{id}` | Get video status + download link |
| GET | `/api/v1/videos/{id}/progress` | SSE real-time progress |
| POST | `/api/v1/storyboard` | Generate storyboard from text |
| GET | `/api/v1/templates` | List video templates |

## License

MIT
