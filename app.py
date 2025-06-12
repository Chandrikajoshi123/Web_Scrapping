import os
import requests
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
st.title("🖼️ Pinterest Image Scraper")

# Use secret from Streamlit's secure vault
ACCESS_TOKEN = st.secrets["access_token"]
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

search_term = st.text_input("Enter search keyword", "minimalist interior")
if st.button("Fetch Pins"):
    with st.spinner("Fetching pins..."):
        base_url = f"https://api.pinterest.com/v5/search/pins/?query={search_term}&page_size=25"
        pins = []
        next_url = base_url

        while next_url and len(pins) < 100:
            res = requests.get(next_url, headers=headers)
            data = res.json()
            pins.extend(data.get("items", []))
            bookmark = data.get("bookmark")
            next_url = base_url + f"&bookmark={bookmark}" if bookmark else None

        st.markdown(f"### Found {len(pins)} pins")
        rows = []
        cols = st.columns(5)
        for i, pin in enumerate(pins):
            media = pin.get("media", {})
            image_url = media.get("images", {}).get("original", {}).get("url", "")
            if image_url:
                with cols[i % 5]:
                    st.image(image_url, use_column_width=True)
                rows.append({
                    "id": pin.get("id"),
                    "title": pin.get("title", ""),
                    "description": pin.get("description", ""),
                    "image_url": image_url
                })

        df = pd.DataFrame(rows)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download CSV", data=csv, file_name="pins_data.csv", mime="text/csv")
