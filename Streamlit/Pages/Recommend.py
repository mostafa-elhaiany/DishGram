from utils.Api import return_fridge_info, get_nutritional_value
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def visualize_object_detection(st, image, detections):
    # Convert image to numpy array
    
    image_np = np.array(image)

    # Create figure and axis
    fig, ax = plt.subplots()

    # Display the image
    ax.imshow(image_np)

    items = []
    # Plot object detection boxes
    for detection in detections:
        x, y, width, height = detection['x'], detection['y'], detection['width'], detection['height']
        rect = plt.Rectangle((x, y), width, height, linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
        items.append(detection["class"])

    # Set axis properties
    ax.axis('off')

    # Show plot
    st.pyplot(fig)

    return items

def handle_images(st):
    # Upload image button
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    if(uploaded_file):
        response = return_fridge_info(uploaded_file)
        # st.json(response)
        # st.image(uploaded_file)
        size = (response["image"]["width"], response["image"]["height"])
        image = Image.open(uploaded_file).resize(size)
        items = visualize_object_detection(st, image,response["predictions"])
        st.json(items)

        st.markdown("""### Tomato and Banana Salad:
        #### Ingredients:
        - 2 ripe tomatoes
        - 1 ripe banana
        - 1 tablespoon olive oil
        - 1 tablespoon balsamic vinegar
        - Salt and pepper to taste
        - Optional: Fresh herbs like basil or parsley for garnish

        #### Instructions:
        1. **Prepare the Ingredients:**
        - Wash the tomatoes and slice them thinly.
        - Peel the banana and slice it into thin rounds.

        2. **Assemble the Salad:**
        - Arrange the tomato slices on a serving plate.
        - Place the banana slices on top of the tomatoes.

        3. **Dress the Salad:**
        - In a small bowl, whisk together olive oil and balsamic vinegar.
        - Drizzle the dressing over the tomato and banana slices.

        4. **Season and Garnish:**
        - Season the salad with salt and pepper to taste.
        - If desired, sprinkle some fresh herbs like basil or parsley on top for added flavor and presentation.

        5. **Serve:**
        - Serve the Tomato and Banana Salad immediately as a refreshing appetizer or side dish.

        #### Additional Notes:
        - Feel free to adjust the quantities of olive oil, balsamic vinegar, salt, and pepper according to your taste preferences.
        - You can also add other ingredients like red onion slices, cucumber slices, or mixed greens to enhance the salad.
        - This salad pairs well with grilled meats or fish for a complete meal.
        """)
        st.title("Nutritional Value")
        nutrition = get_nutritional_value("Tomato and Banana")
        if(len(nutrition)>0):
            for item in nutrition:
                st.code(item)
        else:
            st.write("Unfortunatly our database doesn't have data on that yet.")
            st.write("But fret not! We're working on it.")
        
        st.write("would you like to generate a recipe video about that?")
        generate = st.button("Generate recipe video")
        if(generate):
            st.divider()
            st.title("Ai generated video")
            st.video(f"Streamlit/Assets/Videos/video{np.random.randint(1,9)}.mp4")



def handle_preference(st):
    st.markdown("""
Based on your previous information it seems like you really like pasta 
We think you would love this 
### Pasta Primavera:
#### Ingredients:
- 8 oz pasta of your choice (such as spaghetti, penne, or fusilli)
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 small onion, thinly sliced
- 1 bell pepper, thinly sliced
- 1 medium zucchini, thinly sliced
- 1 cup cherry tomatoes, halved
- Salt and pepper to taste
- Crushed red pepper flakes (optional)
- Grated Parmesan cheese for serving
- Fresh basil leaves for garnish

#### Instructions:
1. **Cook the Pasta:**
   - Cook the pasta according to the package instructions until al dente. Drain and set aside.

2. **Prepare the Vegetables:**
   - In a large skillet, heat olive oil over medium heat.
   - Add minced garlic and sliced onion to the skillet. Sauté until the onion becomes translucent, about 2-3 minutes.

3. **Add Bell Pepper and Zucchini:**
   - Add the sliced bell pepper and zucchini to the skillet. Cook for another 3-4 minutes until the vegetables are slightly tender but still crisp.

4. **Incorporate Cherry Tomatoes:**
   - Add the cherry tomatoes to the skillet. Cook for an additional 2 minutes until the tomatoes soften slightly.

5. **Season and Toss:**
   - Season the vegetables with salt, pepper, and crushed red pepper flakes (if using), to taste.
   - Add the cooked pasta to the skillet with the vegetables. Toss everything together until well combined.

6. **Serve:**
   - Divide the Pasta Primavera among serving plates.
   - Garnish with freshly grated Parmesan cheese and torn basil leaves.
   - Serve hot and enjoy!

#### Additional Notes:
- Feel free to customize the vegetables based on your preferences or what you have available. You can add mushrooms, broccoli, spinach, or any other favorite vegetables.
- For extra protein, you can add cooked chicken, shrimp, or tofu to the dish.
- Adjust the seasoning and spice level according to your taste preferences.
- This dish is versatile and can be enjoyed as a light lunch or dinner.
""")
    st.write("would you like to generate a recipe video about that?")
    generate = st.button("Generate recipe video")
    if(generate):
        st.divider()
        st.title("Ai generated video")
        st.video(f"Streamlit/Assets/Videos/video{np.random.randint(1,9)}.mp4")

def handle_surprise_me(st):
    st.markdown("""### Surprise Me Stir-Fry:

#### Ingredients:
- 1 lb protein of your choice (such as chicken breast, beef sirloin, tofu, or shrimp), thinly sliced or cubed
- 2 tablespoons vegetable oil
- 2 cloves garlic, minced
- 1 small onion, thinly sliced
- 2 cups mixed vegetables (such as bell peppers, broccoli florets, snap peas, carrots, mushrooms)
- 1/4 cup soy sauce or tamari (for a gluten-free option)
- 2 tablespoons oyster sauce (for a vegetarian/vegan option, substitute with hoisin sauce)
- 1 tablespoon rice vinegar
- 1 tablespoon honey or maple syrup (for a vegan option)
- 1 teaspoon sesame oil
- 1 tablespoon cornstarch mixed with 2 tablespoons water
- Cooked rice or noodles for serving
- Sesame seeds and sliced green onions for garnish

#### Instructions:
1. **Prepare the Protein:**
   - If using meat, thinly slice or cube it. If using tofu, drain and press it to remove excess moisture, then cut into cubes.

2. **Stir-Fry the Protein:**
   - Heat vegetable oil in a large skillet or wok over medium-high heat.
   - Add the minced garlic and thinly sliced onion to the skillet. Sauté until fragrant and the onion is translucent, about 2-3 minutes.
   - Add the protein to the skillet and stir-fry until cooked through, about 5-7 minutes. Remove from the skillet and set aside.

3. **Cook the Vegetables:**
   - Add a little more oil to the skillet if needed.
   - Add the mixed vegetables to the skillet and stir-fry until they are crisp-tender, about 5-7 minutes.

4. **Make the Sauce:**
   - In a small bowl, whisk together soy sauce or tamari, oyster sauce (or hoisin sauce), rice vinegar, honey or maple syrup, and sesame oil.
   - Pour the sauce mixture into the skillet with the vegetables.

5. **Thicken the Sauce:**
   - Stir the cornstarch-water mixture to recombine, then pour it into the skillet.
   - Stir the sauce and vegetables until the sauce thickens and coats the vegetables evenly.

6. **Combine and Serve:**
   - Return the cooked protein to the skillet with the vegetables and sauce. Toss everything together until well combined and heated through.
   - Serve the Surprise Me Stir-Fry hot over cooked rice or noodles.
   - Garnish with sesame seeds and sliced green onions.
   - Enjoy the flavorful and exciting combination of ingredients in this Surprise Me Stir-Fry!

#### Additional Notes:
- Feel free to customize the stir-fry by adding your favorite vegetables or adjusting the sauce ingredients to suit your taste preferences.
- You can also add additional flavorings such as ginger, chili flakes, or garlic chili sauce for extra heat.
- This dish is versatile and can be made with any protein of your choice or made vegetarian/vegan by using tofu or tempeh.
- Leftovers can be stored in an airtight container in the refrigerator for up to 3 days.

Enjoy your Surprise Me Stir-Fry adventure!
""")
    st.write("would you like to generate a recipe video about that?")
    generate = st.button("Generate recipe video")
    if(generate):
        st.divider()
        st.title("Ai generated video")
        st.video(f"Streamlit/Assets/Videos/video{np.random.randint(1,9)}.mp4")


def draw_recommend(st):
    recommender = st.selectbox("Choose a recommendation system", ["What's in my fridge", "Based on preferences", "Surprise me"])

    if(recommender == "What's in my fridge"):
        handle_images(st)
    elif(recommender == "Based on preferences"):
        handle_preference(st)
    else:
        handle_surprise_me(st)
