import streamlit as st 


st.set_page_config(page_title="NYC Venue Search", layout="wide", initial_sidebar_state="expanded")

# UI text strings 
page_title = "NYC Venue Search"
page_helper = "Discover NYC! The Streamlit app uses cosine similarity to semantically match your query with Foursquare venue categories and find matching venues in your selected areas."
empty_search_helper = "Select a borough and neighborhood, and enter a search term to get started."
category_list_header = "Suggested venue categories"
borough_search_header = "Select a borough"
neighborhood_search_header = "Select (up to 5) neighborhoods"
semantic_search_header = "What are you looking for?"
semantic_search_placeholder = "Epic night out"
search_label = "Search for categories and venues"
venue_list_header = "Venue details"







boroughs = [{'NAME':'Brooklyn'},{'NAME':'Bronx'},{'NAME':'Manhattan'},{'NAME':'Queens'},{'NAME':'Staten Island'}]
#boroughs = api.get_boroughs()



st.title(page_title)
st.write(page_helper)
st.write("---")

