from utils.Api import return_nutrients, return_categories
import matplotlib.pyplot as plt

def draw_estimate(st):
    st.write("Upload an image and we'll tell you how we estimate nutrients and calories")
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    if(uploaded_file):
        st.image(uploaded_file)
        file_bytes = uploaded_file.read()
        data = return_nutrients(file_bytes)
        categories = return_categories()
        # st.json(data)

        col1, col2 = st.columns(2)

        figure = plt.figure()
        plt.bar([categories[key]['name'] for key in data['distribution'].keys()],data['distribution'].values())
        plt.ylabel("%")
        plt.xticks(rotation=65)
        col1.pyplot(figure)

        figure = plt.figure()
        s = data['estimated_protein_g'] + data['estimated_fat_g'] + data['estimated_carbohydrates_g']
        plt.bar(["protein","fat","carbs"],[data['estimated_protein_g']/s,data['estimated_fat_g']/s,data['estimated_carbohydrates_g']/s])
        col2.pyplot(figure)
        