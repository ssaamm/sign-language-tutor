from sklearn import svm, neighbors, tree
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.naive_bayes import GaussianNB, BernoulliNB

import asl

training_data, test_data, training_target, test_target = train_test_split(asl.data, asl.target, test_size=0.3, random_state=0)

classifiers = {
        'SVC': svm.SVC(gamma=0.001, C=100.),
        'NB ': GaussianNB(),
        'BNB': BernoulliNB(),
        'NBU': neighbors.KNeighborsClassifier(15, weights='uniform'),
        'NBD': neighbors.KNeighborsClassifier(15, weights='distance'),
        'TRE': tree.DecisionTreeClassifier(),
        'GBC': GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0),
        'RFC': RandomForestClassifier()
    }

for name, clf in classifiers.iteritems():
    print name, 'score:', clf.fit(training_data,
            training_target).score(test_data, test_target)
