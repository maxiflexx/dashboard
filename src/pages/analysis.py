import pandas as pd
import streamlit as st

from src.components.candlestick import write_candlestick
from src.components.metric import write_metric
from src.core.services.api_client import get_coins, get_markets
from src.core.services.date import add_days, get_now, sub_days


def find_market(markets, code):
    for market in markets:
        if market['code'] == code:
            return market

def write():
    with st.spinner("Loading Home ..."):
        # title
        st.write(
            """
            # Analysis
            """
        )

        # body
        # selectbox
        markets = get_markets()

        enabled_markets = [market for market in markets if market['isEnabled']]

        market_codes = [f'{market["code"]}' for market in enabled_markets]
        code = st.selectbox(
            "Choose a market",
            market_codes,
            key='selected_market_code',
        )

        target_market = find_market(enabled_markets, code)

        now = get_now()
        start_date = sub_days(now, 5)
        end_date = add_days(now, 1)

        data = get_coins(code, start_date, end_date, 100)

        df = pd.DataFrame(data['data'])

        df['MA20'] = df["tradePrice"].rolling(window=20).mean()
        df['MA5'] = df["tradePrice"].rolling(window=5).mean()

        # metric and chart
        write_metric(target_market, df)
        write_candlestick(df)
