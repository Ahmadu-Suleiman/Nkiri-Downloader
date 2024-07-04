import requests
from bs4 import BeautifulSoup

from src import download


def get_page(_url):
    response = requests.get(_url, verify=False)
    # Check if the request was successful
    if response.status_code == 200:
        # The page was successfully fetched
        html_content = response.text
        return html_content
    else:
        return f"Failed to fetch the page. Status code: {response.status_code}"


def get_button_links(html_content):
    _links = []
    soup = BeautifulSoup(html_content, 'html.parser')
    all_anchor_tags = soup.find_all('a')

    for tag in all_anchor_tags:
        _link = tag.get('href')
        if _link.endswith('.mkv.html'):
            _links.append(_link)
    return _links
