import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("user-data-dir=reddit_Nicer4")
driver = webdriver.Chrome(options=chrome_options)

count=0

driver.get("https://www.reddit.com/user/haydenownsreddit/comments/grii2g/comment_nice/")
driver.set_window_size(1296, 741)
while True:
    driver.find_element(By.CSS_SELECTOR, ".usertext-edit:nth-child(2) textarea").click()
    driver.find_element(By.CSS_SELECTOR, ".usertext-edit:nth-child(2) textarea").send_keys("nice")
    driver.find_element(By.CSS_SELECTOR, ".usertext-edit:nth-child(2) .save").click()
    count+=1
    print(count)
    time.sleep(2)