import numpy as np
from sklearn import svm
from featureAdder import featureAdd

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
clf = svm.SVC(kernel='linear', C = 1.0)
with open('list.txt', 'r') as file:
    for url in file:
        learnlist.append(featureAdd(url))
        X = np.array( learnlist)
        Y = [1]
        clf.fit(X,Y)
