import requests
from PIL import Image
import json

import pprint

pp = pprint.PrettyPrinter(indent=4)

food_categories = {
    "0": {
        "name": "background",
        "calories_lower_bound": 0,
        "calories_upper_bound": 0,
        "protein (g)": 0.0,
        "fat (g)": 0.0,
        "carbohydrates (g)": "0"
    },
    "1": {
        "name": "vegetables | leafy_greens",
        "calories_lower_bound": 15,
        "calories_upper_bound": 35,
        "protein (g)": 2.0,
        "fat (g)": 0.3,
        "carbohydrates (g)": "3"
    },
    "2": {
        "name": "vegetables | stem vegetables",
        "calories_lower_bound": 15,
        "calories_upper_bound": 40,
        "protein (g)": 2.0,
        "fat (g)": 0.2,
        "carbohydrates (g)": "4"
    },
    "3": {
        "name": "vegetables | non-starchy roots",
        "calories_lower_bound": 30,
        "calories_upper_bound": 70,
        "protein (g)": 1.5,
        "fat (g)": 0.1,
        "carbohydrates (g)": "12"
    },
    "4": {
        "name": "vegetables | other",
        "calories_lower_bound": 20,
        "calories_upper_bound": 100,
        "protein (g)": 1.0,
        "fat (g)": 0.5,
        "carbohydrates (g)": "5"
    },
    "5": {
        "name": "fruits",
        "calories_lower_bound": 30,
        "calories_upper_bound": 90,
        "protein (g)": 0.5,
        "fat (g)": 0.2,
        "carbohydrates (g)": "15"
    },
    "6": {
        "name": "protein | meat",
        "calories_lower_bound": 120,
        "calories_upper_bound": 250,
        "protein (g)": 25.0,
        "fat (g)": 8.0,
        "carbohydrates (g)": "0"
    },
    "7": {
        "name": "protein | poultry",
        "calories_lower_bound": 100,
        "calories_upper_bound": 200,
        "protein (g)": 20.0,
        "fat (g)": 5.0,
        "carbohydrates (g)": "0"
    },
    "8": {
        "name": "protein | seafood",
        "calories_lower_bound": 70,
        "calories_upper_bound": 150,
        "protein (g)": 20.0,
        "fat (g)": 2.0,
        "carbohydrates (g)": "0"
    },
    "9": {
        "name": "protein | eggs",
        "calories_lower_bound": 140,
        "calories_upper_bound": 160,
        "protein (g)": 13.0,
        "fat (g)": 10.0,
        "carbohydrates (g)": "1"
    },
    "10": {
        "name": "protein | beans/nuts",
        "calories_lower_bound": 120,
        "calories_upper_bound": 500,
        "protein (g)": 20.0,
        "fat (g)": 10.0,
        "carbohydrates (g)": "30"
    },
    "11": {
        "name": "starches/grains | baked_goods",
        "calories_lower_bound": 250,
        "calories_upper_bound": 400,
        "protein (g)": 8.0,
        "fat (g)": 5.0,
        "carbohydrates (g)": "50"
    },
    "12": {
        "name": "starches/grains | rice/grains/cereals",
        "calories_lower_bound": 100,
        "calories_upper_bound": 370,
        "protein (g)": 7.0,
        "fat (g)": 1.0,
        "carbohydrates (g)": "75"
    },
    "13": {
        "name": "starches/grains | noodles/pasta",
        "calories_lower_bound": 85,
        "calories_upper_bound": 130,
        "protein (g)": 5.0,
        "fat (g)": 1.5,
        "carbohydrates (g)": "25"
    },
    "14": {
        "name": "starches/grains | starchy vegetables",
        "calories_lower_bound": 70,
        "calories_upper_bound": 150,
        "protein (g)": 2.0,
        "fat (g)": 0.2,
        "carbohydrates (g)": "17"
    },
    "15": {
        "name": "starches/grains | other",
        "calories_lower_bound": 100,
        "calories_upper_bound": 400,
        "protein (g)": 8.0,
        "fat (g)": 5.0,
        "carbohydrates (g)": "50"
    },
    "16": {
        "name": "soups/stews",
        "calories_lower_bound": 45,
        "calories_upper_bound": 100,
        "protein (g)": 3.0,
        "fat (g)": 2.0,
        "carbohydrates (g)": "10"
    },
    "17": {
        "name": "herbs/spices",
        "calories_lower_bound": 20,
        "calories_upper_bound": 400,
        "protein (g)": 10.0,
        "fat (g)": 5.0,
        "carbohydrates (g)": "60"
    },
    "18": {
        "name": "dairy",
        "calories_lower_bound": 40,
        "calories_upper_bound": 150,
        "protein (g)": 3.0,
        "fat (g)": 3.0,
        "carbohydrates (g)": "5"
    },
    "19": {
        "name": "snacks",
        "calories_lower_bound": 250,
        "calories_upper_bound": 500,
        "protein (g)": 7.0,
        "fat (g)": 25.0,
        "carbohydrates (g)": "60"
    },
    "20": {
        "name": "sweets/desserts",
        "calories_lower_bound": 260,
        "calories_upper_bound": 450,
        "protein (g)": 4.0,
        "fat (g)": 15.0,
        "carbohydrates (g)": "70"
    },
    "21": {
        "name": "beverages",
        "calories_lower_bound": 0,
        "calories_upper_bound": 60,
        "protein (g)": 0.0,
        "fat (g)": 0.0,
        "carbohydrates (g)": "15"
    },
    "22": {
        "name": "fats/oils/sauces",
        "calories_lower_bound": 700,
        "calories_upper_bound": 900,
        "protein (g)": 0.0,
        "fat (g)": 100.0,
        "carbohydrates (g)": "0"
    },
    "23": {
        "name": "food_containers",
        "calories_lower_bound": 0,
        "calories_upper_bound": 0,
        "protein (g)": 0.0,
        "fat (g)": 0.0,
        "carbohydrates (g)": "0"
    },
    "24": {
        "name": "dining_tools",
        "calories_lower_bound": 0,
        "calories_upper_bound": 0,
        "protein (g)": 0.0,
        "fat (g)": 0.0,
        "carbohydrates (g)": "0"
    },
    "25": {
        "name": "other_food",
        "calories_lower_bound": 100,
        "calories_upper_bound": 400,
        "protein (g)": 8.0,
        "fat (g)": 10.0,
        "carbohydrates (g)": "50"
    }
}


for category in food_categories:
    food_categories[category]['calories_lower_bound'] = float(food_categories[category]['calories_lower_bound'])
    food_categories[category]['calories_upper_bound'] = float(food_categories[category]['calories_upper_bound'])
    food_categories[category]['protein (g)'] = float(food_categories[category]['protein (g)'])
    food_categories[category]['fat (g)'] = float(food_categories[category]['fat (g)'])
    food_categories[category]['carbohydrates (g)'] = float(food_categories[category]['carbohydrates (g)'])


json.dump(food_categories, open("food_categories.json", "w"))
food_categories.update({i:food_categories[str(i)] for i in range(0,26)})

ret_vals = {}   
percentual_distribution = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
for i in range(0, 26):
    if 'calories_lower_bound' not in food_categories[i]:
        print(food_categories[i])
ret_vals['calories_lower_bound'] = sum([food_categories[i]['calories_lower_bound'] for i in percentual_distribution])
ret_vals['calories_upper_bound'] = sum([food_categories[i]['calories_upper_bound'] for i in percentual_distribution])
ret_vals['estimated_protein_g'] = sum([food_categories[i]['protein (g)'] for i in percentual_distribution])
ret_vals['estimated_fat_g'] = sum([food_categories[i]['fat (g)'] for i in percentual_distribution])
ret_vals['estimated_carbohydrates_g'] = sum([food_categories[i]['carbohydrates (g)'] for i in percentual_distribution])

a = Image.open("in_spaghetti.jpg").resize((513, 513)).convert('RGB')
print(a)


image_url = "https://t3.ftcdn.net/jpg/01/09/75/90/240_F_109759077_SVp62TBuHkSn3UsGW4dBOm9R0ALVetYw.jpg"

# load image
image = requests.get(image_url)
with open("spaghetti.jpg", "wb") as f:
    f.write(image.content)
    
# send image to API
url = "https://asdfasdf.greensmoke-c88d1752.switzerlandnorth.azurecontainerapps.io/run-model/"
files = {"file": open("spaghetti.jpg", "rb")}
response = requests.get(url, files=files)
pp.pprint(response.json())

url = "https://asdfasdf.greensmoke-c88d1752.switzerlandnorth.azurecontainerapps.io/categories/"

response = requests.get(url)
pp.pprint(response.json())

import matplotlib
