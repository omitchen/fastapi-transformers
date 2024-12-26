# fastapi-transformers

## Project Features
This project is a text classification API built on FastAPI and Transformers. It utilizes a pre-trained sentiment analysis model to classify the input text and returns the corresponding label and confidence score.

## Installation Instructions
1. Clone the project to your local machine:
   ```bash
   git clone https://github.com/yourusername/fastapi-transformers.git
   cd fastapi-transformers
   ```

2. Create and activate a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```
   or
   ```bash
   poetry shell
   ```

3. Install dependencies:
   ```bash
   pip install poetry
   poetry install
   ```

## How to Run
Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

This will start the server, and you can access the API at `http://127.0.0.1:8000`.

## API Documentation
The API documentation is available at `http://127.0.0.1:8000/docs`.

## API Usage
To use the API, send a POST request to `http://127.0.0.1:8000/classify/` with the text you want to classify in the request body.


