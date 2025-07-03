import os
import tempfile

import gradio as gr
import torch
from diffusers import TextToVideoZeroPipeline
from diffusers.utils import export_to_video

# Load the text-to-video pipeline (zero-shot).  
# This model is relatively small compared to other video models and works on most modern GPUs.
# If you do not have a CUDA-capable GPU available, the pipeline will automatically run on CPU.
# Video generation on CPU is much slower, but it will still work for short clips.

MODEL_ID = "stabilityai/stable-video-diffusion-img2vid-xt"  # default fallback

try:
    # Prefer a pure text-to-video model if the environment already has it cached.
    MODEL_ID = "runwayml/stable-diffusion-v1-5"  # Text2VideoZero can work with any SD-1.5 ckpt
except Exception:
    pass

device = "cuda" if torch.cuda.is_available() else "cpu"

def load_pipeline():
    """Lazily load the pipeline the first time it is needed."""
    pipe = TextToVideoZeroPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    )

    if torch.cuda.is_available():
        pipe.enable_model_cpu_offload()  # keeps memory usage lower on GPU
    pipe.to(device)
    return pipe


pipe = None  # will be initialised on first request


def generate(prompt: str, num_frames: int = 8, guidance_scale: float = 7.5):
    """Generate a short video from a text prompt and return the video file path."""
    global pipe
    if pipe is None:
        pipe = load_pipeline()

    if not prompt or prompt.strip() == "":
        raise gr.Error("Please enter a descriptive prompt.")

    with torch.autocast(device):
        frames = pipe(prompt=prompt, video_length=num_frames, guidance_scale=guidance_scale).images

    # Save the frames to a temporary MP4 so Gradio can display it.
    video_path = tempfile.mktemp(suffix=".mp4")
    export_to_video(frames, video_path, fps=4)
    return video_path


with gr.Blocks(title="AI Video Generator") as demo:
    gr.Markdown("""
    # Text-to-Video Generator 🚀
    Enter a prompt describing the scene you would like to see and click **Generate**.  
    A short video (≈2 s) will be created with state-of-the-art diffusion models.
    """)

    prompt_box = gr.Textbox(label="Prompt", placeholder="e.g. A panda playing guitar on Times Square", lines=2)
    with gr.Row():
        num_frames_inp = gr.Slider(8, 24, value=8, step=1, label="Number of frames")
        guidance_inp = gr.Slider(1.0, 12.0, value=7.5, step=0.5, label="Guidance scale")

    generate_btn = gr.Button("Generate")
    output_video = gr.Video(label="Generated video", autoplay=True)

    generate_btn.click(fn=generate, inputs=[prompt_box, num_frames_inp, guidance_inp], outputs=output_video)

if __name__ == "__main__":
    demo.launch()