import requests, base64, json
import config

categories = None

def return_categories():
    global categories
    response = requests.get(config.CATEGORIES_API)
    categories = response.json()

def return_nutrients(image_file):
    encoded_string = base64.b64encode(image_file.read())
    payload ={"filename": image_file.name, "filedata": encoded_string}
    response = requests.post(url=config.CALORIES_NUTRIENTS_API, data=payload) 
    return response.json()

def return_fridge_info(image_file):
    encoded_string = base64.b64encode(image_file.read())
    payload ={"filename": image_file.name, "filedata": encoded_string}
    response = requests.post(url=config.FRIDGE_DETECTION_API, data=payload) 
    return response.json()


def get_nutritional_value(query):
    key = config.RECIPE_API 
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': key})
    return json.loads(response.text)

def get_recipe(query):
    key = config.RECIPE_API 
    api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': key})
    return json.loads(response.text)
