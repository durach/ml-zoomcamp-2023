#!/usr/bin/env python

import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer


df = pd.read_csv('heart.csv')
df.columns = df.columns.str.lower()

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)

df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_full_train = df_full_train.heartdisease.values
y_test = df_test.heartdisease.values

del df_full_train['heartdisease']
del df_test['heartdisease']

full_train_dicts = df_full_train.to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X_full_train = dv.fit_transform(full_train_dicts) 

test_dicts = df_test.to_dict(orient='records')
X_test = dv.transform(test_dicts)

model = RandomForestClassifier(n_estimators=200, max_depth=10, min_samples_leaf=1, random_state=42)
model.fit(X_full_train, y_full_train)

f_out = open('model_cli.bin', 'wb') 
pickle.dump((dv, model), f_out)
f_out.close()
