import streamlit as st
st.set_page_config(
    page_title= 'minecraft Detail',
    page_icon= 'minecraftemg.png'
)
tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10,tab11,tab12,tab13 = st.tabs(['창고','침실','엘베','통로','광산1','광산2','거래소',
                                         '밀농장','나무농장','포탈','마을','도서관','밀농장2'])
with tab1:
    st.header('창고')
    st.image('창고.png')

with tab2:
    st.header('침실')
    st.image('침실.png')

with tab3:
    st.header('엘베')
    st.image('엘베.png')

with tab4:
    st.header('통로')
    st.image('통로.png')


with tab5:
    st.header('광산1')
    st.image('광산.png')


with tab6:
    st.header('광산2')
    st.image('광산2.png')


with tab7:
    tab7.header('거래소')
    st.image('거래소.png')


with tab8:
    st.header('밀농장')
    st.image('밀농장.png')


with tab9:
    st.header('나무농장')
    st.image('나무팜.png')


with tab10:
    st.header('포탈')
    st.image('포탈.png')


with tab11:
    st.header('마을')
    st.image('마을.png')


with tab12:
    st.header('도서관')
    st.image('도서관.png')


with tab13:
    st.header('밀농장2')
    st.image('밀농장2.png')

