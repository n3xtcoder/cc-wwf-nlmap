from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from datetime import datetime
from langchain_core.output_parsers import JsonOutputParser
from config import BoundingBox, Dataset, openai_key

# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["message"],
    template="""
    Extract the following information from the input text:
    1. BoundingBox: in the format {{"north": float, "south": float, "east": float, "west": float}}
    2. Datetime: a specific date in YYYY-MM-DD format.
    3. Dataset: name of the dataset.

    Input text: "{message}"

    Expected JSON output format:
    {{
        "BoundingBox": {{"north": <float>, "south": <float>, "east": <float>, "west": <float>}},
        "Datetime": "<YYYY-MM-DD>",
        "Dataset": "<dataset_name>"
    }}
    """
)

# Initialize the model
model = ChatOpenAI(api_key=openai_key, model="gpt-4o")
llm_chain = prompt_template | model | JsonOutputParser()

def parse_data(message: str) -> tuple[BoundingBox, datetime, Dataset]:
    """Parses the bounding box, time, and dataset from a prompt."""
    response = llm_chain.invoke(input={"message": message})
    bounding_box = (
        response["BoundingBox"]["north"],
        response["BoundingBox"]["south"],
        response["BoundingBox"]["east"],
        response["BoundingBox"]["west"]
    )
    time = datetime.strptime(response["Datetime"], "%Y-%m-%d")
    dataset = response["Dataset"]
    return bounding_box, time, dataset
