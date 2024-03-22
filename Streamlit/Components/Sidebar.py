

def draw_sidebar(st):
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Profile","Estimate","Recommend","Home", "Create", "Personalize" ,"About", "Ingredients"])
    st.sidebar.title("")

    st.sidebar.title("Preferences")
    tags = st.sidebar.multiselect(
        "Select tags:",
        ["Vegan", "Vegetarian", "Gluten-free", "Lactose-free","Soup", "Dessert", "Baked"]
    )
    return page, tags