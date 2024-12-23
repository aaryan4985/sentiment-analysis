# app.py
from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    # Convert polarity to sentiment and confidence
    if polarity > 0:
        sentiment = 'positive'
        confidence = min(abs(polarity) * 100, 100)
    elif polarity < 0:
        sentiment = 'negative'
        confidence = min(abs(polarity) * 100, 100)
    else:
        sentiment = 'neutral'
        confidence = 100
    
    return sentiment, round(confidence)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    sentiment, confidence = analyze_sentiment(text)
    
    return render_template('index.html',
                         text=text,
                         sentiment=sentiment,
                         confidence_score=confidence)

if __name__ == '__main__':
    app.run(debug=True)