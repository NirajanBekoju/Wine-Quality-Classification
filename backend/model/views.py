from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .process import load_model
from django.core.cache import cache
import numpy as np

# Create your views here.
class ModelPrediction(APIView):
    def scaleAndTransform(self, data, scaler):
        log_data = np.log(data + 0.01)
        return scaler.transform(log_data)

    def post(self, request, format = None):
        data = request.data
        required_keys = ["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", "density", "pH", "sulphates", "alcohol"]

        for key in required_keys:
            if key not in data:
                return Response({"errror" : f"{key} is missing"})

        lr2 = cache.get('lr2')
        scaler2 = cache.get('scaler2')

        if lr2 == None or scaler2 == None:
            load_model()
            lr2 = cache.get('lr2')
            scaler2 = cache.get('scaler2')


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
        processed_input_data = self.scaleAndTransform(data=input_data, scaler=scaler2)
        pred = lr2.predict_proba(processed_input_data)
        print(pred)
        return Response({"lr2_pred" : pred})


