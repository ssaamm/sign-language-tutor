'''
Usage:

    from classifier import clf
    clf.predict(test_data)
'''
from sklearn import neighbors

import asl

clf = neighbors.KNeighborsClassifier(15, weights='distance')
clf.fit(asl.data, asl.target)
