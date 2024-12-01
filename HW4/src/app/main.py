from fastapi import FastAPI
from typing import Union
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Jinsong Liu"}

@app.get("/uni/{uni_id}")
def read_item(uni_id: str, q: Union[str, None] = None):
    return {"uni_id": uni_id, "q": q}
