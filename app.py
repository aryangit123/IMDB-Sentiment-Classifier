
import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_DIR = r"D:\projects\IMDB_Sentiment_Classifier\imdb_bert"

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
model.eval()

st.title("🎬 IMDb Sentiment Classifier")
st.write("Enter a movie review to predict its sentiment.")

review = st.text_area("Movie Review", placeholder="This movie was amazing...")

if st.button("Predict Sentiment"):
    if review.strip():
        inputs = tokenizer(
            review,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=256
        )

        with torch.no_grad():
            outputs = model(**inputs)
            probs = torch.softmax(outputs.logits, dim=1)[0]

        prediction = int(torch.argmax(probs).item())
        label = model.config.id2label.get(prediction, str(prediction))

        st.subheader(f"Sentiment: {label.upper()}")
        st.write(f"Confidence: {probs[prediction].item():.2%}")
    else:
        st.warning("Please enter a review.")
