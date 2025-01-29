# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:23:15 2025

@author: Thiwe
"""

import streamlit as st
import pandas as pd
import datetime
from io import BytesIO
from PIL import Image

# Title of the app
st.title("Researcher Profile Page")

# Default profile image
default_image = "picture.png"
st.image(default_image, caption="Profile Picture", width=150)

# Upload a profile picture
uploaded_file = st.file_uploader("Upload a profile picture", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Profile Picture", width=150)

# Researcher information
name = "Miss T Mabuza"
field = "Industrial Engineering"
institution = "University of Johannesburg"

# Sidebar: Date Range Selection
st.sidebar.title("Select Date Range")
start_date = st.sidebar.date_input("Start Date", value=datetime.date(2019, 1, 1))
end_date = st.sidebar.date_input("End Date", value=datetime.date(2025, 12, 31))

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Publications Section
st.header("Publications")
csv_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if csv_file is not None:
    publications = pd.read_csv(csv_file)

    # Display the uploaded data
    st.dataframe(publications)

    # Filtering by keyword
    keyword = st.text_input("Filter by keyword")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str, errors='ignore').str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Publication Trends Visualization
st.header("Publication Trends")
if csv_file is not None:
    if "Year" in publications.columns:
        try:
            publications["Year"] = pd.to_numeric(publications["Year"], errors="coerce")  # Ensure Year is numeric
            year_counts = publications["Year"].dropna().astype(int).value_counts().sort_index()
            st.bar_chart(year_counts)
        except Exception as e:
            st.write("Error processing 'Year' column:", e)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Contact Information
st.header("Contact Information")
email = "jane.doe@example.com"
st.write(f"You can reach {name} at {email}.")