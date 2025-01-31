from transformers import pipeline

def analyze_depression(text):
    """
    Analyze depression using a pre-trained NLP model.
    """
    classifier = pipeline("text-classification", model="distilbert-base-uncased")
    result = classifier(text)
    return result