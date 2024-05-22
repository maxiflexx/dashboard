import pandas as pd
import streamlit as st

from src.core.services.api_client import data_io_client


# 모달은 x, esc외 종료되면 다시 re_run됨 -> 버튼이 있을 경우 함수가 두번 호출된다는 뜻
# test 함수는 콜백에 할당된 함수이므로 test 함수에는 콜백 빼자
# https://discuss.streamlit.io/t/menu-between-multipages-calling-st-rerun-within-a-callback-is-a-no-op/53827
@st.experimental_dialog("Market crawl")
def crawl_dialog(**kwargs):
    df = pd.DataFrame(kwargs)
    if "markets" in st.session_state:
        row_numer = list(st.session_state["markets"]["edited_rows"].keys())[0]
        row = df.loc[row_numer]

        market_code = row["code"]
        name = row['englishName']
        is_enabled = st.session_state["markets"]["edited_rows"][row_numer]['isEnabled']

        data_io_client.put_json(f'/markets/{market_code}', {
            "isEnabled": is_enabled,
        })

        if is_enabled:
            st.write(f'{name} start crawling')
        else:
            st.write(f'{name} ends crawling')




def write_table(df: pd.DataFrame):
    df['image'] = df['code'].apply(lambda x: f'http://localhost:3001/public/{x.split("-")[1]}.png')

    new_column_order = ['image', 'code', 'koreanName', 'englishName', 'isEnabled']
    st.data_editor(
        df,
        column_order=new_column_order,
        column_config={
            "image": st.column_config.ImageColumn(
                "Logo",
            ),
            "code": st.column_config.Column(
                "Market",
                disabled=True,
            ),
            "koreanName": st.column_config.Column(
                "Korean Name",
                disabled=True,
            ),
            "englishName": st.column_config.Column(
                "English Name",
                disabled=True,
            ),
            "isEnabled": st.column_config.CheckboxColumn(
                "Enabled",
                help="check is good",
                default=False,
            ),
        },
        hide_index=True,
        kwargs=df.to_dict(),
        on_change=crawl_dialog,
        use_container_width=True,
        key='markets'
    )

