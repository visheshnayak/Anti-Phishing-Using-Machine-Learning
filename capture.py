#Import
from selenium import webdriver

driver = webdriver.Firefox()

def susPage():
    driver.get("/home/vishesh/Documents/BE-Project/Anti-Phishing-Using-Machine-Learning/index.html")

def captureURL():
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
            return url
