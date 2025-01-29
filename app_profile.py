# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:00:55 2025

@author: Thiwe
"""

import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information

name = "Miss T Mabuza"
field = "Industrial Engineering"
institution = "University of Johannesburg"
st.sidebar.title("Select Date Range")
start_date = st.sidebar.date_input(label="Start Date", value=pd.to_datetime('2019-01-01'))
end_date = st.sidebar.date_input(label="End Date", value=pd.to_datetime('2025-12-31'))

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "jane.doe@example.com"
st.write(f"You can reach {name} at {email}.")


 