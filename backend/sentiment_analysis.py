from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder
import ast

from scraper import scrape_reviews

def analyze_sentiment(input):
    data = input
    reviews = data['reviews']

    x = [review['text'] for review in reviews] 
    y = [int(review['score']) for review in reviews]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = make_pipeline(TfidfVectorizer(), MultinomialNB())

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred, zero_division=1)
    confusion_mat = confusion_matrix(y_test, y_pred)

    return {
        'accuracy': accuracy,
        'classification_report': classification_rep,
        'confusion_matrix': confusion_mat
    }

# To test the function of the sentiment analysis:
game_url = 'https://www.metacritic.com/game/minecraft/'
result = analyze_sentiment(scrape_reviews(game_url))
print(result)