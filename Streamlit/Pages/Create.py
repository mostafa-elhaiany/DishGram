import requests, config, json
from utils.Api import get_nutritional_value, get_recipe

def json_to_markdown(json_data):
    markdown_text = ""
    for key, value in json_data.items():
        markdown_text += f"### {key}\n\n"
        markdown_text += f"{value}\n"
    return markdown_text


def draw_create(st):
    search_bar, _ = st.columns(2)
    recipe = search_bar.text_input("What recipe are you looking for?")
    st.divider()
    if(len(recipe)==0):
        st.write("please insert a search query")
    elif(len(recipe)!=0):
        returned_json = get_recipe(recipe)
        if(len(returned_json)==0):
            st.write("Unfortunatly we couldn't find anything. Are you sure you wrote it correclty?")
        else:
            selected_object = st.selectbox("Select Recipe", returned_json, format_func=lambda x: f"{x['title']}")
            if(selected_object):
                MD = json_to_markdown(selected_object)
            else:
                MD = json_to_markdown(returned_json[0])
            st.markdown(MD)
            st.divider()
            st.title("AI outputs")
            col1, col2 = st.columns(2)
            col1.title("Structured Ingredients and Instructions")
            col1.code("""
                {
                "ingredients": [
                    "1/2 cup Sherry",
                    "4 Cloves garlic",
                    "6 tablespoons Soy sauce",
                    "2 teaspoons Plum sauce",
                    "2 tablespoons Black bean paste",
                    "6 tablespoons Hoisin sauce",
                    "2 teaspoons Salt",
                    "1 1/2 teaspoons Chinese 5-spice",
                    "1/2 cup Sugar"
                ],
                "servings": "13 Servings",
                "instructions": [
                    "Mix together well.",
                    "Heat in a double boiler - add cornstarch for thickening."
                ]
                }
            """)
            col2.title("Ordered prompts for text2video generation")
            col2.code("""
            {
            "prompts": [
            "Create a video demonstrating the gathering of ingredients for the sauce, including sherry, garlic, soy sauce, plum sauce, black bean paste, hoisin sauce, salt, Chinese 5-spice, and sugar.",
            "Produce a video showcasing the process of mixing the ingredients together thoroughly.",
            "Generate a video presenting the quantity of servings the sauce recipe yields (13 servings).",
            "Create a video illustrating the heating of the sauce in a double boiler.",
            "Produce a video demonstrating the addition of cornstarch to the sauce for thickening.",
            "Generate a video summarizing the steps of preparing the sauce, highlighting key ingredients and the thickening process.",
            "Create a video showcasing the final appearance and consistency of the sauce in a serving container.",
            "Produce a video offering serving suggestions or pairings for the sauce, if applicable."
            ]
            }            
            """)
            st.title("Nutritional Value")
            nutrition = get_nutritional_value(recipe)
            if(len(nutrition)>0):
                for item in nutrition:
                    st.code(item)
            else:
                st.write("Unfortunatly our database doesn't have data on that yet.")
                st.write("But fret not! We're working on it.")
                
            st.divider()
            st.title("Ai generated video")
            st.video("Streamlit/Assets/Videos/video9.mp4")

