from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load model and tools
model = pickle.load(open("model.pkl", "rb"))
encoder = pickle.load(open("label_encoder.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

app = FastAPI(title="Persona AI")

# Input format (MCQ vector)
class InputData(BaseModel):
    features: list  # MCQ encoded values

@app.get("/")
def home():
    return {"message": "Persona AI is running 🚀"}

@app.post("/predict")
def predict_personality(data: InputData):
    try:
        input_array = np.array(data.features).reshape(1, -1)
        scaled_input = scaler.transform(input_array)

        # Get probabilities (IMPORTANT CHANGE)
        probabilities = model.predict_proba(scaled_input)[0]

        classes = encoder.classes_

        result = dict(zip(classes, probabilities))
        create_pie_chart(result)

        # Final personality
        top_personality = classes[np.argmax(probabilities)]

        return {
            "status": "success",
            "personality": top_personality,
            "breakdown": result
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
        
    

def create_pie_chart(data):
    labels = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(6,6))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Persona AI - Personality Trait Composition")

    plt.savefig("personality_pie.png")
    plt.close()