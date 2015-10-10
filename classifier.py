'''
Usage:

    from classifier import clf
    clf.predict(test_data)
'''
from sklearn import svm

import asl

clf = svm.SVC(gamma=0.0001, C=50)
clf.fit(asl.data, asl.target)
