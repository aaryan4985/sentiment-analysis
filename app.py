from flask import Flask, render_template, request

app = Flask(__name__)

# Function to analyze sentiment using a simple keyword-based approach
def analyze_sentiment(text):
    positive_keywords = ['good', 'great', 'excellent', 'happy', 'positive', 'awesome', 'fantastic']
    negative_keywords = ['bad', 'terrible', 'sad', 'negative', 'awful', 'horrible', 'poor']

    text_lower = text.lower()
    positive_count = sum(keyword in text_lower for keyword in positive_keywords)
    negative_count = sum(keyword in text_lower for keyword in negative_keywords)

    if positive_count > negative_count:
        return 'POSITIVE', positive_count
    elif negative_count > positive_count:
        return 'NEGATIVE', negative_count
    else:
        return 'NEUTRAL', 0

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
