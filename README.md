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

## Preprocessing data
1. **Importing dataset**: I have used `pd.read_csv()` method to import the dataset. While reading the data, I have used **latin-1** which uses the characters 0 through 127, so it can encode half as many characters as **latin-1**. I have renamed the columns of the dataframe from **v1** and **v2** to **label** and **message** respectivelly.
![latin-1 image](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Latin-1-infobox.svg/1200px-Latin-1-infobox.svg.png)

2. **Removing punctuations**: I have used regular expressions library **(re)** to remove the **punctuations** using the function re.sub() which substitutes all the characters other than alphabets to whitespaces.

4. **Removing stopwords**: The w
5. **Vectoriztion**: Bag of Words(BoW) is a technique implemented for generating vectors from textual data.
6. **Splitting dataset**: The dataset is then divided into training and testing data in the ratio 80:20.

## Spam detection model
1. **Generate model**: The naive bayes classifier works best with the spam classification since it works on conditional probability.
2. **Testing the model and measuring the performance**: The model which I have generated gave me an accuracy of 98%.



