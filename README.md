# Sentiment Marker

## Overwiew
The Sentiment Detector is a simple graphical user interface (GUI) application built using Python's tkinter library and the vaderSentiment package.
It allows users to input a sentence and analyze the sentiment by displaying the results in terms of positive, negative, neutral percentages, and an overall sentiment rating.

VADER is specifically tuned for sentiments expressed in social media and performs well with short, informal text and has an accuracy rate of around 90% for social media texts.
For other types of text, such as news articles or formal documents, VADER's accuracy might be lower, around 70-80%

## Features
- Input Text Area: A space where users can enter the sentence they wish to analyze.
- Sentiment Analysis: The application uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool to evaluate the input text.
- Result Display: It shows the percentage of positive, neutral, and negative sentiments in the text.
- Overall Sentiment: Provides an overall rating of the sentiment (Positive, Negative, Neutral).
- Clear Function: A button to clear all input and output fields.
- Exit Function: A button to exit the application.

## GUI 
<img width="185" alt="image" src="https://github.com/user-attachments/assets/9c693fe4-69dc-4d8f-9f59-74e12b116e12">

## Requirements
- Python: 3.x
- vaderSentiment: Sentiment Analysis tool; install using "!pip install vaderSentiment"
tkinter: Standard Python library for creating GUIs; install using "!pip install tkinter"

## How to Use
1) Setup: Ensure Python is installed on your system along with the vaderSentiment package.
2) Run the Application: Execute the Python script to open the GUI.
3) Input Sentence: Enter the sentence you wish to analyze in the text area.
4) Analyze Sentiment: Click the "Check Sentiment" button to process the input text.
5) View Results: The application displays the sentiment analysis results in the respective fields.
6) Clear Input/Output: Use the "Clear" button to reset the input and output fields.
