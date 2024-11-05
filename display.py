from config import BoundingBox, Dataset
from datetime import datetime, timedelta
import streamlit as st
import geemap.foliumap as geemap
import ee
from data import datasets

ee.Authenticate()
ee.Initialize(project="ee-n3xtcoder")

def display_data(data: tuple[BoundingBox | None, datetime, Dataset]) -> None:
    """Displays the data on a map or other output in Streamlit."""
    Map = geemap.Map(center=[40, -100], zoom=4)
    Map.add_basemap("ROADMAP")

    bounding_box, time, dataset_name = data
    st.write(f"Bounding Box: {bounding_box}")
    st.write(f"Time: {time}")
    st.write(f"Dataset name: {dataset_name}")

    dataset = next((item for item in datasets if item["image_id"] == dataset_name), None)
    if dataset is None:
        raise ValueError("Invalid dataset name.")

    image = None
    start_date = time - timedelta(days=3)
    end_date = time + timedelta(days=3)
    if dataset["is_collection"]:
        image_collection = ee.ImageCollection(dataset_name).filterDate(start_date, end_date)
        image = image_collection.first()
    else:
        image = ee.Image(dataset_name)

    vis_params = {'min': dataset["min"], 'max': dataset["max"]}

    Map.addLayer(ee_object=image, vis_params=vis_params, name=dataset_name, opacity=0.7)

    if bounding_box is not None:
        bounding_box_list = [
            [bounding_box[1], bounding_box[3]],  # [south, west]
            [bounding_box[0], bounding_box[2]]   # [north, east]
        ]

        Map.fit_bounds(bounding_box_list)
    else:
        Map.setCenter(0, 0, 2)
    
    Map.to_streamlit(width=800, height=600)

