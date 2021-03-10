from typing import Optional

from fastapi import FastAPI

from src.twitter.twitter import Twitter

app = FastAPI()

@app.get("/get_followers")
def get_followers():
    twitter = Twitter()
    return twitter.get_followers("poteitosconmojo")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = "birigulillo"):
    return {"item_id": item_id, "q": "birigulillo"}