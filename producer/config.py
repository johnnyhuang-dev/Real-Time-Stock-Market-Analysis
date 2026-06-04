import logging
import os
from dotenv import load_dotenv

load_dotenv()

#configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)