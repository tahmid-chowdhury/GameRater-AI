from requests_html import HTMLSession
from bs4 import BeautifulSoup

def scrape_reviews(game_url):
    url = f"{game_url}user-reviews/"
    
    session = HTMLSession()

    resp = session.get(url)
    resp.html.render(sleep=1)
    html = resp.html.html

    soup = BeautifulSoup(html, 'html.parser')

    game_title = soup.find('a', class_='c-productSubpageHeader_back').get_text(strip=True)

    output = []
    reviews = soup.find_all('div', class_='c-siteReview')
    for review in reviews:
        score = review.find('div', class_='c-siteReviewScore').get_text(strip=True)
        text = review.find('div', class_='c-siteReview_quote').get_text(strip=True)
        output.append({
            'score': score,
            'text': text
        })

    return {
        'game_title': game_title,
        'reviews': output
    }

# To test the function of the scraper:
# game_url = 'https://www.metacritic.com/game/minecraft/'
# result = scrape_reviews(game_url)
# print(result)