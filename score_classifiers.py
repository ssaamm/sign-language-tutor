from sklearn import svm
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn import neighbors, tree
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier

import asl

threshold = int(len(asl.data) * 0.8)
training_data = asl.data[:threshold]
training_target = asl.target[:threshold]

test_data = asl.data[threshold:]
test_target = asl.target[threshold:]

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
