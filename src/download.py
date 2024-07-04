import os
import threading
import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

from src import utility


def get_ad_blocker():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, '..', 'files', 'adblocker.crx')


def _downloader(driver, link):
    driver.get(link)
    driver.refresh()

    button = driver.find_element(By.ID, "downloadbtn")
    try:
        button.click()
    except ElementClickInterceptedException as e:
        button.click()


def _download_multiple(links):
    options = ChromeOptions()
    options.add_argument("--no-headless")
    options.add_extension(get_ad_blocker())
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    original_window = driver.current_window_handle
    time.sleep(6)
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])
    driver.close()
    driver.switch_to.window(original_window)

    for link in links:
        _downloader(driver, link)


async def start_downloads(link):
    try:
        page = utility.get_page(link)
        links = utility.get_button_links(page)

        if links:
            threading.Thread(target=_download_multiple, args=(links,)).start()
    except Exception as e:
        print(e)
