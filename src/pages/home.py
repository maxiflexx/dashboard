import pandas as pd
import streamlit as st

from src.components.table import write_table
from src.core.services.api_client import get_markets


def write():
    with st.spinner("Loading Home ..."):
        # title
        st.write(
            """
            # Home
            """
        )

        # body
        st.write(
            """
            What is Lorem Ipsum?
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
            """
        )

        st.write(
            """
            What is Lorem Ipsum?
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
            """
        )

        data = get_markets()
        df = pd.DataFrame(data)

        write_table(df)
