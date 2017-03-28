#from sklearn.svm import SVC
from sklearn.externals import joblib
from featureAdder import featureAdd

from selenium import webdriver
driver = webdriver.Firefox()

#Redirect to the webpage
def susPage():
    #Redirect to the page
    driver.get("localhost:5000/")

def urlAnalysis() :
    #Load the learned pickle
    clf2 = joblib.load('learned.pkl')

    #Get the current URL
    url = driver.current_url

    #Get the URL every time it changes
    while (True):
        #Get the current URL
        urllater = driver.current_url
        if url != urllater :
            url = urllater

            #Open a file in order to write the current URL
            f = open('currenturl.txt', 'w')

            #Write the current URL into the file
            f.write(url)
            f.close()

            res = clf2.predict(featureAdd(url))
            print res

            if res != [0]:
                susPage()
            else:
                print "Not suspicious"
