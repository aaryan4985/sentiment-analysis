from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    sentiment = analyze_sentiment(text)
    return render_template('index.html', sentiment=sentiment, text=text)

if __name__ == '__main__':
    app.run(debug=True)
