import numpy as np
from sklearn.svm import SVC
from featureAdder import featureAdd
from capture import *

#def analyzeURL():
#    X = np.array( [Website1, feat1, feat2, feat3,..],
#                  [Website2, feat1, feat2, feat3,..]
#                  ...
#    )
#    Y = [Labels]
#
#    clf = svm.SVC(kernel='linear', C = 1.0)
#
#    clf.fit(X,Y)
#
#    print(clf.predict([website, features])) #Shows result


#to read url from the file one by one

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

checkURL = captureURL()

res = clf.predict(featureAdd(checkURL))
print res

if res != [0]:
    susPage()
else:
    print "Not suspicious"
