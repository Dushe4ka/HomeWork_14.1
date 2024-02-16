import os
import json

def load_data():
    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
    PATH = os.path.join(ROOT_DIR, 'data', 'products.json')
    with open(PATH, encoding='UTF-8') as f:
        data = json.load(f)
        return data