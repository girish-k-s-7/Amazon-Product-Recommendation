import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model artifacts
user_factors = joblib.load("model/user_factors.npy")
item_factors = joblib.load("model/item_factors.npy")
user_map = joblib.load("model/user_map.pkl")
item_map = joblib.load("model/item_map.pkl")

# Load dataset
df = pd.read_csv(r"C:\Users\giris\Documents\datasets for practice\cleaned_amazon_reviews.csv")

# Build index mappings
user_index = {v: k for k, v in user_map.items()}
item_index = {v: k for k, v in item_map.items()}

# Filter dataset to known users/items
df = df[df['UserId'].isin(user_index) & df['ProductId'].isin(item_index)]

df['user_idx'] = df['UserId'].map(user_index)
df['item_idx'] = df['ProductId'].map(item_index)

# Prediction function
def predict_rating(user_idx, item_idx):
    return np.dot(user_factors[user_idx], item_factors[item_idx])


st.set_page_config(page_title="Amazon Recommender", layout="centered")
st.title("Amazon Product Recommendation System")

user_id = st.selectbox("Select a User ID", df['UserId'].unique())

top_n = st.slider("Number of recommendations", 5, 20, 10)

if st.button("Recommend"):
    user_idx = user_index[user_id]

    # Products already seen
    seen = set(df[df['user_idx'] == user_idx]['item_idx'])

    # Score unseen products
    scores = []
    for item_idx in range(item_factors.shape[0]):
        if item_idx not in seen:
            score = predict_rating(user_idx, item_idx)
            scores.append((item_idx, score))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top_items = scores[:top_n]

    st.subheader("Recommended Products")

    for idx, score in top_items:
        st.write(f"Product ID: {item_map[idx]}")
