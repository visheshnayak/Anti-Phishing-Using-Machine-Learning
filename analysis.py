import numpy as np
from sklearn import svm
from selenium import webdriver

def captureURL():
    #Get Which browser the user is using
    driver = webdriver.Firefox()

    #Get the current URL
    url = driver.current_url

    #Get the URL every time it changes
    while (True):
        urllater = driver.current_url

        if url != urllater :
            url = urllater
            testURL = url
            return testURL

def analyzeURL():
    X = np.array( [Website1, feat1, feat2, feat3,..],
                  [Website2, feat1, feat2, feat3,..]
                  ...
    )
    Y = [Labels]

    clf = svm.SVC(kernel='linear', C = 1.0)

    clf.fit(X,Y)

    print(clf.predict([website, features])) #Shows result
