#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 21:03:03 2021

@author: abhishekr
"""

import nltk
from nltk.stem import PorterStemmer
import re
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import pandas as pd



#Importing dataset 
dataset=pd.read_csv("spam.csv", encoding='latin-1')
dataset = dataset.loc[:, ~dataset.columns.str.contains('^Unnamed')]
dataset=dataset.rename(columns={'v1':'label','v2':'message'})


#Cleaning dataset and preprocessing

ps=PorterStemmer()

#Remove punctuations, stopwords and perform stemming
corpus=[]
for i in range(len(dataset)):
    review=re.sub('[^a-zA-Z]',' ',dataset['message'][i])
    review=review.lower()
    review=review.split()
    result=[]
    for word in review:
        if word not in stopwords.words('english'):
            result.append(ps.stem(word))
    result=" ".join(result)
    corpus.append(result)

#Vectoriztion
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
X=cv.fit_transform(corpus).toarray()

y=pd.get_dummies(dataset['label'])
y=y.iloc[:,-1].values    

#Splitting of dataset into train and test data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.20,random_state=0)

#Generating a machine learning model
from sklearn.naive_bayes import MultinomialNB
spam_detector=MultinomialNB().fit(X_train,y_train)

#Testing the model
y_pred=spam_detector.predict(X_test)

#Metrics to test the performance of the model
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test, y_pred) 
    
        
    
    


