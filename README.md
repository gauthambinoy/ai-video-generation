# 🎬 AI Video Generator

A simple yet powerful web application that generates videos from text prompts using AI models. This application provides a beautiful, modern interface for users to create videos by simply describing what they want to see.

## ✨ Features

- **Text-to-Video Generation**: Convert text prompts into videos
- **Multiple Styles**: Choose from realistic, artistic, cinematic, and animated styles
- **Variable Duration**: Generate videos from 3 to 10 seconds
- **Real-time Progress**: Live updates during video generation
- **Beautiful UI**: Modern, responsive design with smooth animations
- **Easy Integration**: Ready to integrate with various AI video services

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ai-video-generation
   ```

2. **Install dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Create environment file** (optional):
   ```bash
   cp .env.example .env
   # Edit .env with your API keys if using external services
   ```

4. **Run the application**:
   ```bash
   python3 main.py
   ```

5. **Open your browser** and navigate to:
   ```
   http://localhost:8000
   ```

## 🎯 How to Use

1. **Enter a video description**: Describe what you want to see in your video
   - Example: "A serene sunset over a calm lake with birds flying"

2. **Choose your style**: Select from available video styles
   - Realistic, Artistic, Cinematic, or Animated

3. **Set duration**: Choose video length (3, 5, or 10 seconds)

4. **Generate**: Click the "Generate Video" button and wait for completion

5. **View result**: Your generated video will appear below the form

## 🔧 Architecture

### Backend (FastAPI)
- **main.py**: Core application with video generation endpoints
- **requirements.txt**: Python dependencies
- **Static file serving**: For generated videos and assets

### Frontend
- **index.html**: Beautiful, responsive single-page application
- **Real-time updates**: Progress tracking and status updates
- **Modern UI**: Clean design with smooth animations

## 🤖 AI Model Integration

The application is designed to easily integrate with various AI video generation services:

### Currently Supported (Demo Mode)
- **Simulation Mode**: Demonstrates the complete workflow

### Ready for Integration
- **Hugging Face**: Text-to-video models via Inference API
- **Runway ML**: Professional video generation service
- **Stable Video Diffusion**: Open-source video generation
- **OpenAI**: Future video generation capabilities
- **Replicate**: Various video generation models

### Example Integration (Hugging Face)

```python
# Add to main.py
async def generate_video_with_huggingface(prompt: str, job_id: str):
    API_URL = "https://api-inference.huggingface.co/models/damo-vilab/text-to-video-ms-1.7b"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}
    
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    
    video_filename = f"video_{job_id}.mp4"
    video_path = f"static/videos/{video_filename}"
    
    with open(video_path, "wb") as f:
        f.write(response.content)
    
    return f"/static/videos/{video_filename}"
```

## 📁 Project Structure

```
ai-video-generation/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── static/             # Generated videos and assets
│       ├── videos/         # Generated video files
│       └── images/         # Generated images
├── frontend/
│   └── index.html          # Frontend interface
├── .env.example            # Environment variables template
└── README.md              # This file
```

## 🛠️ Development

### Adding New AI Services

1. **Create a new generation function**:
   ```python
   async def generate_video_with_service(prompt: str, job_id: str):
       # Your integration code here
       pass
   ```

2. **Update the main endpoint**:
   ```python
   @app.post("/api/generate-video")
   async def generate_video(request: VideoRequest):
       # Call your new function
       video_url = await generate_video_with_service(request.prompt, job_id)
   ```

3. **Add required dependencies** to `requirements.txt`

### Customizing the UI

- Edit `frontend/index.html` to modify the interface
- Update CSS styles for different themes
- Add new form fields for additional parameters

## 🔐 Environment Variables

Create a `.env` file with your API keys:

```bash
# Hugging Face
HUGGINGFACE_API_KEY=your_key_here

# OpenAI
OPENAI_API_KEY=your_key_here

# Runway ML
RUNWAY_API_KEY=your_key_here

# Application settings
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

## 📝 API Endpoints

### POST `/api/generate-video`
Generate a video from a text prompt.

**Request Body**:
```json
{
  "prompt": "A beautiful sunset over mountains",
  "duration": 5,
  "style": "cinematic"
}
```

**Response**:
```json
{
  "video_url": "/static/videos/video_123.mp4",
  "job_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "completed",
  "message": "Video generated successfully!"
}
```

### GET `/api/job-status/{job_id}`
Check the status of a video generation job.

**Response**:
```json
{
  "status": "processing",
  "progress": 45,
  "video_url": null,
  "message": "Generating video... 45%"
}
```

## 🚀 Deployment

### Local Development
```bash
python3 main.py
```

### Production (with Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
```

### Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:

1. Check the existing issues
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

## 🔮 Future Enhancements

- [ ] Multiple AI model support
- [ ] Video editing capabilities
- [ ] Batch video generation
- [ ] User authentication
- [ ] Video gallery
- [ ] Advanced styling options
- [ ] Mobile app version
- [ ] Cloud deployment guides

---

**Happy video generating! 🎥✨**