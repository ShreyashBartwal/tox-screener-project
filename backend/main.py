from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Initialize FastAPI app
app = FastAPI()

# Allow Cross-Origin Resource Sharing (CORS) for your React app
origins = [
    # For local development
    "http://localhost:5173",
    
    # For the Vercel production and preview URLs
    "https://tox-screener-project-2hloaymsz-shreyashbartwals-projects.vercel.app",
    "https://tox-screener-project.vercel.app"  # Corrected: removed trailing slash
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Load the fine-tuned model and tokenizer
MODEL_DIR = "./model"
model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Define the input data structure
class RequestText(BaseModel):
    text: str

# Define the prediction endpoint
@app.post("/predict")
def predict(request: RequestText):
    inputs = tokenizer(request.text, return_tensors="pt", truncation=True, padding=True).to(device)
    
    with torch.no_grad():
        logits = model(**inputs).logits
        
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    confidence = torch.max(probabilities).item()
    predicted_class_id = torch.argmax(logits, dim=-1).item()
    
    # Your label mapping from the notebook: {1: "PRETOX_REL", 0: "NO_PRETOX_REL"}
    prediction = "Relevant to Preclinical Toxicology" if predicted_class_id == 1 else "Not Relevant"
    
    return {"prediction": prediction, "confidence": confidence}

@app.get("/")
def root():
    return {"message": "ToxScreener API is online"}
