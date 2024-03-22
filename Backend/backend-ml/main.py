from fastapi import File, Form, UploadFile, Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import tensorflow.compat.v2 as tf
import tensorflow_hub as hub

from tensorflow.keras.models import load_model
from tensorflow.keras.utils import get_file 
from tensorflow.keras.utils import load_img 
from tensorflow.keras.utils import img_to_array
from tensorflow import expand_dims
from tensorflow.nn import softmax

from numpy import argmax
from numpy import max
from numpy import array
from json import dumps
from uvicorn import run
import os

from PIL import Image
import numpy as np
import requests
from io import BytesIO
import base64
import sys



app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)

food_categories = {"0": {"name": "background", "calories_lower_bound": 0.0, "calories_upper_bound": 0.0, "protein (g)": 0.0, "fat (g)": 0.0, "carbohydrates (g)": 0.0}, "1": {"name": "vegetables | leafy_greens", "calories_lower_bound": 15.0, "calories_upper_bound": 35.0, "protein (g)": 2.0, "fat (g)": 0.3, "carbohydrates (g)": 3.0}, "2": {"name": "vegetables | stem vegetables", "calories_lower_bound": 15.0, "calories_upper_bound": 40.0, "protein (g)": 2.0, "fat (g)": 0.2, "carbohydrates (g)": 4.0}, "3": {"name": "vegetables | non-starchy roots", "calories_lower_bound": 30.0, "calories_upper_bound": 70.0, "protein (g)": 1.5, "fat (g)": 0.1, "carbohydrates (g)": 12.0}, "4": {"name": "vegetables | other", "calories_lower_bound": 20.0, "calories_upper_bound": 100.0, "protein (g)": 1.0, "fat (g)": 0.5, "carbohydrates (g)": 5.0}, "5": {"name": "fruits", "calories_lower_bound": 30.0, "calories_upper_bound": 90.0, "protein (g)": 0.5, "fat (g)": 0.2, "carbohydrates (g)": 15.0}, "6": {"name": "protein | meat", "calories_lower_bound": 120.0, "calories_upper_bound": 250.0, "protein (g)": 25.0, "fat (g)": 8.0, "carbohydrates (g)": 0.0}, "7": {"name": "protein | poultry", "calories_lower_bound": 100.0, "calories_upper_bound": 200.0, "protein (g)": 20.0, "fat (g)": 5.0, "carbohydrates (g)": 0.0}, "8": {"name": "protein | seafood", "calories_lower_bound": 70.0, "calories_upper_bound": 150.0, "protein (g)": 20.0, "fat (g)": 2.0, "carbohydrates (g)": 0.0}, "9": {"name": "protein | eggs", "calories_lower_bound": 140.0, "calories_upper_bound": 160.0, "protein (g)": 13.0, "fat (g)": 10.0, "carbohydrates (g)": 1.0}, "10": {"name": "protein | beans/nuts", "calories_lower_bound": 120.0, "calories_upper_bound": 500.0, "protein (g)": 20.0, "fat (g)": 10.0, "carbohydrates (g)": 30.0}, "11": {"name": "starches/grains | baked_goods", "calories_lower_bound": 250.0, "calories_upper_bound": 400.0, "protein (g)": 8.0, "fat (g)": 5.0, "carbohydrates (g)": 50.0}, "12": {"name": "starches/grains | rice/grains/cereals", "calories_lower_bound": 100.0, "calories_upper_bound": 370.0, "protein (g)": 7.0, "fat (g)": 1.0, "carbohydrates (g)": 75.0}, "13": {"name": "starches/grains | noodles/pasta", "calories_lower_bound": 85.0, "calories_upper_bound": 130.0, "protein (g)": 5.0, "fat (g)": 1.5, "carbohydrates (g)": 25.0}, "14": {"name": "starches/grains | starchy vegetables", "calories_lower_bound": 70.0, "calories_upper_bound": 150.0, "protein (g)": 2.0, "fat (g)": 0.2, "carbohydrates (g)": 17.0}, "15": {"name": "starches/grains | other", "calories_lower_bound": 100.0, "calories_upper_bound": 400.0, "protein (g)": 8.0, "fat (g)": 5.0, "carbohydrates (g)": 50.0}, "16": {"name": "soups/stews", "calories_lower_bound": 45.0, "calories_upper_bound": 100.0, "protein (g)": 3.0, "fat (g)": 2.0, "carbohydrates (g)": 10.0}, "17": {"name": "herbs/spices", "calories_lower_bound": 20.0, "calories_upper_bound": 400.0, "protein (g)": 10.0, "fat (g)": 5.0, "carbohydrates (g)": 60.0}, "18": {"name": "dairy", "calories_lower_bound": 40.0, "calories_upper_bound": 150.0, "protein (g)": 3.0, "fat (g)": 3.0, "carbohydrates (g)": 5.0}, "19": {"name": "snacks", "calories_lower_bound": 250.0, "calories_upper_bound": 500.0, "protein (g)": 7.0, "fat (g)": 25.0, "carbohydrates (g)": 60.0}, "20": {"name": "sweets/desserts", "calories_lower_bound": 260.0, "calories_upper_bound": 450.0, "protein (g)": 4.0, "fat (g)": 15.0, "carbohydrates (g)": 70.0}, "21": {"name": "beverages", "calories_lower_bound": 0.0, "calories_upper_bound": 60.0, "protein (g)": 0.0, "fat (g)": 0.0, "carbohydrates (g)": 15.0}, "22": {"name": "fats/oils/sauces", "calories_lower_bound": 700.0, "calories_upper_bound": 900.0, "protein (g)": 0.0, "fat (g)": 100.0, "carbohydrates (g)": 0.0}, "23": {"name": "food_containers", "calories_lower_bound": 0.0, "calories_upper_bound": 0.0, "protein (g)": 0.0, "fat (g)": 0.0, "carbohydrates (g)": 0.0}, "24": {"name": "dining_tools", "calories_lower_bound": 0.0, "calories_upper_bound": 0.0, "protein (g)": 0.0, "fat (g)": 0.0, "carbohydrates (g)": 0.0}, "25": {"name": "other_food", "calories_lower_bound": 100.0, "calories_upper_bound": 400.0, "protein (g)": 8.0, "fat (g)": 10.0, "carbohydrates (g)": 50.0}}


food_categories.update({i:food_categories[str(i)] for i in range(0,26)})


m = hub.KerasLayer(
    'https://www.kaggle.com/models/google/mobile-food-segmenter-v1/frameworks/TensorFlow1/variations/seefood-segmenter-mobile-food-segmenter-v1/versions/1',
    output_key="food_group_segmenter:semantic_predictions")



@app.get("/")
async def root():
    headers = {
        'Accept': 'text/plain',
    }
    try:
        response = requests.get('https://icanhazdadjoke.com/', headers=headers)
    except:
        return JSONResponse({"message": "There was an error fetching the joke"},status_code=569)
    return JSONResponse(content=response.json(), status_code=69)

@app.post("/run-model/")
async def run_model(filename: str = Form(...), filedata: str = Form(...)):
    image_as_bytes = str.encode(filedata)  # convert string to bytes
    img_recovered = base64.b64decode(image_as_bytes)
    filename = "uploaded_" + filename + ".jpg"
    
    try:
        with open(filename,"wb") as f:
            f.write(img_recovered)
    except Exception:
        return JSONResponse({"message": "There was an error uploading the file"},status_code=569)
        
    print("File Uploaded")
    try:
        image = Image.open(filename).resize((513, 513)).convert('RGB')
    except:
        return JSONResponse({"message": "There was an error processing the image"},status_code=542)
   
    
    ret_vals = {}
    
    # Resize the image to 513x513 and ensure it's RGB
    image = image.resize((513, 513))
    image = image.convert('RGB')

    # Convert the image to a numpy array and preprocess it for the model
    image = np.array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0  # Normalize the image data to the range [0, 1]

    try:
        array = m(image).numpy()
    except:
        return JSONResponse({"message": "There was an error running the model"},status_code=543)
    #array = np.random.rand(513, 513, 26)
    
    print("Array Shape")
    values = list(np.unique(array))
    distribution = {}
    for v in values:
        distribution[v] = (array==v).sum()
    
    print("Raw Array")
    percentual_distribution = {}
    scale = 1/np.sum(list(distribution.values())[1:23])*100
    for i in range(1,23):
        if i in distribution:
            percentual_distribution[i] = distribution[i]*scale    
    
    print("Percentual Distribution")
    #ret_vals['raw_array'] = array.tolist()
    ret_vals['distribution'] = percentual_distribution
    #ret_vals['categories'] = {i:food_categories[i] for i in range(1,26) if i in percentual_distribution}
    ret_vals['calories_lower_bound'] = sum([food_categories[i]['calories_lower_bound']*percentual_distribution[i] for i in percentual_distribution])
    ret_vals['calories_upper_bound'] = sum([food_categories[i]['calories_upper_bound']*percentual_distribution[i] for i in percentual_distribution])
    ret_vals['estimated_protein_g'] = sum([food_categories[i]['protein (g)']*percentual_distribution[i] for i in percentual_distribution])
    ret_vals['estimated_fat_g'] = sum([food_categories[i]['fat (g)']*percentual_distribution[i] for i in percentual_distribution])
    ret_vals['estimated_carbohydrates_g'] = sum([food_categories[i]['carbohydrates (g)']*percentual_distribution[i] for i in percentual_distribution])
    
    
        
    return JSONResponse(content=ret_vals)

@app.get("/categories/")
def get_categories():
    return JSONResponse(content=food_categories)

@app.post("/fridge/")
def get_fridge(filename: str = Form(...), filedata: str = Form(...)):
    image_as_bytes = str.encode(filedata)  # convert string to bytes
    img_recovered = base64.b64decode(image_as_bytes)  # decode base64string
    filename = "uploaded_" + filename + ".jpg"
    
    try:
        with open(filename, "wb") as f:
            f.write(img_recovered)
    except Exception:
        return JSONResponse({"message": "There was an error uploading the file"},status_code=569)
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    params = {
        "confidence": 0.15,
        'api_key': 'Nu74IoZ68utC9AuEd144',
    }

    data = image_as_bytes

    try:
        result = requests.post('https://detect.roboflow.com/smarterchef/5', params=params, headers=headers, data=data)
    except:
        return JSONResponse({"message": "There was an error processing the image"},status_code=542)
    
    result = result.json()
      
    return JSONResponse(content=result)


if __name__ == "__main__":
    try:
        port = int(os.environ.get('PORT', 5000))
        run(app, host="0.0.0.0", port=port)
    except:
        port = int(os.environ.get('PORT', 5001))
        run(app, host="0.0.0.0", port=port)