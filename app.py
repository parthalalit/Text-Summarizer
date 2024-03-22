import streamlit as st
from textSummarizer.pipeline.prediction import PredictionPipeline
import os

def main():
    st.title("Text Summarization App")

    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Go to", ["Home", "Train", "Predict"])

    if app_mode == "Home":
        st.write("Welcome to the Text Summarization App!")
        st.write("You can train the model or use it to make predictions.")

    elif app_mode == "Train":
        st.write("Training...")
        try:
            os.system("python main.py")
            st.success("Training successful!")
        except Exception as e:
            st.error(f"Error occurred! {e}")

    elif app_mode == "Predict":
        st.subheader("Text Input")
        text = st.text_area("Enter the text you want to summarize:")
        if st.button("Summarize"):
            try:
                obj = PredictionPipeline()
                summary = obj.predict(text)
                st.subheader("Summary")
                st.write(summary)
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")

if __name__ == "__main__":
    main()
