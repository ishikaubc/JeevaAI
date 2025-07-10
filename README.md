# JeevaAI
AI for Good Hackathon

Feature 1: Donor Availability Predictor
Collect past donation data
Use Logistic Regression / Random Forest to predict donor likelihood
Output a list of predicted "available donors" based on region & date

Feature 2: AI Care Bot
Chat interface
NLP-based responses on Thalassemia topics (symptoms, nutrition, transfusion)
Use LangChain + OpenAI or Ollama 


To install dependencies:
```bash
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To run server:
```bash
python -m backend.app
```

To open SwaggerUI:
```bash
http://localhost:8000/docs
```