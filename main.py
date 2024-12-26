from transformers import pipeline
from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

text_classifier = pipeline("sentiment-analysis")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/classify/")
def classify_text(text: str):
    """
    文本分类接口
    参数：
        - text: 输入文本
    """
    try:
        result = text_classifier(text)
        return {"label": result[0]["label"], "score": result[0]["score"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
