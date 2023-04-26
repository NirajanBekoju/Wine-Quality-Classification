from rest_framework.views import APIView
from rest_framework.response import Response
from .process import load_model
from django.core.cache import cache
import numpy as np
from .models import WineQuality

# Create your views here.
class ModelPrediction(APIView):
    def scaleAndTransform(self, data, scaler):
        """log transformation and standard scaling"""
        log_data = np.log(data + 0.01)
        return scaler.transform(log_data)
    
    def scaleAndTransform2(self, data, scaler):
        """min max scaling and log transformation"""
        data = scaler.transform(data)
        return np.log(data + 0.0001)

    def post(self, request, format = None):
        data = request.data
        required_keys = ["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", "density", "pH", "sulphates", "alcohol"]

        for key in required_keys:
            if key not in data:
                return Response({"errror" : f"{key} is missing"})

        lr2 = cache.get('lr2')
        scaler2 = cache.get('scaler2')
        min_max_scaler = cache.get('min_max_scaler')
        xgbClassifier = cache.get('xgbClassifier')

        if None in [lr2, scaler2, min_max_scaler, xgbClassifier]:
            load_model()
            # get the cache value again
            lr2 = cache.get('lr2')
            scaler2 = cache.get('scaler2')
            min_max_scaler = cache.get('min_max_scaler')
            xgbClassifier = cache.get('xgbClassifier')

        fixed_acidity =  data["fixed_acidity"]
        volatile_acidity = data["volatile_acidity"]
        citric_acid = data["citric_acid"]
        residual_sugar = data["residual_sugar"] 
        chlorides = data["chlorides"] 
        free_sulfur_dioxide = data["free_sulfur_dioxide"] 
        total_sulfur_dioxide = data["total_sulfur_dioxide"]
        density = data["density"]
        pH = data["pH"]
        sulphates = data["sulphates"] 
        alcohol = data["alcohol"] 

        input_data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
        
        print(input_data)
        try:
            input_data = list(map(float, input_data))
        except ValueError as e:
            return Response({"error":"Not convertible to float"})

        input_data = np.expand_dims(input_data, axis = 0)
        print(input_data)

        """Logistic Regression model"""
        processed_input_data = self.scaleAndTransform(data=input_data, scaler=scaler2)
        lr2_pred = lr2.predict_proba(processed_input_data).flatten()

        """XGBClassifier Model"""
        processed_input_data = self.scaleAndTransform2(data=input_data, scaler=min_max_scaler)
        xgb_pred = xgbClassifier.predict_proba(processed_input_data).flatten()

        print(np.argmax(lr2_pred), np.argmax(xgb_pred))
        # Save the model
        WineQuality.objects.create(
            fixed_acidity = fixed_acidity, 
            volatile_acidity = volatile_acidity, 
            citric_acid = citric_acid, 
            residual_sugar = residual_sugar, 
            chlorides = chlorides, 
            free_sulfur_dioxide = free_sulfur_dioxide, 
            total_sulfur_dioxide = total_sulfur_dioxide, 
            density = density, 
            pH = pH, 
            sulphates = sulphates, 
            alcohol = alcohol, 
            lr_pred = np.argmax(lr2_pred),
            xgb_pred = np.argmax(xgb_pred),
            )

        return Response({"lr2_pred" : lr2_pred, "xgb_pred" : xgb_pred})


