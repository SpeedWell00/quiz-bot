# Lab 8 - Task 1

Here is my setup for Task 1. It's a simple web service using **FastAPI**.

Basically, I created a single GET endpoint that returns a greeting message. I also hooked up `uv` to manage the packages, plus added **Ruff** (for linting) and **pytest** so the code stays clean and actually works.

### How to run it

First, grab the dependencies:
```bash
uv sync