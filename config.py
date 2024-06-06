import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    format="%(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

class Config(object):
    # Get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    # The Telegram API details
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")

    # File / video download location
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 4194304000  # 4GB

    # Chunk size that should be used with requests : default is 128KB
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    # Proxy for accessing youtube-dl in GeoRestricted Areas
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # Set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3700

    OWNER_ID = int(os.environ.get("OWNER_ID", 0))
    ADL_BOT_RQ = {}
    AUTH_USERS = list({int(x) for x in os.environ.get("AUTH_USERS", "0").split()})
    if OWNER_ID not in AUTH_USERS:
        AUTH_USERS.append(OWNER_ID)
