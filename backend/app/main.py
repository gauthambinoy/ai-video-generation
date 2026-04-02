"""AI Video Generation — FastAPI Application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Video Generation Platform",
    description="Text-to-video pipeline with AI storyboarding and voice synthesis",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {"status": "healthy", "version": "1.0.0"}


@app.post("/api/v1/videos")
async def create_video(prompt: str = ""):
    """Create a new video generation job."""
    return {
        "video_id": "placeholder-uuid",
        "status": "queued",
        "prompt": prompt,
    }


@app.get("/api/v1/videos/{video_id}")
async def get_video(video_id: str):
    """Get video status and download link."""
    return {
        "video_id": video_id,
        "status": "processing",
        "progress": 0,
        "download_url": None,
    }


@app.post("/api/v1/storyboard")
async def generate_storyboard(prompt: str = ""):
    """Generate a video storyboard from text."""
    from .services.storyboard import StoryboardGenerator
    gen = StoryboardGenerator()
    scenes = await gen.generate(prompt)
    return {"scenes": [vars(s) for s in scenes]}


@app.get("/api/v1/templates")
async def list_templates():
    """List available video templates."""
    return {
        "templates": [
            {"id": "explainer", "name": "Explainer Video", "duration": 60},
            {"id": "tutorial", "name": "Tutorial", "duration": 120},
            {"id": "short", "name": "YouTube Short", "duration": 30},
        ]
    }
