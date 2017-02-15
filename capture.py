#!/usr/bin/python

#open file in order to write the URLs
f = open('URL.txt', 'w+')

#Import
from selenium import webdriver

#Get Which browser the user is using
driver = webdriver.Firefox()

#Get the current URL
url = driver.current_url

#Get the URL every time it changes
while (True):
    #try:
    urllater = driver.current_url
    #except selenium.NoSuchWindowException as e :
    #    print("You have closed the browser.")

    if url != urllater :
        url = urllater
        f.write(url + '\n')

#Close the File
f.close()
