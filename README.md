# Sentiment Marker

## Overwiew
The Sentiment Marker is a web-based sentiment analysis tool built using Gradio and VADER Sentiment Analysis. It allows users to input text and instantly analyze its sentiment.

VADER (Valence Aware Dictionary and sEntiment Reasoner) is specifically designed for social media and short-form text, achieving around 90% accuracy for such content. For news articles or formal documents, accuracy may range between 70-80%.

## Features
- Input Text Area: A space where users can enter the sentence they wish to analyze.
- Sentiment Analysis: The application uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool to evaluate the input text.
- Result Display: It shows the percentage of positive, neutral, and negative sentiments in the text.
- Overall Sentiment: Provides an overall rating of the sentiment (Positive, Negative, Neutral).
- Clear Function: A button to clear all input and output fields.
- Exit Function: A button to exit the application.

## GUI 
<img width="842" alt="image" src="https://github.com/user-attachments/assets/d7903cdf-992f-45cd-a89a-eeba9f07482a" />

## Demo
https://huggingface.co/spaces/vanshika-garg/sentiment-marker
   

## Requirements
- Python: 3.x
- vaderSentiment (for sentiment analysis)
- gradio (for the interface)

## How to Use
1) Setup: Ensure Python is installed on your system along with the vaderSentiment package.
2) Run the Application: Execute the Python script to open the GUI.
3) Input Sentence: Enter the sentence you wish to analyze in the text area.
4) Analyze Sentiment: Click the "Check Sentiment" button to process the input text.
5) View Results: The application displays the sentiment analysis results in the respective fields.
6) Clear Input/Output: Use the "Clear" button to reset the input and output fields.
