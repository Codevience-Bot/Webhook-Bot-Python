import os
from os.path import join, dirname
from dotenv import load_dotenv
from webhook_bot.app import app

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
app.run(port=os.environ.get("port"), debug=True)
