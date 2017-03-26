import numpy as np
from sklearn.svm import SVC
from featureAdder import featureAdd
#from capture import *
#Import
from selenium import webdriver

driver = webdriver.Firefox()

def susPage():
    driver.get("/home/vishesh/Documents/BE-Project/Anti-Phishing-Using-Machine-Learning/index.html")

learnlist=[]
clf = SVC()

with open('list.txt', 'r') as f:
    for line in f:
        learnlist.append(featureAdd(line))
#print learnlist
#print len(learnlist)
X = np.array(learnlist)
#Adding the phishing learning set
y = [1]*2497

#Adding the normal phishing set
y.extend([0]*501)
#print y

clf.fit(X, y)

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
        res = clf.predict(featureAdd(url))
        print res
        if res != [0]:
            susPage()
        else:
            print "Not suspicious"
