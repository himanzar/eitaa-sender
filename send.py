# -*- coding: utf-8 -*-
import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys

TEXT = "سلام\nشما به کانال @getamira در ایتا دعوت شده اید"
OFFSET = 0

profile_path = "profile"
chrome_path = "../geckodriver/chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('user-data-dir='+profile_path)
browser = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)

browser.get('https://web.eitaa.com/')

input('inter any key to start advertising')
print("advertising started...\n")

for i in range(0, 1300790 - 1007991):

    browser.get("https://web.eitaa.com/#/im?p=u{}_1".format(i + 1007991 + OFFSET))
    time.sleep(7)
    try:
        text_box = browser.find_elements_by_css_selector('div.composer_rich_textarea')[0]
        text_box.click()
        text_box.send_keys(TEXT)
        text_box.send_keys(Keys.ENTER)
        time.sleep(2.5)
    except:
        continue


#filds=
#driver = webdriver.Firefox(executable_path=path)
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("http://www.google.com")
"""
# coded by @getamira
#What is Eitaa Sander?
#Eitaa Sender is a service that sends advertising spam with Eitaa Yar in Eitaa Messenger.
#
#In what language is Eitaa Sander programmed?
#Eitaa Sander is programmed in Python.
#
#Who is the programmer Eitaa Sander?
#We do not know either ...














