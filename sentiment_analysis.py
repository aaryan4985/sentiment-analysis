import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Print a welcome message
print("Welcome to Sentiment Analysis!")

# Sample data
data = {
    'text': [
        "I love Python programming! It's so exciting.",
        "I hate bugs in the code.",
        "It's a sunny day and I'm feeling happy.",
        "This product is terrible. I want my money back!",
        "Life is a rollercoaster, full of ups and downs.",
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)
print(df)

# Function to analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)  
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Apply sentiment analysis to the text column
df['sentiment'] = df['text'].apply(analyze_sentiment)
print(df)