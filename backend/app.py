from flask import Flask, render_template, request
import scraper  # Your web scraper module
import sentiment_analysis  # Your sentiment analysis module
import generator  # Your AI-generated reviews module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_reviews', methods=['POST'])
def generate_reviews():
    game_title = request.form['game_title']
    reviews = scraper.scrape_reviews(game_title)
    sentiment_results = sentiment_analysis.analyze_sentiment(reviews)
    silly_reviews = generator.generate_review(sentiment_results)
    return render_template('index.html', reviews=reviews, silly_reviews=silly_reviews)

if __name__ == '__main__':
    app.run(debug=True)