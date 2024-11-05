import os
from typing import Tuple, TypeAlias, Literal
from dotenv import load_dotenv

load_dotenv()

# API key configuration
openai_key = os.getenv("OPENAI_API_KEY")

# Type aliases
BoundingBox: TypeAlias = Tuple[float, float, float, float]
Dataset: TypeAlias = Literal["COPERNICUS/S2_HARMONIZED", "CGIAR/SRTM90_V4", "GOOGLE/DYNAMICWORLD/V1", "COPERNICUS/S5P/OFFL/L3_CO", "WORLDCLIM/V1/BIO"]

class DatasetNotFoundError(Exception):
    """Custom exception raised when no dataset is found in the message."""
    pass
