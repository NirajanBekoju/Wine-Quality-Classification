from django.core.cache import cache
import pickle

def load_model():
    # Load the machine learning model
    model_path = "classifiers_model/"
    with open(model_path + 'lr_1.pkl', 'rb') as f:
        print("Loading model 1...")
        lr1 = pickle.load(f)

    with open(model_path + 'scaler_2.pkl', 'rb') as f:
        print("Loading Standard Scaler 2...")
        scaler2 = pickle.load(f)

    with open(model_path + 'lr_2.pkl', 'rb') as f:
        print("Loading LR2 model...")
        lr2 = pickle.load(f)

    # Store the machine learning model in cache
    cache.set('lr1', lr1)
    cache.set('lr2', lr2)
    cache.set('scaler2', scaler2)

# Load the machine learning model at the start of the Django server
load_model()