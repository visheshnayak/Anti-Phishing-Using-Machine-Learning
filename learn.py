import numpy as np
from sklearn.svm import SVC
import pickle
from featureAdder import *
from sklearn.externals import joblib

#The dataset list
learnlist=[]

def learning() :
    '''
    #No. of trusted websites
    #trustedWeb = 503

    #No. of Untrusted websites
    #untrustedWeb = 28371
    '''
    #Get the numbers of trusted websites and untrusted websites
    with open('objs.pickle', 'rb') as getStats:
        trustedWeb = pickle.load(getStats)
    getStats.close()

    #trustedWeb = 503
    #Write the the stats back to the dump
    #trustedWeb += 1
    with open('objs.pickle', 'wb') as putStats:
        pickle.dump( trustedWeb, putStats)
    putStats.close()

    #declaring the kernel
    clf = SVC()

    #reading the csv file with phishing datasets
    with open('verified_online.csv', 'r') as untrustedReserve:
        for line in untrustedReserve:
            learnlist.append( featureAdd(line) )

    #print learnlist
    untrustedReserve.close()

    #reading the trusted urls
    with open('verified_offline.csv', 'r') as trustedReserve:
        for line in trustedReserve:
            learnlist.append( featureAdd(line) )

    print learnlist
    trustedReserve.close()

    #Adding the dataset
    X = np.array(learnlist)

    #Adding the phishing labels
    y = [1]*28371

    #Adding the Non phishing labels
    y.extend([0]*trustedWeb)

    #finding the pattern
    clf.fit(X, y)

    #s = pickle.dumps(clf)
    #clf2 = pickle.load(s)
    #print clf2.predict(featureAdd("https://www.google.com"))

    #Saving for later purposes
    joblib.dump(clf, 'learned.pkl')

#learning()
