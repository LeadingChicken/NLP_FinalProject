from fastapi import FastAPI
from pydantic import BaseModel
from similarity import compute_similarity

class UserInput(BaseModel):
    eng_sent: str
    vie_sent: str

app = FastAPI()

@app.post("/calculate")
def operate(input:UserInput):
    result = compute_similarity(input.eng_sent, input.vie_sent)
    return result