import streamlit as st
from textSummarizer.pipeline.prediction import PredictionPipeline
import subprocess

text = "What is Text Summarization?"

# Initialize the prediction pipeline object
prediction_pipeline = PredictionPipeline()

# Define the Streamlit app
def main():
    st.title('Text Summarization App')

    # Redirect to documentation
    if st.button('Go to Documentation'):
        st.experimental_set_query_params()
        st.experimental_rerun()

    # Train the model
    if st.button('Train Model'):
        try:
            subprocess.run(["python", "main.py"])
            st.write("Training successful!")
        except Exception as e:
            st.error(f"Error occurred during training: {e}")

    # Input text for prediction
    input_text = st.text_input('Enter text for prediction', text)

    # Predict
    if st.button('Predict'):
        try:
            summary = prediction_pipeline.predict(input_text)
            st.subheader('Summary')
            st.write(summary)
        except Exception as e:
            st.error(f"Error occurred during prediction: {e}")

if __name__ == '__main__':
    main()
