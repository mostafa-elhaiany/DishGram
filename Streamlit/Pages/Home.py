import json
from numpy import random

def __filter(full_list, user_preferences):

    select_list = random.choice(full_list, 5, replace=False)

    if(len(user_preferences)==0):
        return select_list
    filtered_objects = [obj for obj in select_list if any(tag in user_preferences for tag in obj.get('tags', []))]
    return filtered_objects


def display_local_video_grid(st, json_list, tags):

    filtered_list = __filter(json_list, tags)
    if(len(filtered_list)==0):
        st.write("Unfortunalty no posts right now")
        return
    # Calculate the number of rows needed in the grid
    num_cols = 1
    num_rows = (len(json_list) + num_cols - 1) // num_cols
    # Create a grid layout
    for row in range(num_rows):
        cols = st.columns(num_cols)
        for col in range(num_cols):
            index = row * num_cols + col
            if index < len(filtered_list):
                path = filtered_list[index]["path"]
                file = open(path, 'rb')
                file_bytes = file.read()
                if(path[-4:]==".mp4"):
                    cols[col].video(file_bytes)
                else:
                    cols[col].image(file_bytes, width=512)
                
            else:
                break


def draw_home(st, tags):
    st.title("For you page")
    st.write("The community's selected posts")  

    st.divider()

    with open("Streamlit/Assets/foryou.json", "r") as f:
        json_file = json.load(f)

    display_local_video_grid(st,json_file,tags)
