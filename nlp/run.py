import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt 

from sentiment.utils import PredictSentiment

def sentimentAnalysis():
    st.header('Sentiment Analysis')

    st.markdown("""
        This application contains a trained sentiment analysis model, capable of telling 
        whether a sentence is positive or negative. The data used to develop this model comes from 3 different
        sources, all of them being customers' reviews about the service/product they consumed.""")

    user_input = st.text_input("Write your sentence: ", ' ')
    inp_arr = [user_input]

    if st.button('Predict'):
        pred,prob,df_tokens=PredictSentiment().predict(inp_arr)
        st.header(user_input)
        if pred[0]==0:
            string = "{}% Negative!:thumbsdown:".format(round(prob,2))
            cmap='OrRd'
            df_tokens.Coef = df_tokens.Coef * -1
            st.header(string)
        else: 
            string = "{}% Positive!:thumbsup:".format(round(prob,2))
            cmap='Blues'
            st.header(string)

def artClass():
    """ 
    """

    st.title('Article classification')
    #st.header('Article classification')
    
    st.markdown("""
        This application reads an article of your preference and predicts its class. 
        The application use a random forest model trained with 2500 articles from BBC.
        
        The possible classes are: entretainment, politics, sports, business, and tech.""")

    st.write("The dataset used to train this model was retrieved from http://mlg.ucd.ie/datasets/bbc.html")

    uploaded_file = st.file_uploader("Upload your article HERE:",type=['txt'])

def spamDetection():

    st.title('Article classification')
    st.markdown("""
    This app tells if the text provided is prone to be spam or not spam. 

    """)
    

    my_expander = st.expander(label='Inspect Model', expanded=False)
    with my_expander:
        st.text(""" The data set contains 5572 labeled emails. Being 4825 Not spam and 747 spam.""")
        st.text("The model is a supporting vector machine trained with 80% of data and tested with the rest 20%.")
        st.text("As preprocesing step, TfIdf was used before training the model.")
        clicked = st.button("View model's performance")

def main():
    st.set_page_config(layout="wide")
    st.sidebar.header('Choose the NLP application:')
    app = st.sidebar.selectbox('Select:',['<select>','Sentiment Analysis','Article Classification','Spam Detection'])

    if app == 'Sentiment Analysis':
        sentimentAnalysis()
    
    if app == 'Article Classification':
        artClass()

    if app == 'Spam Detection':
        spamDetection()


if __name__ == "__main__":
    main()