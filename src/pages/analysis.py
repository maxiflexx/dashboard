from typing import Any, Dict, List

import pandas as pd
import streamlit as st

from src.components.candlestick import write_candlestick
from src.components.metric import write_metric
from src.core.services.api_client import data_io_client
from src.core.services.date import add_days, get_now, sub_days


def get_markets():
    answer = data_io_client.get_json(
        path='/markets',
    )
    return answer

def load_data(code: str):
    now = get_now()
    startDate = sub_days(now, 5)
    endDate = add_days(now, 1)

    answer = data_io_client.get_json(
        path='/coins',
        query={
            "market": code,
            "startDate": startDate,
            "endDate": endDate,
            "limit": 100,
        }
    )
    return answer

def find_market(markets, code):
    for market in markets:
        if market['code'] == code:
            return market

def write():
    markets = get_markets()
    enabled_markets = [market for market in markets if market['isEnabled']]

    market_codes = [f'{market["code"]}' for market in enabled_markets]
    code = st.selectbox(
        "market??",
        market_codes,
        key='selected_market_code',
    )

    target_market = find_market(enabled_markets, code)

    data = load_data(code)
    df = pd.DataFrame(data['data'])

    df['MA20'] = df["tradePrice"].rolling(window=20).mean()
    df['MA5'] = df["tradePrice"].rolling(window=5).mean()


    with st.spinner("Loading Home ..."):
        write_metric(target_market, df)
        write_candlestick(df)
