from typing import Any, Dict, List

import pandas as pd
import streamlit as st


def write_metric(target_market: Dict[str, Any], df: pd.DataFrame):
    max_price = df['highPrice'].max()
    min_price = df['lowPrice'].min()
    first = df.iloc[0]

    st.markdown(
        """
        <style>
            [data-testid="stMetricValue"] {
                font-size: 1vw;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    col1.container(height=120, border=True).metric(label="Market", value=target_market['englishName'])
    col2.container(height=120, border=True).metric(label="Current", value=first['candleDateTimeUtc'])
    col3.container(height=120, border=True).metric(label="Max Price", value=max_price, delta=int(max_price - min_price))
    col4.container(height=120, border=True).metric(label="Min Price", value=min_price, delta=int(min_price - max_price))
