import gradio as gr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    
    negative = f"{scores['neg']*100:.2f}%"
    neutral = f"{scores['neu']*100:.2f}%"
    positive = f"{scores['pos']*100:.2f}%"
    overall_sentiment = "😊 Positive" if scores["compound"] >= 0.05 else "😔 Negative" if scores["compound"] <= -0.05 else "😐 Neutral"
    
    return negative, neutral, positive, overall_sentiment

# Create a Gradio interface
demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(placeholder="Enter text for sentiment analysis..."),
    outputs=[
        gr.Textbox(label="Negative"),
        gr.Textbox(label="Neutral"),
        gr.Textbox(label="Positive"),
        gr.Textbox(label="Overall Sentiment")
    ]
)

# Run the app
demo.launch()
