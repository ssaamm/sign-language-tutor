from sklearn import svm, neighbors, tree
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.naive_bayes import GaussianNB, BernoulliNB

import collections

import asl

training_data, test_data, training_target, test_target = train_test_split(asl.data, asl.target, test_size=0.5, random_state=0)

classifiers = {
        'SVCP': svm.SVC(gamma=0.001, C=10),
        'SVCR': svm.SVC(gamma=0.0001, C=50),
        'NB ': GaussianNB(),
        'BNB': BernoulliNB(),
        'NBU': neighbors.KNeighborsClassifier(5, weights='uniform'),
        'NBD': neighbors.KNeighborsClassifier(5, weights='distance'),
        'TRE': tree.DecisionTreeClassifier(),
        'GBC': GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0),
        'RFC': RandomForestClassifier()
    }

scores = [(n, clf.fit(training_data, training_target).score(test_data,
    test_target)) for n, clf in classifiers.iteritems()]

for name, score in sorted(scores, key=lambda t: t[1], reverse=True):
    print name, score
