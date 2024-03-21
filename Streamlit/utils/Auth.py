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
    with open("Streamlit/Assets/credentials/creds.json", "r") as f:
        credentials = json.load(f)
    credentials[username]=password
    with open("Streamlit/Assets/credentials/creds.json", "w") as f:
        json.dump(credentials, f)
