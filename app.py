import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to scrape data
def scrape_tripadvisor(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.content, 'html.parser')

        # Scrape specific data from the page (adjust according to the page structure)
        titles = soup.find_all('span', class_='ui_header h1')
        reviews = soup.find_all('q')
        
        scraped_data = []
        for title, review in zip(titles, reviews):
            scraped_data.append({
                'title': title.get_text(strip=True),
                'review': review.get_text(strip=True)
            })

        return scraped_data
    
    except Exception as e:
        st.error(f"Error occurred: {e}")
        return []

# Streamlit app layout
st.title("TripAdvisor Review Scraper")
url = st.text_input("Enter the TripAdvisor URL to scrape:")

if st.button("Scrape"):
    if url:
        st.write("Scraping data from:", url)
        results = scrape_tripadvisor(url)

        if results:
            st.subheader("Scraped Data:")
            for idx, data in enumerate(results):
                st.write(f"**Review {idx + 1}:**")
                st.write(f"**Title:** {data['title']}")
                st.write(f"**Review:** {data['review']}")
                st.write("---")
        else:
            st.write("No data found or an error occurred.")
    else:
        st.warning("Please enter a valid URL.")
