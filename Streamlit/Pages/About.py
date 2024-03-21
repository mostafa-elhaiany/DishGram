import graphviz

def draw_about(st):
    st.title("About Page")
    st.write("This is the about page. Learn more about us here.")
    st.divider()

    st.write("Dishgram is a social-media platfrom that also acts as a nutrition app.")
    st.write("When you order food, when you cook something that looks fabulous, the first thought is usually I wanna take a pic and show my friends.")
    st.write("Why make nutrition tracking any harder than this?")
    st.divider()

    st.write("Each time you upload a new image it's sent to our backend servers where we find out what the meal is, find out the estimate calorie count and nutrients for you")
    st.write("Not only that, but everyone that follows you can see your meals and your nutrition score. You can challenge your friends on who's more healthy")
    st.divider()

    st.write("But wait there's more, ")
    st.write("Unsure what to eat? Unsure how to customize? ask our very own system to handle it for you")
    st.write("Have restrictions of any kind? tweak your tags and we'll take it off your feed")
    st.divider()

    st.write("And as if that wasn't already enough,")
    st.write("unsure how to cook the meal? The instructions are too unclear. Say no more!")
    st.write("Our system generates an AI generated recipe video for you to follow through")
    st.divider()


    st.write("Let's visualize how the video generation tool looks like")

    graph = graphviz.Digraph()
    graph.edge('User', 'GPT_1')
    graph.edge('System', 'GPT_1')
    graph.edge('GPT_1', 'GPT_1')
    graph.edge('GPT_1', 'GPT_2')
    graph.edge('GPT_2', 'GPT_2')
    graph.edge('System', 'GPT_2')
    graph.edge('GPT_2', 'Text2Video')
    graph.edge('Text2Video', 'UI')
    graph.edge('UI', 'User')

    col1, col2,_ = st.columns(3)
    col1.graphviz_chart(graph)
    col2.write("This is a highlevel chart of how our Ai video generation is set up")
    col2.write("""
    First, the user inputs a query for a certain dish, country, or simply nothing.
    A list of dishes based on the users interests are then created.
    LLMs are used to structure recipe into Ingredients, and Instructions
    The LLMs are also used as self-supervisors where they re-prompt themselves for feedback and idea validation
    Instructions are used to generate a text2video prompt by another LLM, using the same self feedback loop
    Prompts are then used to generate a video for each instruction.
    An algorithm puts the videos together with Ai generated Audio and sends it back to the user
""")
    
    st.divider()
    _,title,_ = st.columns(3)
    title.title("Team Members")
    team1, team2, team3, team4 = st.columns(4)
    team1.image("Streamlit/Assets/Images/hamna.jpeg")
    team1.write("Hamna Khalid")

    team2.image("Streamlit/Assets/Images/joel.jpeg")
    team2.write("Joel Lingg")

    team3.image("Streamlit/Assets/Images/ibrahim.jpeg")
    team3.write("Ibrahim Siraj Pasha")

    team4.image("Streamlit/Assets/Images/mostafa.jpeg")
    team4.write("Mostafa ElHayani")
    
    st.divider()
    _,image_col, _ = st.columns(3)
    # image_col.image("Streamlit/Assets/Images/socialsQR.jpeg")
    # image_col.write("Follow our socials!")
    