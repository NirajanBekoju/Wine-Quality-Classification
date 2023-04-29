from rest_framework.views import APIView
from rest_framework.response import Response
from .process import predict
from django.core.cache import cache
import numpy as np
from .models import WineQuality

# Create your views here.
class ModelPrediction(APIView):
    

    def post(self, request, format = None):
        data = request.data
        required_keys = ["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", "density", "pH", "sulphates", "alcohol"]

        for key in required_keys:
            if key not in data:
                return Response({"errror" : f"{key} is missing"})

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

        result, prediction = predict(input_data)
        lr_pred, xgb_pred, rf_pred, svm_pred = prediction

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
            lr_pred = lr_pred,
            xgb_pred = xgb_pred,
            rf_pred = rf_pred, 
            svm_pred = svm_pred
            )

        return Response(result)


