import numpy as np
from sklearn.svm import SVC
import pickle
from featureAdder import *
from sklearn.externals import joblib

#The dataset list
learnlist=[]

def learning() :
    #No. of trusted websites
#    trustedWeb = 502

    #No. of Untrusted websites
#    untrustedWeb = 2497

    #Get the numbers of trusted websites and untrusted websites
    with open('objs.pickle', 'rb') as f:
        trustedWeb, untrustedWeb = pickle.load(f)

    f.close()

    #Write the the stats back to the dump
    trustedWeb += 1
    with open('objs.pickle', 'wb') as f2:
        pickle.dump([trustedWeb, untrustedWeb], f2)
    f2.close()

    #declaring the kernel
    clf = SVC(kernel = 'linear')

    #reading the list.txt file to create the datasets
    with open('list.txt', 'r') as f:
        for line in f:
            learnlist.append(featureAdd(line))

    #Adding the dataset
    X = np.array(learnlist)

    #Adding the phishing labels
    y = [0]*untrustedWeb

    #Adding the Non phishing labels
    y.extend([1]*trustedWeb)

    #finding the pattern
    clf.fit(X, y)

    '''
    s = pickle.dumps(clf)
    clf2 = pickle.load(s)
    print clf2.predict(featureAdd("https://www.google.com"))
    '''

    #Saving for later purposes
    joblib.dump(clf, 'learned.pkl')

learning()
