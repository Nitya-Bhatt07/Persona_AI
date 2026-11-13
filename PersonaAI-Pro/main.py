from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import numpy as np
import pickle
import sqlite3

app = FastAPI()

model = pickle.load(open("persona_model.pkl","rb"))

# DB
conn = sqlite3.connect("feedback.db", check_same_thread=False)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS feedback (msg TEXT)")
conn.commit()

details = {
    "Leader": {
        "title":"👑 Leader",
        "desc":"Bold, confident & decision maker",
        "advice":"Practice empathy & patience"
    },
    "Creative": {
        "title":"🎨 Creative",
        "desc":"Innovative & imaginative",
        "advice":"Turn ideas into execution"
    },
    "Analytical": {
        "title":"🧠 Analytical",
        "desc":"Logical & detail-oriented",
        "advice":"Avoid overthinking"
    },
    "Social": {
        "title":"🌟 Social",
        "desc":"Outgoing & energetic",
        "advice":"Take time for yourself"
    },
    "Calm": {
        "title":"🌿 Calm",
        "desc":"Peaceful & balanced",
        "advice":"Step out of comfort zone"
    }
}

@app.get("/")
def home():
    return {"message":"PersonaAI Premium 🚀"}

@app.get("/ui")
def ui():
    return FileResponse("index.html")

@app.get("/predict")
def predict(**kwargs):
    try:
        values = [int(kwargs[f"q{i}"]) for i in range(1,16)]

        if any(v<1 or v>5 for v in values):
            raise HTTPException(400,"Values must be 1-5")

        result = model.predict([values])[0]
        return details[result]

    except Exception as e:
        raise HTTPException(500,str(e))

@app.get("/feedback")
def feedback(msg:str):
    cur.execute("INSERT INTO feedback VALUES (?)",(msg,))
    conn.commit()
    return {"message":"Thank you for your feedback!! ~ From Nitya...😊"}