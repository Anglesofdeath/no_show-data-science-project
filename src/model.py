import logging
import yaml
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection._split import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.svm import SVC
from src.cleaning_engineering_functions import read_yaml

class Model:
    def __init__(self, data) -> None:
        self.data = data

        self.logger = logging.getLogger(__name__)

    def build_model_random_forest(self):
        config_file = read_yaml("src/conf/config.yaml")
        if config_file['RandomForest']['Run'] == False:
            self.logger.info("Random Forest Skipped")
            return
        self.logger.info("Running Random Forest")
        drop_columns_name = ["price", "no_show", "checkout_month", "booking_month", "checkout_day", "booking_id"]
        X = self.data.drop(drop_columns_name, axis = 1)

        y = self.data["no_show"]

        enc = OneHotEncoder(handle_unknown="ignore")
        encoder_df = pd.DataFrame(enc.fit_transform(X[['branch', 'first_time', 'country', 'room', 'arrival_month', 'platform', 'arrival_day']]).toarray())
        X.reset_index()
        encoder_df.reset_index()
        X = X.join(encoder_df)
        X = X.drop(['branch', 'first_time', 'country', 'room', 'arrival_month', 'platform', 'arrival_day'], axis = 1)
        X_train, X_test, y_train, y_test = train_test_split(
            encoder_df, y, test_size=0.2, random_state=2
        )

        #checking if run GridSearch -- based on config setting
        if config_file['RandomForest']['GridCV'] == True:
            self.logger.info("Running Grid CV")
            pipe = Pipeline([('classifier' , RandomForestClassifier())])

            param_grid = [
                {'classifier' : [RandomForestClassifier()],
                'classifier__max_depth': list(range(5, 25))} 
            ]

            # Create grid search object

            clf = GridSearchCV(pipe, param_grid = param_grid, cv = 2, verbose=True, n_jobs=-1, scoring = 'accuracy')

            # Fit on data

            best_clf = clf.fit(X_train, y_train)
            y_pred = best_clf.predict(X_test)
            print("best params:")
            print(clf.best_params_)
        else:
            self.logger.info("Grid CV skipped")
            clf = RandomForestClassifier(max_depth = config_file['RandomForest']['MaxDepth'], random_state=42)
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)
            
        self.logger.info(f"Accuracy score: {accuracy_score(y_test, y_pred)}")
        self.logger.info(f"f1 score: {f1_score(y_test, y_pred, average='macro')}")

    def build_model_logistic_regression(self):
        config_file = read_yaml("src/conf/config.yaml")
        if config_file['Logistic']['Run'] == False: #check if user wants to run Logistic Regression -- based on config file
            self.logger.info("Logistic Regression Skipped")
            return
        self.logger.info("Running Logistic Regression")
        drop_columns_name = ["price", "no_show", "checkout_month", "booking_month", "checkout_day", "booking_id"]
        X = self.data.drop(drop_columns_name, axis = 1)

        y = self.data["no_show"]

        enc = OneHotEncoder(handle_unknown="ignore")
        encoder_df = pd.DataFrame(enc.fit_transform(X[['branch', 'first_time', 'country', 'room', 'arrival_month', 'platform', 'arrival_day']]).toarray())
        X.reset_index()
        encoder_df.reset_index()
        X = X.join(encoder_df)
        X = X.drop(['branch', 'first_time', 'country', 'room', 'arrival_month', 'platform', 'arrival_day'], axis = 1)
        X_train, X_test, y_train, y_test = train_test_split(
            encoder_df, y, test_size=0.2, random_state=2
        )
        #checking if run GridSearch -- based on config file
        if config_file['Logistic']['GridCV'] == True:
            self.logger.info("Running Grid CV")
            pipe = Pipeline([('classifier' , LogisticRegression())])
            param_grid = [
                {'classifier' : [LogisticRegression()],
                    'classifier__penalty' : ['l2'],
                    'classifier__solver': ['liblinear', 'lbfgs', 'newton-cg'],
                    'classifier__C':[0.001, 0.009, 0.01, .09, 0.25, 0.5, 0.75, 1, 5, 10, 25]}
            ]
            # Create grid search object

            clf = GridSearchCV(pipe, param_grid = param_grid, cv = 2, verbose=True, n_jobs=-1, scoring = 'accuracy')

            # Fit on data

            best_clf = clf.fit(X_train, y_train)
            y_pred = best_clf.predict(X_test)
            print("best params:")
            print(clf.best_params_)
        else:
            self.logger.info("Grid CV skipped")
            clf = LogisticRegression(penalty = config_file['Logistic']['Penalty'], C = config_file['Logistic']['C'], solver = config_file['Logistic']['Solver'], random_state=42)
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)

        self.logger.info(f"Accuracy score: {accuracy_score(y_test, y_pred)}")
        self.logger.info(f"f1 score: {f1_score(y_test, y_pred, average='macro')}")

    def build_model_SVM(self):
        config_file = read_yaml("src/conf/config.yaml")
        if config_file['SVM']['Run'] == False:
            self.logger.info("SVM Skipped")
            return
        self.logger.info("Running SVM")
        drop_columns_name = ["price", "no_show", "checkout_month", "booking_month", "checkout_day", "booking_id"]
        X = self.data.drop(drop_columns_name, axis = 1)

        y = self.data["no_show"]

        enc = OneHotEncoder(handle_unknown="ignore")
        encoder_df = pd.DataFrame(enc.fit_transform(X[['branch', 'first_time', 'country', 'room', 'arrival_month', 'platform', 'arrival_day']]).toarray())
        X.reset_index()
        encoder_df.reset_index()
        X = X.join(encoder_df)
        X = X.drop(['branch', 'first_time', 'country', 'room', 'arrival_month', 'platform', 'arrival_day'], axis = 1)
        X_train, X_test, y_train, y_test = train_test_split(
            encoder_df, y, test_size=0.2, random_state=2
        )
        if config_file['SVM']['GridCV'] == True:
            self.logger.info("Running Grid CV")
            pipe = Pipeline([('classifier' , SVC())])


            param_grid = [
                {'classifier' : [SVC()],
                'classifier__kernel': ['poly', 'sigmoid']}, # 'rbf' wasn't used because its too complicated and takes too long
            ]

            # Create grid search object

            clf = GridSearchCV(pipe, param_grid = param_grid, cv = 2, verbose=True, n_jobs=-1)

            # Fit on data

            best_clf = clf.fit(X_train, y_train)
            y_pred = best_clf.predict(X_test)
        else:
            self.logger.info("Grid CV skipped")
            clf = SVC(random_state=42)
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)
        
        self.logger.info(f"Accuracy score: {accuracy_score(y_test, y_pred, average='macro')}")
        self.logger.info(f"f1 score: {f1_score(y_test, y_pred, average='macro')}")