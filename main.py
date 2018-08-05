from bs4 import BeautifulSoup
import urllib.request
import logging
import requests

logger = logging.getLogger(__name__)

HOST = 'https://news.ycombinator.com/'

def parse_topic(data):

    pass


def parse_page():
    try:
        response = requests.get(HOST)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, features='html.parser')
            for item in soup.find_all('tr', class_='athing'):
                storylink_tag = item.find('a', class_='storylink')
                item_id = item['id']
                item_full_link = storylink_tag['href']
                item_host = urllib.request.splithost(item_full_link)[0]
                item_topic = storylink_tag.get_text()

                yield requests.get(HOST, params={'id': item_id})

                

    except Exception as err:
        logger.exception('Unexpected error')