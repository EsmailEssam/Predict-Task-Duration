import os
from openai import OpenAI
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)

######################################## OpenAI ########################################
# Load environment variables
load_dotenv(override=True)

try:
    # Get OpenAI API key
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    # Initialize OpenAI client
    client = OpenAI(api_key=OPENAI_API_KEY)

except:
    logging.info("OpenAI API key not found in environment variables")


######################################## variables ########################################
# Path to the trained model
MODEL_PATH = "../models/best_model.pkl"

# Encoder mapping for 'Environment'
ENVIRONMENT_MAPPING = {"Arctic": 0, "Desert": 1, "Onshore": 2, "Offshore": 3}