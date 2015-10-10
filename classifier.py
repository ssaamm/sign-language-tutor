'''
Usage:

    from classifier import clf
    clf.predict(test_data)
'''
from sklearn import svm
from sklearn.externals import joblib

import asl

clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(asl.data, asl.target)
