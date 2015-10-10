from sklearn import svm
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.externals import joblib
from sklearn.cross_validation import train_test_split

import asl

training_data, test_data, training_target, test_target = train_test_split(asl.data, asl.target, test_size=0.3, random_state=0)

classifiers = {
        'SVC': svm.SVC(gamma=0.001, C=100.),
        'NB': GaussianNB(),
        'BNB': BernoulliNB(),
    }

for name, clf in classifiers.iteritems():
    print name, 'score:', clf.fit(training_data,
            training_target).score(test_data, test_target)
