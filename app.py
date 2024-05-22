import streamlit as st

import src.pages.analysis
import src.pages.dataset
import src.pages.home
from src.core.services.api_client import data_io_client

PAGES = {
    "Home": src.pages.home,
    "Analyses": src.pages.analysis,
    "Dataset": src.pages.dataset
}

def sidebar():
	# st.sidebar.image("./src/assets/images/logo.png", use_column_width=True)

	st.sidebar.title("Navigation")

	selection = st.sidebar.radio("Go to", list(PAGES.keys()))

	page = PAGES[selection]

	data = data_io_client.get_json('/coins', { "market": "KRW-BTC", "startDate": "2024-04-20", "endDate": "2024-04-26" })

	with st.spinner(f"Loading {selection} ..."):
		page.write()

def main():
	sidebar()


if __name__ == "__main__":
	main()
