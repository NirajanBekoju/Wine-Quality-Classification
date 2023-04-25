from django.core.cache import cache
import pickle
from xgboost import XGBClassifier

def load_model():
    # Load the machine learning model
    model_path = "classifiers_model/"
    with open(model_path + 'scaler_2.pkl', 'rb') as f:
        print("Loading Standard Scaler 2...")
        scaler2 = pickle.load(f)

    with open(model_path + 'lr_2.pkl', 'rb') as f:
        print("Loading LR2 model...")
        lr2 = pickle.load(f)

    with open(model_path + 'min_max_scaler_boosting.pkl', 'rb') as f:
        print("Min Max Scaler loading...")
        min_max_scaler = pickle.load(f)

    xgbClassifier = XGBClassifier()
    xgbClassifier.load_model(model_path + "xg_boosting_model.pkl")

    # Store the machine learning model in cache
    cache.set('lr2', lr2)
    cache.set('scaler2', scaler2)

    cache.set('min_max_scaler', min_max_scaler)
    cache.set('xgbClassifier', xgbClassifier)

# Load the machine learning model at the start of the Django server
load_model()