import requests

from bs4 import BeautifulSoup

URL = 'https://www.anekdot.ru/random/anekdot/'


def get_joke():
    response = requests.get(URL)

    bs = BeautifulSoup(response.text, 'html.parser')

    jokes = bs.findAll('div', 'topicbox')
    joke = jokes[1].find('div', 'text')

    joke_text_with_style = '\n'.join(joke.stripped_strings)

    return joke_text_with_style
