import os
import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


def get_ad_blocker():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, '..', 'files', 'adblocker.crx')


options = ChromeOptions()
options.add_argument("--no-headless")
options.add_extension(get_ad_blocker())
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

time.sleep(6)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
driver.close()


def _downloader(link):
    driver.get(link)
    driver.refresh()

    button = driver.find_element(By.ID, "downloadbtn")
    try:
        button.click()
    except ElementClickInterceptedException as e:
        button.click()


def download_multiple(links):
    for link in links:
        _downloader(link)
