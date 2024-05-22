import pandas as pd
import streamlit as st

from src.components.candlestick import write_candlestick


def write():
    with st.spinner("Loading Home ..."):
        st.write(
            """
## The Magic of Streamlit

The only way to truly understand how magical Streamlit is to play around with it.
But if you need to be convinced first, then here is the **4 minute introduction** to Streamlit!

Afterwards you can explore examples in the Gallery and go to the [Streamlit docs](https://streamlit.io/docs/) to get started.
    """
        )
        file = st.file_uploader("Choose a file")
        if file is None:
            return

        if file.type != 'text/csv' and file.type != 'application/json':
            st.write('Please json or csv!')
            return

        df = pd.read_json(file)
        st.write(df)
        st.write(df.keys())

        st.write("select market and time field!")
        market_column, time_column = st.columns([1, 1])

        selected_market_field = market_column.selectbox('Market Field', df.keys(), index=None)
        selected_time_field = time_column.selectbox('Time Field', df.keys(), index=None)

        if selected_market_field is None or selected_time_field is None:
            return

        st.write("select ohlc field!")
        open_column, high_column, low_column, close_column = st.columns([1, 1, 1, 1])

        selected_open_field = open_column.selectbox('Open Price Field', df.keys(), index=None)
        selected_high_field = high_column.selectbox('High Price Field', df.keys(), index=None)
        selected_low_field = low_column.selectbox('Low Price Field', df.keys(), index=None)
        selected_close_field = close_column.selectbox('Close Price Field', df.keys(), index=None)

        if (
            selected_open_field is None or
            selected_high_field is None or
            selected_low_field is None or
            selected_close_field is None
        ):
            return

        st.write("select accumulated field!")
        acc_price_column, acc_volumn_column = st.columns([1, 1])

        selected_acc_price_field = acc_price_column.selectbox('Acc Price Field', df.keys(), index=None)
        selected_acc_volumn_field = acc_volumn_column.selectbox('Acc Volumn Field', df.keys(), index=None)

        if selected_acc_price_field is None or selected_acc_volumn_field is None:
            return

        converted_df = df.rename(columns={
            selected_market_field: "market",
            selected_time_field: "candleDateTimeUtc",
            selected_open_field: "openingPrice",
            selected_high_field: "highPrice",
            selected_low_field: "lowPrice",
            selected_close_field: "tradePrice",
            selected_acc_price_field: "candleAccTradePrice",
            selected_acc_volumn_field: "candleAccTradeVolume",
        })

        st.write(converted_df)

        converted_df['MA20'] = converted_df["tradePrice"].rolling(window=20).mean()
        converted_df['MA5'] = converted_df["tradePrice"].rolling(window=5).mean()

        write_candlestick(converted_df)

