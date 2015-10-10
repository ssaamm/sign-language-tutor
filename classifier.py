'''
Usage:

    from classifier import clf
    clf.predict(test_data)
'''
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib

import asl

clf = GaussianNB()
clf.fit(asl.data, asl.target)
