import json
def authenticate(username, password):
    with open("Streamlit/Assets/credentials/creds.json", "r") as f:
        credentials = json.load(f)
    try:
        password_gt = credentials[username]
        if(password == password_gt):
            return True, "Success"
        else:
            return False, "Wrong password"
    except KeyError:
        return False, "Username does not exist"

def name_exists(username):
    with open("Streamlit/Assets/credentials/creds.json", "r") as f:
        credentials = json.load(f)
    return username in credentials

def append_user(username, password):
    new_user = {
    "posted_images": [], 
    "calories": [], 
    "today_calorie": 0, 
    "waters":[],
    "today_water":0,
    "protiens":[],
    "today_protein":0,
    "fats":[],
    "today_fat":0,
    "carbs":[],
    "today_carbs":0,
    "meals": []
    }
    with open("Streamlit/Assets/credentials/creds.json", "r") as f:
        credentials = json.load(f)
    credentials[username]=password
    with open("Streamlit/Assets/credentials/creds.json", "w") as f:
        json.dump(credentials, f)
    with open(f"Streamlit/Assets/info/{username}.json", "w") as f:
        json.dump(new_user, f)
