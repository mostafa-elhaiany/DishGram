from dotenv import load_dotenv
import os

load_dotenv()

RECIPE_API = os.getenv('recipeAPI')
OPENAI_API = os.getenv('openAi')
RECIPE2INSTRUCTIONS = os.getenv('recipe2instructions_prompt')
INSTRUCTIONS2VIDEO = os.getenv('recipe2video_prompt')

CATEGORIES_API = os.getenv("backend_route") + os.getenv("categories_api")
CALORIES_NUTRIENTS_API = os.getenv("backend_route") + os.getenv("calories_api")
FRIDGE_DETECTION_API = os.getenv("backend_route") + os.getenv("fridge_detection_route")
