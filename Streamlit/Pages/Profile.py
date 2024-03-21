import matplotlib.pyplot as plt
import numpy as np
import os, json

def generate_bar_plot(data,ylabel, title, color):
    fig = plt.figure(figsize=(10, 5))
    plt.bar(np.arange(len(data)), data, color=color)
    plt.title(title)
    plt.xlabel('Days')
    plt.ylabel(ylabel)
    plt.xticks(np.arange(len(data)), [f'{i} days ago' if i>1 else "yesterday" for i in range(len(data)+1, 1, -1)],rotation=45)
    return fig

def generate_pie():
    labels = 'Protein', 'Carbs', 'Fats',
    sizes = [25, 30, 45]
    explode = (0.02, 0.01, 0.01)

    fig = plt.figure(figsize=(10, 6))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    return fig

def display_images(st, images):
    num_images = len(images)
    rows = (num_images + 2) // 3  # Calculate number of rows needed
    for i in range(rows):
        cols = st.columns(3)  # Create three columns
        for j in range(3):
            index = i * 3 + j
            if index < num_images:
                cols[j].image(images[index], use_column_width=True, caption=f"Image {index+1}")



def handle_images(st, user_json):

    # Upload image button
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    uploaded_images = user_json["posted_images"]
    # If image is uploaded, add it to the list and display
    upload_dir = "Streamlit/Assets/uploaded_images"
    if uploaded_file is not None:
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        new_image_path = os.path.join(upload_dir, uploaded_file.name)
        with open(new_image_path, "wb") as f:
            f.write(uploaded_file.read())

        uploaded_images.append(new_image_path)
        st.success("Image uploaded successfully!")
        print(uploaded_file)
    # Display uploaded images
    if len(uploaded_images) > 0:
        st.write("### Uploaded Images:")
        display_images(st, uploaded_images)
    
    user_json["posted_images"] = uploaded_images
    with open(f"Streamlit/Assets/info/{st.session_state['username']}.json", 'w') as f:
        json.dump(user_json,f)


def draw_profile(st):
    l_corner, title, _, _= st.columns([6,1,6,1])
    try:
        l_corner.image(f"Streamlit/Assets/Images/{st.session_state['username']}.jpeg", width=128)
    except:
        pass
    l_corner.caption(st.session_state["username"])

    title.metric("Score", 60, -10)

    st.divider()
    st.header("Your nutirion dashboard")

    st.toggle("goal mode")

    water_col, calories_col, nutrients_col = st.columns(3)
    water_col.write("your water intake")
    water_plot = generate_bar_plot(np.random.randint(1, 10, 5), "litres", 'Water intake', 'b')
    water_col.pyplot(water_plot)
    water_col.metric("Today's water", 2.5, -np.round(np.random.random(),1)*2)

    calories_col.write("your calorie intake")
    calorie_plot = generate_bar_plot(np.random.randint(1, 10, 5), "calories", 'Calorie intake', 'g')
    calories_col.pyplot(calorie_plot)
    calories_col.metric("Today's calories", np.round(np.random.random(),1)*3000, (np.round(np.random.random(),1)-.5)*500)

    nutrients_col.write("your micronutrients intake")
    pie_plot = generate_pie()
    nutrients_col.pyplot(pie_plot)
    pro, fat, car = nutrients_col.columns(3)
    
    pro.metric("Today's protein", "30%", "-5%")
    fat.metric("Today's fat", "10%", "5%")
    car.metric("Today's carbs", "20%", "0%")

    st.divider()

    json_file_path = f"Streamlit/Assets/info/{st.session_state['username']}.json"
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as f:
            user_json = json.load(f)
    else:
        user_json = {"posted_images":[]}
        with open(json_file_path, 'w') as f:
            json.dump(user_json,f)

    handle_images(st, user_json)
