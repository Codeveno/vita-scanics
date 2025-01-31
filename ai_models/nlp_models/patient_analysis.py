from transformers import pipeline

def analyze_patient_text(text):
    """
    Analyze patient text using a pre-trained NLP model.
    """
    classifier = pipeline("text-classification", model="distilbert-base-uncased")
    result = classifier(text)
    return result