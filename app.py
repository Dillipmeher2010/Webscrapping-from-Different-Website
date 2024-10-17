import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to scrape data
def scrape_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Modify the following line based on the structure of the target website
        titles = soup.find_all('h2')  # Example: scrapes all <h2> tags
        return [title.get_text() for title in titles]
    
    except Exception as e:
        st.error(f"Error occurred: {e}")
        return []

# Streamlit app layout
st.title("Web Scraping App")
url = st.text_input("Enter the URL to scrape:")

if st.button("Scrape"):
    if url:
        st.write("Scraping data from:", url)
        results = scrape_data(url)

        if results:
            st.subheader("Scraped Data:")
            for idx, title in enumerate(results):
                st.write(f"{idx + 1}. {title}")
        else:
            st.write("No data found or error occurred.")
    else:
        st.warning("Please enter a valid URL.")
