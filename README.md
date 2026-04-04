# AI Video Generation

Backend service for AI-powered video content creation — scriptwriting, scene composition, voiceover synthesis, and rendering.

[![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python)](https://python.org)

## Overview

Modular pipeline that takes a topic or prompt and produces a fully rendered short-form video:

1. **Script Generation** — Structured narrative from a topic prompt
2. **Scene Planning** — Break script into visual scenes with timing
3. **Asset Generation** — Create or source visuals for each scene
4. **Voiceover** — Text-to-speech synthesis with natural pacing
5. **Rendering** — Composite final video with transitions and captions

## Getting Started

```bash
git clone https://github.com/gauthambinoy/ai-video-generation.git
cd ai-video-generation/backend
pip install -r requirements.txt
cp .env.example .env
python -m app.main
```

## License

MIT
