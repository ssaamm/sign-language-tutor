import asl

from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC

n_samples = len(asl.data)
X = asl.data
y = asl.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5,
        random_state=0)

#tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4], 'C': [1, 10, 100,
#    1000]}, {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [0.001, 0.00055, 0.0001], 'C':
    [10, 50, 100]}]

for score in ['precision', 'recall']:
    clf = GridSearchCV(SVC(C=1), tuned_parameters, cv=5, scoring='%s_weighted' %
            score)
    clf.fit(X_train, y_train)

    print score, clf.best_params_
