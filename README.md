# SMS-spam-detection
This repository contains the code which detects whether a SMS message is a spam or a legitimate one

## Context
The SMS Spam Collection is a set of SMS tagged messages that have been collected for SMS Spam research. It contains one set of SMS messages in English of 5,574 messages, tagged acording being ham (legitimate) or spam.

## Dataset
The **spam.csv** contain one message per line. Each line is composed by two columns: **v1** contains the label (ham or spam) and **v2** contains the raw text.
This corpus has been collected from free or free for research sources at the Internet:

1. A collection of **425 SMS spam** messages was manually extracted from the **Grumbletext** Web site. This is a UK forum in which cell phone users make public claims about SMS spam messages, most of them without reporting the very spam message received.
2. A subset of **3,375** SMS randomly chosen ham messages of the NUS SMS Corpus (NSC), which is a dataset of about 10,000 legitimate messages collected for research at the Department of Computer Science at the National University of Singapore.
3. A list of **450 SMS ham messages** collected from Caroline Tag's PhD Thesis.
4. Finally, we have incorporated the SMS Spam Corpus v.0.1 Big. It has **1,002 SMS ham messages** and **322 spam messages**.

## Spam detector model
1. **Importing dataset**: I have used pandas library to import the dataset and renamed the columns v1 and v2 with label and message respectivelly.
2. **Cleaning data and preprocessing**: Removing punctuations, stopwords and perform stemming.
3. **Vectoriztion**: Bag of Words(BoW) is a technique implemented for generating vectors from textual data.
4. **Splitting dataset**: The dataset is then divided into training and testing data in the ratio 80:20.
5. **Generate model**: The naive bayes classifier works best with the spam classification since it works on conditional probability.
6. **Testing the model and measuring the performance**: The model which I have generated gave me an accuracy of 98%.



