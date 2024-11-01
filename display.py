from config import BoundingBox, Dataset
from datetime import datetime
import streamlit as st

def display_data(data: tuple[BoundingBox, datetime, Dataset]) -> None:
    """Displays the data on a map or other output in Streamlit."""
    bounding_box, time, dataset = data
    st.write(f"Bounding Box: {bounding_box}")
    st.write(f"Time: {time}")
    st.write(f"Dataset: {dataset}")
