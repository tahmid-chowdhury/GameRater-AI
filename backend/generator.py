import random
from scraper import scrape_reviews
from sentiment_analysis import analyze_sentiment

def generate_review(sentiment_results, reviews):
    accuracy = sentiment_results['accuracy']
    classification_report = sentiment_results['classification_report']
    confusion_matrix = sentiment_results['confusion_matrix']

    if accuracy < 0.5:
        return "The AI is not feeling very confident today. Better luck next time!"

    sentiment_category = determine_sentiment_category(confusion_matrix)

    if sentiment_category == 'positive':
        return generate_positive_review(reviews)
    elif sentiment_category == 'negative':
        return generate_negative_review(reviews)
    else:
        return generate_neutral_review(reviews)

def determine_sentiment_category(confusion_matrix):
    if confusion_matrix[3, 3] > 0:
        return 'positive'
    elif confusion_matrix[0, 0] > 0 or confusion_matrix[1, 1] > 0:
        return 'negative'
    else:
        return 'neutral'

def generate_positive_review(reviews):
    positive_templates = [
        "Wow, the AI thinks this game is a masterpiece! It must be as legendary as a dragon in a tuxedo.",
        "The AI is so positive about this game that it's considering building a themed spaceship to explore the cosmos."
    ]
    return random.choice(positive_templates)

def generate_negative_review(reviews):
    negative_templates = [
        "The AI is disappointed in this game. It's like trying to fight a dragon with a wooden sword - frustrating!",
        "Oh no! The AI expected this game to be as exciting as a llama disco party on Saturn, but it's more like a snooze fest."
    ]
    return random.choice(negative_templates)

def generate_neutral_review(reviews):
    neutral_templates = [
        "The AI is feeling neutral about this game. It's neither a rainbow-colored cheese labyrinth nor a marshmallow pillow fight.",
        "The AI is as indifferent as a rubber chicken wearing tap shoes. This game is just there, existing."
    ]
    return random.choice(neutral_templates)
    
# To test the function of the review generator:
game_url = 'https://www.metacritic.com/game/alan-wake-ii/'
result = generate_review(analyze_sentiment(scrape_reviews(game_url)), scrape_reviews(game_url))
print(result)