import pandas as pd
import streamlit as st

from src.components.candlestick import write_candlestick


def write():
    with st.spinner("Loading Home ..."):
        # title
        st.write(
            """
            # Dataset
            """
        )

        # body
        # info
        st.write(
            """
            What is Lorem Ipsum?
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
            """
        )

        # file upload
        file = st.file_uploader("Choose a file")
        if file is None:
            return


        if file.type == 'text/csv':
            df = pd.read_csv(file)

        if file.type == 'application/json':
            df = pd.read_json(file)

        if file.type != 'text/csv' and file.type != 'application/json':
            st.write('Please json or csv!')
            return

        st.write(df)

        # select field
        st.write("Choose a market and time field")
        market_column, time_column = st.columns([1, 1])

        selected_market_field = market_column.selectbox('Market Field', df.keys(), index=None)
        selected_time_field = time_column.selectbox('Time Field', df.keys(), index=None)

        if selected_market_field is None or selected_time_field is None:
            return

        st.write("Choose a ohlc field")
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

        st.write("Choose a accumulated field")
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

        # chart
        write_candlestick(converted_df)

