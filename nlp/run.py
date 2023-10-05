import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt 


def main():
    st.set_page_config(layout="wide")
    st.sidebar.header('Choose the NLP application:')
    app = st.sidebar.selectbox('Select:',['Review Analysis','Article Classification','Spam Detection'])

    # if app == 'Review Analysis':
    #     revAnalysis()
    
    # if app == 'Article Classification':
    #     artClass()

    # if app == 'Spam Detection':
    #     spamDetection()


if __name__ == "__main__":
    main()