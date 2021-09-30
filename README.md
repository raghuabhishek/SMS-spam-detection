# SMS-spam-detection
This repository contains the code which detects whether a SMS message is a spam or a legitimate one



## Context

![Spam-image](https://blog.textedly.com/hubfs/winner-jpg.jpeg)

The SMS Spam Collection is a set of SMS tagged messages that have been collected for SMS Spam research. It contains one set of SMS messages in English of 5,574 messages, tagged acording being ham (legitimate) or spam.

## Dataset
The **spam.csv** contain one message per line. Each line is composed by two columns: **v1** contains the label (ham or spam) and **v2** contains the raw text.
This corpus has been collected from free or free for research sources at the Internet:

1. A collection of **425 SMS spam** messages was manually extracted from the **Grumbletext** Web site. This is a UK forum in which cell phone users make public claims about SMS spam messages, most of them without reporting the very spam message received.
2. A subset of **3,375** SMS randomly chosen ham messages of the NUS SMS Corpus (NSC), which is a dataset of about 10,000 legitimate messages collected for research at the Department of Computer Science at the National University of Singapore.
3. A list of **450 SMS ham messages** collected from Caroline Tag's PhD Thesis.
4. Finally, we have incorporated the SMS Spam Corpus v.0.1 Big. It has **1,002 SMS ham messages** and **322 spam messages**.

## Preprocessing data

![Pandas-img](data:image/png;base64,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)
1. **Importing dataset**: I have used `pd.read_csv()` method to import the dataset. While reading the data, I have used **latin-1** which uses the characters 0 through 127, so it can encode half as many characters as **latin-1**. I have renamed the columns of the dataframe from **v1** and **v2** to **label** and **message** respectivelly.
2. **Removing punctuations**: I have used regular expressions library **(re)** to remove the **punctuations** using the function 
`re.sub('[^a-zA-Z]',' ',dataset['message'][i])` which substitutes all the characters other than alphabets to whitespaces. 
3. **Removing stopwords**: The stopwords like "is","the","or" etc which doesnt have any significance should be removed from the message and we used stopwords module from nltk to acheive this. `stopwords.words('english')`
4. **Stemming**: Stemming is a process of reducing the word to its root stem or removing the affixes. I have used **PorterStemmer** in my code to acheive stemming. `PorterStemmer.stem(word)`
5. **Vectoriztion**: Vectorization is a process of generating numerical vectors/arary from textual data. I have implemented **Bag of Words(BoW)** technique which counts the number of occurances of the word in a message. To implement this, I have leveraged **CountVectorizer** class to acheive this.
`X=CountVectorizer.fit_transform(corpus).toarray()`
6. **Splitting dataset**: The dataset is then divided into training and testing data in the ratio 80:20. 
`X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.20,random_state=0)`

## Spam detection model
1. **Generate model**: The **Naive bayes classifier** uses **Bayes Theorem** which is based on conditionl probability is used to generate a model for the spam dataset. I have used **sklearn** library for implementing Naive Bayes classifier. `spam_detector=MultinomialNB().fit(X_train,y_train)`
2. **Testing the model**: I have used predict() function to test the model `y_pred=spam_detector.predict(X_test)`. 
3. **Measuring the performance**: I have used confusion matrix and accuracy to determine the performance of the ML model. `cm=confusion_matrix(y_test,y_pred)` `accuracy=accuracy_score(y_test, y_pred)`.


