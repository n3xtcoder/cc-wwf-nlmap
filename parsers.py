from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from datetime import datetime
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.exceptions import OutputParserException
from config import BoundingBox, Dataset, openai_key, DatasetNotFoundError
from prompts import bounding_box_prompt, datetime_prompt, dataset_prompt
from data import datasets

model = ChatOpenAI(api_key=openai_key, model="gpt-4o", temperature=0.5)

def extract_bounds(message: str) -> BoundingBox | None:
    """Extracts the bounding box from a prompt."""
    prompt_template = PromptTemplate(input_variables=["message"], template=bounding_box_prompt)
    llm_chain = prompt_template | model | JsonOutputParser()
    try:
        response = llm_chain.invoke(input={"message": message})
    except OutputParserException:
        return None
    
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
    llm_chain = prompt_template | model | StrOutputParser()
    response = llm_chain.invoke(input={"message": message})
    try: 
        return datetime.strptime(response, "%Y-%m-%d")
    except ValueError:
        return datetime.now()

def generate_dataset_descriptions(datasets: list[dict[str, any]]) -> str:
    """Creates a description of the dataset."""
    dataset_descriptions = ""

    for idx, dataset in enumerate(datasets, start=1):
        dataset_descriptions += f"""{idx}. **{dataset['name']}**
    - **Image ID:** "{dataset['image_id']}"
    - **Date Range:** {dataset['date_start']} to {dataset['date_end']}
    - **Tags:** {dataset['tags']}
    - **Description:** {dataset['description'].strip()}
    \n"""
        
    return dataset_descriptions


def extract_dataset(message: str) -> Dataset:
    """Extracts the dataset from a prompt."""

    dataset_descriptions = generate_dataset_descriptions(datasets)
    prompt_template = PromptTemplate(input_variables=["message", "dataset_descriptions"], template=dataset_prompt)
    
    llm_chain = prompt_template | model | StrOutputParser()
    response = llm_chain.invoke(input={"message": message, "dataset_descriptions": dataset_descriptions})
    
    clean_response = response.strip().strip('"')
    valid_image_ids = [dataset['image_id'] for dataset in datasets]

    if clean_response not in valid_image_ids:
        raise DatasetNotFoundError("Invalid dataset.")

    return clean_response

# extract the dataset
def translate_nl_to_map_data(message: str) -> tuple[BoundingBox | None, datetime, Dataset]:
    """Parses the bounding box, time, and dataset from a prompt."""

    # TODO: run the functions concurrently
    bounding_box = extract_bounds(message)
    time = extract_time(message)
    dataset = extract_dataset(message)

    return bounding_box, time, dataset
