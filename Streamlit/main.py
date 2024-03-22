import sys
import os

def find_project_root():
    current_path = os.path.abspath(__file__)  # Get the absolute path of the current script
    while True:
        if os.path.isdir(os.path.join(current_path, 'Streamlit')):
            return current_path
        # Move up one directory level
        current_path = os.path.dirname(current_path)
        # Break the loop if we've reached the root directory
        if current_path == os.path.dirname(current_path):
            break
    # If we reach here, no marker was found, so return None or handle appropriately
    return None

# Example usage:
project_root = find_project_root()
if project_root:
    print("Found project root at:", project_root)
else:
    print("Unable to locate project root.")
sys.path.append(project_root)


import streamlit as st


from utils.Auth import authenticate, name_exists, append_user

from Components import Sidebar
from Pages import Home, About, Create, Personalization, Ingredients, Profile, Recommend

def main():
    l_corner, title, _, r_corner= st.columns([6,1,6,1])
    l_corner.image("Streamlit/Assets/Images/logo.png", width=128)
    r_corner.image("Streamlit/Assets/Images/logo.png", width=128)
    title.title("DishGram")
    st.divider()
        # If user is logged in, display welcome message and logout button
    if 'username' in st.session_state:
        st.sidebar.title(f"Welcome, {st.session_state['username']}!")

        page, tags = Sidebar.draw_sidebar(st)
        if page == "Profile":
            Profile.draw_profile(st)
        elif page == "Recommend":
            Recommend.draw_recommend(st)
        elif page == "Home":
            Home.draw_home(st, tags)
        elif page == "About":
            About.draw_about(st)
        elif page == "Ingredients":
            Ingredients.draw_ingredients(st)
        elif page == "Create":
            Create.draw_create(st)
        elif page == "Personalize":
            Personalization.draw_personalize(st)

        # Logout button
        if st.sidebar.button("Logout"):
            st.session_state.pop('username')

    # If user is not logged in, display login form
    else:
        _, c,_ = st.columns(3)
        new_here = c.toggle("New here?")
        if(not new_here):
            c.header("Make sure to log in first")
            # st.divider()
            # st.sidebar.title("Login")
            username = c.text_input("Username")
            password = c.text_input("Password", type='password')

            _, c1,_ = st.columns([3.5, 1, 3])
            login_button = c1.button("Login")

            if login_button:
                status, message = authenticate(username, password)
                if status:
                    st.session_state['username'] = username
                else:
                    st.error(message)
        else:
            c.header("Create an account here")
            username = c.text_input("Username")
            password = c.text_input("Password", type='password')

            _, c1,_ = st.columns([3.5, 1, 3])
            login_button = c1.button("sign up")

            if login_button:
                if(name_exists(username)):
                    st.error("Username already exists!")
                else:
                    append_user(username, password)
                    st.session_state['username'] = username
                    

            


if __name__ == "__main__":
    main()
