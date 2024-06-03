import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots
from ta.momentum import StochasticOscillator
from ta.trend import MACD


def write_candlestick(df: pd.DataFrame):
    # initialize
    fig = make_subplots(
        rows=4,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.01,
        row_heights=[0.5, 0.1, 0.2, 0.2],
    )

    # OHLC chart
    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df['openingPrice'],
            high=df['highPrice'],
            low=df['lowPrice'],
            close=df['tradePrice'],
            name="Main",
            showlegend=False
        ),
    )

    # MA chart
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['MA5'],
            line=dict(color='blue', width=2),
            name='MA 5',
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['MA20'],
            line=dict(color='orange', width=2),
            name='MA 20',
        )
    )

    # Volume chart
    colors = ['green' if row['openingPrice'] - row['tradePrice'] >= 0
          else 'red' for index, row in df.iterrows()]

    fig.add_trace(
        go.Bar(
            x=df.index,
            y=df['candleAccTradeVolume'],
            marker_color=colors,
        ),
        row=2,
        col=1,
    )

    # MACD chart
    macd = MACD(
        close=df['tradePrice'],
        window_slow=26,
        window_fast=12,
        window_sign=9
    )

    colors = ['green' if val >= 0
          else 'red' for val in macd.macd_diff()]

    fig.add_trace(
        go.Bar(
            x=df.index,
            y=macd.macd_diff(),
            marker_color=colors,
        ),
        row=3,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=macd.macd(),
            line=dict(color='black', width=2)
        ),
        row=3,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=macd.macd_signal(),
            line=dict(color='blue', width=1)
        ),
        row=3,
        col=1,
    )

    # Stochastics chart
    stoch = StochasticOscillator(
        high=df['highPrice'],
        close=df['tradePrice'],
        low=df['lowPrice'],
        window=14,
        smooth_window=3,
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=stoch.stoch(),
            line=dict(color='black', width=2),
        ),
        row=4,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=stoch.stoch_signal(),
            line=dict(color='blue', width=1),
        ),
        row=4,
        col=1,
    )

    # Update layout and label
    dt_all = pd.date_range(
        start=df.index[0],
        end=df.index[99]
    )
    dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(df.index)]
    dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]


    fig.update_layout(
        height=1000,
        # width=1500,
        showlegend=False,
        xaxis_rangeslider_visible=False,
        xaxis_rangebreaks=[dict(values=dt_breaks)]
    )

    fig.update_yaxes(title_text="Price", row=1, col=1)
    fig.update_yaxes(title_text="Volume", row=2, col=1)
    fig.update_yaxes(title_text="MACD", showgrid=False, row=3, col=1)
    fig.update_yaxes(title_text="Stoch", row=4, col=1)

    st.write(fig)
