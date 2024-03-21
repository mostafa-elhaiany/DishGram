import json
def draw_ingredients(st):
    with open("Streamlit/Assets/ingredients.json", "r") as f:
        ingredient_list = json.load(f)

    num_cols = 2
    num_rows = (len(ingredient_list) + num_cols - 1) // num_cols - 1
    idx = 0
    for _ in range(num_rows):
        columns = st.columns(num_cols)
        for col in columns:
            if(idx>len(ingredient_list)):
                break
            col.image(ingredient_list[idx]["imageLink"])
            col.write(ingredient_list[idx]["name"])
            idx+=1

