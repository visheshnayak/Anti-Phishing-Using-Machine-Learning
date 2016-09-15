#!/usr/bin/python
from selenium import webdriver

#Get Which browser the user is using
driver = webdriver.Firefox()

#Get the current URL
url = driver.current_url

#Get the URL every time it changes
while (True):
    try:
        urllater = driver.current_url
    except selenium.common.exceptions.NoSuchWindowException :
        print("You have closed the browser.")

    if url != urllater :
        url = urllater
        print (url)
