import streamlit as st

import src.pages.analysis
import src.pages.dataset
import src.pages.home

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

	with st.spinner(f"Loading {selection} ..."):
		page.write()

def main():
	sidebar()


if __name__ == "__main__":
	main()
