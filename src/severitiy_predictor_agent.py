import os
from dotenv import load_dotenv

print("Current working directory:", os.getcwd())

#dotenv_path ="venv/.env"

#print("Dot env path exists", os.path.exists(dotenv_path))

#load_dotenv(dotenv_path="venv/.env")

load_dotenv()

print("openai_api_key",os.getenv("OPENAI_API_KEY"))
print("SMTP_PASS",os.getenv("SMTP_PASS"))
