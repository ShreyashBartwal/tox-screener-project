# ToxScreener: An AI-Powered Preclinical Toxicology Text Classifier

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-blue?style=for-the-badge)

A full-stack web application that uses a fine-tuned transformer model to classify biomedical text for its relevance to preclinical toxicology.

<!-- 
**IMPORTANT:** Add a screenshot or a short GIF of your app working here! 
It's the best way to show what your project does. 
You can use a tool like Giphy Capture or Kap to record your screen.
-->
![ToxScreener Demo](./docs/demo.gif)

**Live Demo:** [Preclinical Toxicology Screener](https://tox-screener-project.vercel.app/)

## About The Project

This project was built to solve a real-world problem for biomedical researchers: rapidly screening large volumes of text (like scientific abstracts or research notes) to identify documents relevant to preclinical toxicology. By automating this process, researchers can save significant time during literature reviews.

The project is a complete end-to-end application, demonstrating the full lifecycle of a modern AI product:

1.  **Data Acquisition & Model Training:** A `distilbert-base-uncased` model was fine-tuned on the `javicorvi/pretoxtm-dataset` using Google Colab for efficient, GPU-accelerated training.
2.  **Backend Development:** A robust API was built with **FastAPI** to serve the trained PyTorch model. It exposes a simple endpoint that accepts text and returns a classification result.
3.  **Frontend Development:** A clean, responsive user interface was created with **React**. The UI allows users to input text and view the model's prediction and confidence score in real-time.
4.  **Version Control & DevOps:** The project is version-controlled with Git. I successfully navigated challenges with large file storage using **Git LFS** and secure development practices by preventing secrets from being committed, thanks to **GitHub Push Protection**.

## Tech Stack

This project uses a modern, industry-standard set of technologies:

*   **Backend:**
    *   Python
    *   FastAPI (for the web server)
    *   Uvicorn (for the ASGI server)
*   **Frontend:**
    *   React.js
    *   HTML/CSS
*   **Machine Learning / Data:**
    *   PyTorch
    *   Hugging Face Transformers (for the model and tokenizer)
    *   Hugging Face Datasets (for data loading)
    *   Scikit-learn (for metrics)
*   **Version Control & Tooling:**
    *   Git & GitHub
    *   Git LFS (for large model file storage)
    *   Visual Studio Code
    *   Google Colab (for model training)

## Features

*   Analyzes any input biomedical text.
*   Classifies text as either `Relevant to Preclinical Toxicology` or `Not Relevant`.
*   Provides a confidence score for each prediction.
*   Simple, intuitive
