import json

def load_documents(path):

    with open(path) as f:
        return json.load(f)
