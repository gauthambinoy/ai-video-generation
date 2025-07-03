#!/bin/bash

echo "🎬 AI Video Generator - Starting Application"
echo "==========================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Navigate to backend directory
cd backend

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found in backend directory"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install --break-system-packages -r requirements.txt

# Create static directories
echo "📁 Creating static directories..."
mkdir -p static/videos
mkdir -p static/images

# Start the application
echo "🚀 Starting the AI Video Generator..."
echo "📱 Open your browser and go to: http://localhost:8000"
echo "⏹️  Press Ctrl+C to stop the server"
echo ""

python3 main.py