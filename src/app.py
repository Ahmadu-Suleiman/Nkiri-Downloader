from src import download
from src import utility

url = 'https://nkiri.com/hard-home-2024-download-hollywood-movie/'

page = utility.get_page(url)
links = utility.get_button_links(page)

if links:
    download.download_multiple(links)
