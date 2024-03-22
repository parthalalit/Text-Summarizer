#from fastapi import FastAPI
#import uvicorn
import sys
import os
#from fastapi.templating import Jinja2Templates
#from starlette.responses import RedirectResponse
#from fastapi.responses import Response
import streamlit as st 
from textSummarizer.pipeline.prediction import PredictionPipeline


def main():
    # Set title and description
    st.title('Text Summarizer App')
    st.write('This is an end-to-end text summarizer pipeline.')

    # Load your model or initialize your pipeline
    summarizer = PredictionPipeline()

    # Add user input for text to be summarized
    text_input = st.text_area('Enter text to summarize:', '')

    # Add a button to trigger the summarization
    if st.button('Summarize'):
        # Perform summarization
        summary = summarizer.summarize(text_input)

        # Display the summary
        st.subheader('Summary:')
        st.write(summary)

if __name__ == '__main__':
    main()