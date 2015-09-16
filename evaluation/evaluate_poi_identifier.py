#!/usr/bin/python


"""
    starter code for the validation mini-project
    the first step toward building your POI identifier!

    start by loading/formatting the data

    after that, it's not our code anymore--it's yours!
"""

import pickle
import sys
import pandas as pd
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, random_state=42, test_size=0.3)

### it's all yours from here forward!  
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
clf.score(features_test, labels_test)
pred_test = clf.predict(features_test)

print confusion_matrix(labels_test, pred_test)
print "Precision score: " + str(precision_score(labels_test, pred_test))
print "Recall score: " + str(recall_score(labels_test, pred_test))

predictions =  pd.Series([0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1])
true_labels =  pd.Series([0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0])

print pd.crosstab(true_labels, predictions, rownames=['True'], colnames=['Predicted'], margins=True)