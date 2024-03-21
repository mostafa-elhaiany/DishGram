from dotenv import load_dotenv
import os

load_dotenv()

RECIPE_API = os.getenv('recipeAPI')
OPENAI_API = os.getenv('openAi')
RECIPE2INSTRUCTIONS = os.getenv('recipe2instructions_prompt')
INSTRUCTIONS2VIDEO = os.getenv('recipe2video_prompt')