bounding_box_prompt = """
You are an expert in geographical data extraction and analysis. Your task is to examine the user's message and determine whether it contains any mentions of geographical locations.

If the message includes a geographical location, identify it and provide its bounding box coordinates in the following JSON format:

{{"north": <float>, "south": <float>, "east": <float>, "west": <float>}}

Ensure that the coordinates are accurate and correspond precisely to the geographical entity mentioned.

If the message does not contain any geographical location from which you could create a bounding box, return a unified output indicating that no geographical location was found in the message.

Here are some examples:

1. If the message is: "Show me the latest Sentinel 2 image from Berlin", return the bounding box coordinates of Berlin in the JSON format.

2. If the message is: "Show me the SRTM elevation for the Alps", return the bounding box coordinates of the Alps in the JSON format.

3. If the message is: "Show a consensus land cover map from Dynamic world for Mozambique for the year 2023", return the bounding box coordinates of Mozambique in the JSON format.

4. If the message is: "You mama speaks 3 languages", return: "No geographical location found in the message."

5. If the message is: "Show me the Carbon Monoxide from Sentinel 5P for the globe in 2020 and 2023", return "No geographical location found in the message.".

Here is the user's message:
{message}

Return the bounding box if a geographical location is found; otherwise, return a unified output indicating that no location was found.
"""

# how to parse the different outputs

datetime_prompt = """
You are an expert in temporal data extraction and analysis. Your task is to examine the user's message and determine whether it contains any specific dates.

If the message includes a date, extract it and provide it in the YYYY-MM-DD format. Ensure that the extracted date is accurate and corresponds precisely to the date mentioned in the message.

If the message does not contain any specific date, year or similar, return a unified output indicating that no date was found in the message. If a longer time period is mentioned, such as a month or year, you should return the middle day of that period.

If the message contains more than one date, you should return the first date found.

Here are some examples:

1. If the message is: "Show me the latest Sentinel 2 image from Berlin", return: "No date found in the message."

2. If the message is: "Show me the SRTM elevation for the Alps", return: "No date found in the message."

3. If the message is: "We need to complete the project by the end of the month", return: "No date found in the message."

4. If the message is: "Show a consensus land cover map from Dynamic world for Mozambique for the year 2023", return the date "2023-07-01".

Here is the user's message:
{message}

Return the date in YYYY-MM-DD format if a specific date is found; otherwise, return a unified output indicating that no date was found.
"""

dataset_prompt = """
You are an expert in geographical data mapping and analysis. Your task is to examine the user's message and determine whether it refers to any of the available datasets listed below.

**Available Datasets:**

{dataset_descriptions}

**Instructions:**

- If the user's message refers to one of these datasets, identify the dataset and return its **Image ID** (e.g., "COPERNICUS/S2_HARMONIZED").
- Ensure that the dataset you select matches the user's request precisely.
- If the message does not correspond to any of the available datasets, return "No dataset found in the message.".

**Here is the user's message:**

{message}

**Return the dataset's Image ID if a matching dataset was found; otherwise, return "No dataset found in the message.".**
"""