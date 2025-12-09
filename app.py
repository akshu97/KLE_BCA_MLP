import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK data only once
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

# Load model and files
@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load("logistic_regression_sms_spam_model.pkl")
        vectorizer =

