from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tkinter import *
from tkinter import messagebox

# Function to clear all input and output fields
def clearAll():
    negativeField.config(state=NORMAL)
    neutralField.config(state=NORMAL)
    positiveField.config(state=NORMAL)
    overallField.config(state=NORMAL)
    
    negativeField.delete(0, END)
    neutralField.delete(0, END)
    positiveField.delete(0, END)
    overallField.delete(0, END)
    textArea.delete(1.0, END)
    
    negativeField.config(state=DISABLED)
    neutralField.config(state=DISABLED)
    positiveField.config(state=DISABLED)
    overallField.config(state=DISABLED)

# Sentiment Detection Function
def detect_sentiment():
    sentence = textArea.get("1.0", "end").strip()
    if not sentence:
        messagebox.showwarning("Input Error", "Please enter some text to analyze.")
        return

    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    
    negativeField.config(state=NORMAL)
    neutralField.config(state=NORMAL)
    positiveField.config(state=NORMAL)
    overallField.config(state=NORMAL)
    
    negativeField.delete(0, END)
    neutralField.delete(0, END)
    positiveField.delete(0, END)
    overallField.delete(0, END)
    
    negativeField.insert(10, f"{sentiment_dict['neg']*100:.2f}% Negative")
    neutralField.insert(10, f"{sentiment_dict['neu']*100:.2f}% Neutral")
    positiveField.insert(10, f"{sentiment_dict['pos']*100:.2f}% Positive")
    
    if sentiment_dict['compound'] >= 0.05:
        overallField.insert(10, "😊 Positive")
    elif sentiment_dict['compound'] <= -0.05:
        overallField.insert(10, "😔 Negative")
    else:
        overallField.insert(10, "😐 Neutral")
    
    negativeField.config(state=DISABLED)
    neutralField.config(state=DISABLED)
    positiveField.config(state=DISABLED)
    overallField.config(state=DISABLED)

# GUI Setup
gui = Tk()
gui.config(background="#f0f8ff")
gui.title("Sentiment Marker")
gui.geometry("500x550")
gui.resizable(False, False)

guiFrame = Frame(gui, bg="#f0f8ff", padx=20, pady=20)
guiFrame.pack(expand=True)

custom_font = ("Arial", 12, "bold")
custom_entry_font = ("Arial", 10)

Label(guiFrame, text="Enter Your Sentence", bg="#f0f8ff", font=custom_font).pack(pady=5)
textArea = Text(guiFrame, height=5, width=50, font=custom_entry_font, borderwidth=1, relief="solid")
textArea.pack(pady=5)

Button(guiFrame, text="Check Sentiment", fg="white", bg="#4682B4", font=custom_font, command=detect_sentiment).pack(pady=10)

# Create fields with proper margins
for text in ["Negative Score:", "Neutral Score:", "Positive Score:"]:
    Label(guiFrame, text=text, bg="#f0f8ff", font=custom_font).pack(pady=3)
    entry = Entry(guiFrame, state=DISABLED, font=custom_entry_font, borderwidth=1, relief="solid", justify=CENTER)
    entry.pack(pady=3, ipadx=5, ipady=3)
    
    if "Negative" in text:
        negativeField = entry
    elif "Neutral" in text:
        neutralField = entry
    elif "Positive" in text:
        positiveField = entry

# Special Box for Overall Sentiment (Larger)
Label(guiFrame, text="Overall Sentiment:", bg="#f0f8ff", font=custom_font).pack(pady=5)
overallField = Entry(guiFrame, state=DISABLED, font=("Arial", 14, "bold"), borderwidth=2, relief="solid", justify=CENTER, width=35)
overallField.pack(pady=5, ipadx=10, ipady=8)

# Buttons Section
frame_buttons = Frame(guiFrame, bg="#f0f8ff")
frame_buttons.pack(pady=10)
Button(frame_buttons, text="Clear", fg="white", bg="#FF8C00", font=custom_font, command=clearAll).pack(side=LEFT, padx=10)
Button(frame_buttons, text="Exit", fg="white", bg="#B22222", font=custom_font, command=gui.destroy).pack(side=RIGHT, padx=10)

gui.mainloop()
