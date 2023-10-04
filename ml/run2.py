import streamlit as st

def main():
    st.set_page_config(layout="wide")
    st.sidebar.header('Choose the Machine learning application:')
    values = ['<select>','House prices']
    app = st.sidebar.selectbox('Select:',values)

    # if app == 'House prices':
    #     housePrices()

if __name__ == "__main__":
    main()