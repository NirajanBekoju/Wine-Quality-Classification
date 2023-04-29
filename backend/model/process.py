from django.core.cache import cache
import pickle
from xgboost import XGBClassifier
import numpy as np


## load the scaler and models
model_path = "classifiers_model/"
with open(model_path + 'robust_scaler.pkl', 'rb') as f:
  robust_scaler = pickle.load(f)

with open(model_path + 'best_rf_model.pkl', 'rb') as f:
  best_rf_model = pickle.load(f)

with open(model_path + 'best_svc_model.pkl', 'rb') as f:
  best_svc_model = pickle.load(f)


with open(model_path + 'scaler_2.pkl', 'rb') as f:
    print("Loading Standard Scaler 2...")
    standard_scaler = pickle.load(f)

with open(model_path + 'lr_2.pkl', 'rb') as f:
    print("Loading LR2 model...")
    lr2 = pickle.load(f)

with open(model_path + 'min_max_scaler_boosting.pkl', 'rb') as f:
    print("Min Max Scaler loading...")
    min_max_scaler = pickle.load(f)

xgbClassifier = XGBClassifier()
xgbClassifier.load_model(model_path + "xg_boosting_model.pkl")

## Scale and Transform function
def standardScaleAndTransform(data, scaler):
    """log transformation and standard scaling"""
    log_data = np.log(data + 0.01)
    return scaler.transform(log_data)
    
def minmaxScaleAndTransform2(data, scaler):
    """min max scaling and log transformation"""
    data = scaler.transform(data)
    return np.log(data + 0.0001)

def robustScaleAndTransform(data, scaler):
  data = np.log(data + 0.0001)
  return scaler.transform(data)   

def predict(data):
    result = {}

    data = np.expand_dims(data, axis = 0)
    # standard scaling and logistic regression prediction
    standard_scaled_data = standardScaleAndTransform(data=data, scaler=standard_scaler)
    result["lr2_pred"] = lr2.predict_proba(standard_scaled_data).flatten()

    # min max scaling and xgbClassifier prediction
    minmax_scaled_data = minmaxScaleAndTransform2(data=data, scaler=min_max_scaler)
    result["xgb_pred"] = xgbClassifier.predict_proba(minmax_scaled_data).flatten()

    # Robust scaling => random forest and svc prediction
    robust_scaled_data = robustScaleAndTransform(data, scaler = robust_scaler)
    result["rf_pred"] = best_rf_model.predict_proba(robust_scaled_data).flatten()
    result["svc_pred"] = best_svc_model.predict_proba(robust_scaled_data).flatten()
    return result, [np.argmax(result["lr2_pred"]), np.argmax(result["xgb_pred"]), np.argmax(result["rf_pred"]), np.argmax(result["svc_pred"])]
