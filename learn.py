import numpy as np
from sklearn.svm import SVC
#import pickle
from featureAdder import *
from sklearn.externals import joblib

#The dataset list
learnlist=[]

#declaring the kernel
clf = SVC(kernel = 'linear')

#reading the list.txt file to create the datasets
with open('list.txt', 'r') as f:
    for line in f:
        learnlist.append(featureAdd(line))

#Adding the dataset
X = np.array(learnlist)

#Adding the phishing labels
y = [1]*2497

#Adding the Non phishing labels
y.extend([0]*501)

#finding the pattern
clf.fit(X, y)

'''
s = pickle.dumps(clf)
clf2 = pickle.load(s)
clf2.predict(featureAdd("https://www.google.com"))
'''

#Saving for later purposes
joblib.dump(clf, 'learned.pkl')
