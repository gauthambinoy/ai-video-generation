# AI Video Generator Demo

This repository contains a minimal example of a *text-to-video* application built with
[🤗 Diffusers](https://github.com/huggingface/diffusers) and a Gradio web UI.

The app lets you enter a prompt and produces a short, 2–4 second video that matches your description.

## Quick start

1.  (Optional) Create and activate a Python virtual environment.
2.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Run the Gradio interface:

    ```bash
    python backend/app/main.py
    ```

4.  Open the URL printed in the terminal (by default <http://localhost:7860>) and enter a prompt like
    *"A panda playing guitar on Times Square"*.

---

### Notes

* The default model is **Text2Video-Zero** powered by a Stable Diffusion 1.5 checkpoint.  
  If you have a GPU, the pipeline will automatically use half-precision weights and
  offload parts of the model to CPU to fit in ~8 GB VRAM.
* Video generation on CPU works but is **very** slow. Reduce the number of frames
  or try a smaller model if you do not have a CUDA-capable GPU.
* Feel free to experiment with other checkpoints that are compatible with
  `TextToVideoZeroPipeline` (for example, a DreamBooth SD 1.5 model).  
  Simply set the `MODEL_ID` constant in `backend/app/main.py` to the model ID on
  the Hugging Face hub.