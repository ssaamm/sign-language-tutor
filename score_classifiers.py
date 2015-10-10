from sklearn import svm
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.externals import joblib

import asl

threshold = int(len(asl.data) * 0.8)
training_data = asl.data[:threshold]
training_target = asl.target[:threshold]

test_data = asl.data[threshold:]
test_target = asl.target[threshold:]

classifiers = {
        'SVC': svm.SVC(gamma=0.001, C=100.),
        'NB': GaussianNB(),
        'BNB': BernoulliNB(),
    }

for name, clf in classifiers.iteritems():
    print name, 'score:', clf.fit(training_data,
            training_target).score(test_data, test_target)
