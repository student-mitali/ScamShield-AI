from dotenv import load_dotenv
import os

load_dotenv()

from caspian_sdk import CommClient

client = CommClient(
    api_key=os.getenv("CASPIAN_API_KEY"),
    base_url=os.getenv("CASPIAN_BASE_URL")
)

print("✅ Caspian Connected")