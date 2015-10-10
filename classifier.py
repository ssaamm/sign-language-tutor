'''
Usage:

    from classifier import clf
    clf.predict(test_data)
'''
from sklearn import svm
from sklearn.externals import joblib

FILENAME = 'clf.pkl'

try:
    clf = joblib.load(FILENAME)
except:
    import asl
    clf = svm.SVC(gamma=0.0001, C=50, probability=True)
    clf.fit(asl.data, asl.target)
    joblib.dump(clf, FILENAME)
