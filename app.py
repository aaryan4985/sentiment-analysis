from flask import Flask, render_template, request
from transformers import pipeline

# Initialize the sentiment analysis pipeline with a pre-trained model
sentiment_analyzer = pipeline("sentiment-analysis")

app = Flask(__name__)

# Function to analyze sentiment
def analyze_sentiment(text):
    result = sentiment_analyzer(text)[0]
    return result['label'], result['score']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    sentiment, score = analyze_sentiment(text)
    return render_template('index.html', sentiment=sentiment, score=score, text=text)

if __name__ == '__main__':
    app.run(debug=True)
