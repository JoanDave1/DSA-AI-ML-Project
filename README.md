# DSA-AI-ML-Project

## PROJECT OVERVIEW

This project involved the development of an end-to-end credit card fraud detection system that analyzes transaction patterns and predicts whether a transaction is fraudulent or legitimate. The system combines exploratory data analysis, machine learning modeling, and web deployment, resulting in a fully functional and publicly accessible application.

### Data Collection & Understanding: 

A real-world credit card transactions dataset was used, containing numerical features representing transaction behavior and a target variable indicating fraud (1) or non-fraud (0). Special attention was paid to the class imbalance, since fraudulent transactions occur far less frequently than legitimate ones.

### Data Preprocessing:

The dataset was cleaned and prepared for modeling by:

* Removing null and duplicate values
* Separating features and target labels
* Handling class imbalance
* Splitting the data into training and testing sets

This ensured the model learned meaningful patterns without bias.

### Exploratory Data Analysis & Key Findings:

#### 1. Class Distribution (Fraud vs. No Fraud)

The dataset is highly imbalanced with fraudulent transactions greatly outnumbering non-fraudulent transactions. This reflects that payment systems that lead to fraudulent transactions are in most cases, rare. Special care was taken to ensure that models and metrics (precision, recall, roc-auc) suitable for imbalanced data were used. 

#### 2. Transaction Distance From Home

This feature is a strong indicator of fraudulent or abnormal behaviour as fraudulent transactions tend to occur farther from the card owner's home location. Transactions made from customers' home location may, in most cases, indicate stolen card usage. 

#### 3. Distance From Last Transaction

In most cases, sudden changes in location are a key signal for fraud. Fraudulent transactions often show large differences in distance when compared to previous transaction. 

#### 4. Ratio To Median Purchase Price



#### Live Demo:
https://credit-card-fraud-app-1.onrender.com

#### Source Code:
https://github.com/JoanDave1/credit-card-fraud-app
