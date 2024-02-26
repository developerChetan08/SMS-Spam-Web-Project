import streamlit as st
import pickle
import nltk

def transform_text(text):
    ##1)Lower case
    text = text.lower()

    ##2)Tokenization
    text = nltk.word_tokenize(text)

    ##3)Removing special characters
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    ##4)Removing stop words and punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    ##5)Stemming
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
modal = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_input("Enter the message")

#1.preprocess
transform_sms = transform_text(input_sms)

#2.vectorize
vector_input = tfidf.transform([transform_sms])

#3.predict
result = modal.predict(vector_input)[0]