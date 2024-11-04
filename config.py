import os
from typing import Tuple, TypeAlias, Literal
from dotenv import load_dotenv

load_dotenv()

# API key configuration
openai_key = os.getenv("OPENAI_API_KEY")

# Type aliases
BoundingBox: TypeAlias = Tuple[float, float, float, float]
Dataset: TypeAlias = Literal["davinci", "curie", "babbage", "USGS/SRTMGL1_003"]

class BoundingBoxNotFoundError(Exception):
    """Custom exception raised when no bounding box is found in the message."""
    pass

