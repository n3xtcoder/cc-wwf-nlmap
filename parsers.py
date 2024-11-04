from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from datetime import datetime
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from config import BoundingBox, Dataset, openai_key, BoundingBoxNotFoundError
from prompts import bounding_box_prompt, datetime_prompt

model = ChatOpenAI(api_key=openai_key, model="gpt-4o")

def extract_bounds(message: str) -> BoundingBox:
    """Extracts the bounding box from a prompt."""
    prompt_template = PromptTemplate(input_variables=["message"], template=bounding_box_prompt)
    llm_chain = prompt_template | model | JsonOutputParser()
    try:
        response = llm_chain.invoke(input={"message": message})
    except OutputParserException:
        raise BoundingBoxNotFoundError("No bounding box found in the message.")
    
    bounding_box = (
        response["north"],
        response["south"],
        response["east"],
        response["west"]
    )

    return bounding_box

def extract_time(message: str) -> datetime:
    """Extracts the time from a prompt."""
    prompt_template = PromptTemplate(input_variables=["message"], template=datetime_prompt)
    llm_chain = prompt_template | model | JsonOutputParser()
    try:
        response = llm_chain.invoke(input={"message": message})
    except OutputParserException:
        return datetime.now()
        
    time = datetime.strptime(response, "%Y-%m-%d")
    return time

def extract_dataset(message: str) -> Dataset:
    """Extracts the dataset from a prompt."""

    # TODO: create a list of datasets with all their properties
    # TODO: create a prompt
    # TODO: work on the display function

    return "USGS/SRTMGL1_003"

# extract the dataset
def translate_nl_to_map_data(message: str) -> tuple[BoundingBox, datetime, Dataset]:
    """Parses the bounding box, time, and dataset from a prompt."""

    bounding_box = extract_bounds(message)
    time = extract_time(message)
    dataset = extract_dataset(message)

    print(f"Bounding Box: {bounding_box}")
    print(f"Time: {time}")
    print(f"Dataset: {dataset}")

    return bounding_box, time, dataset
