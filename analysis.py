import numpy as np
from sklearn import svm

X = np.array( [Website1, feat1, feat2, feat3,..],
              [Website2, feat1, feat2, feat3,..]
              ...
)
Y = [Labels]

clf = svm.SVC(kernel='linear', C = 1.0)

clf.fit(X,Y)

print(clf.predict([website, features])) #Shows result
