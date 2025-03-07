def load_model():
    return pipeline("text-generation", model="distilgpt2")