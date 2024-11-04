from config import BoundingBox, Dataset
from datetime import datetime
import streamlit as st
import geemap.foliumap as geemap
import ee

ee.Authenticate()
ee.Initialize(project="ee-n3xtcoder")

datasets = ['USGS/SRTMGL1_003', "COPERNICUS/S1_GRD"]

def display_data(data: tuple[BoundingBox, datetime, Dataset]) -> None:
    """Displays the data on a map or other output in Streamlit."""
    Map = geemap.Map(center=[40, -100], zoom=4)
    Map.add_basemap("ROADMAP")

    vis_params = {'min': 0, 'max': 3000, 'palette': ['blue', 'green', 'red']}

    bounding_box, time, dataset = data
    dataset = datasets[0]  # TODO: get from NL input
    st.write(f"Bounding Box: {bounding_box}")
    st.write(f"Time: {time}")
    st.write(f"Dataset: {dataset}")

    # Update the map with the new dataset
    new_dataset = ee.Image(dataset)
    new_vis_params = vis_params  # TODO: get from NL input
    Map.addLayer(new_dataset, new_vis_params, dataset)

    bounding_box_list = [
        [bounding_box[1], bounding_box[3]],  # [south, west]
        [bounding_box[0], bounding_box[2]]   # [north, east]
    ]

    Map.fit_bounds(bounding_box_list)
    
    Map.to_streamlit(width=800, height=600)

