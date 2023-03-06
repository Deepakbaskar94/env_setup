from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Access environment variables
api_key = os.getenv('API_KEY')
database_url = os.getenv('DATABASE_URL')
debug = os.getenv('DEBUG')

print("",api_key,"\n",database_url,"\n",debug)
# print("",type(api_key),"\n",type(database_url),"\n",type(debug))
