import streamlit as st 


st.set_page_config(page_title="NYC Venue Search", layout="wide", initial_sidebar_state="expanded")

# UI text strings 
page_title = "FormationML Projet 5"
page_helper = "Poser votre question "
empty_search_helper = "Select a borough and neighborhood, and enter a search term to get started."
category_list_header = "Suggested venue categories"
borough_search_header = "Select a borough"
neighborhood_search_header = "Select (up to 5) neighborhoods"
semantic_search_header = "What are you looking for?"
semantic_search_placeholder = "Epic night out"
search_label = "Search for categories and venues"
venue_list_header = "Venue details"




def render_search_result():
    """
    Render the search results on the main content area.
    """
    col1, col2 = st.columns([1,2])
    col1.write(category_list_header)
    col1.table(st.session_state.suggested_categories)
    col2.write(f"Found {len(st.session_state.suggested_places)} venues.")
    if (len(st.session_state.suggested_places) > 0):
        col2.map(st.session_state.suggested_places, zoom=13, use_container_width=True)
        st.write(venue_list_header)
        st.dataframe(data=st.session_state.suggested_places, use_container_width=True)


boroughs = [{'NAME':'Brooklyn'},{'NAME':'Bronx'},{'NAME':'Manhattan'},{'NAME':'Queens'},{'NAME':'Staten Island'}]
#boroughs = api.get_boroughs()



st.title(page_title)
st.write(page_helper)
st.write("---")

