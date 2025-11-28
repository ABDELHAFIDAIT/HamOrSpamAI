import streamlit as st
import joblib
import numpy as np


model = joblib.load("models/best_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


