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

The dataset is highly imbalanced with fraudulent transactions greatly outnumbering non-fraudulent transactions. This reflects that payment systems that lead to fraudulent transactions are in most cases, rare. Special care was taken to ensure that models and metrics (precision, recall, roc-auc) suitable for imbalanced data were used. e

<img width="450" height="234" alt="image" src="https://github.com/user-attachments/assets/79a158f7-4e1d-47a3-bb63-bc9bd41ab929" />

#### 2. Transaction Distance From Home

This feature is a strong indicator of fraudulent or abnormal behaviour as fraudulent transactions tend to occur farther from the card owner's home location. Transactions made from customers' home location may, in most cases, indicate stolen card usage. 

<img width="1232" height="764" alt="image" src="https://github.com/user-attachments/assets/b53214d5-ca5e-4c22-baef-5f30b39b8d96" />

#### 3. Distance From Last Transaction

In most cases, sudden changes in location are a key signal for fraud. Fraudulent transactions often show large differences in distance when compared to previous transaction. 

#### 4. Ratio To Median Purchase Price

Fraudulent transactions usually have a significantly higher ratio to median purchase price as fraudulent transactions involve amounts larger than a customer's typical spending on an average. This often means that fraudsters attempt high value purchases before the cards are blocked. 

<img width="1268" height="777" alt="image" src="https://github.com/user-attachments/assets/74ccc879-82bf-4899-aff4-0287e652f5c0" />

#### 5. Online Transactions

Fraud is more prevalent in online transactions where pin or chip is not inputted physically. Online transactions that lack physical verification are usually more vulnerable to fraud. Therefore, mode of transaction strongly influences the risk of fraud.

<img width="1306" height="758" alt="image" src="https://github.com/user-attachments/assets/22ea310c-0939-4367-a130-d7a0f765200e" />

(NOTE: The distance-based features represent values that show how unusual the transaction location is compared to what is normal for that customer, rather than real-world physical distances. Higher values indicate abnormal transaction locations relative to a customer’s typical behavior.)

#### 6. Correlation Analysis:

Moderate correlations exist between fraud and distance from home, distance from last transaction, ratio to median purchase price and online transactions. It should be noted however, that no single feature determines fraud and fraud detection depends on combined behavioural patterns. 

### Recommendations

#### Live Demo:
https://credit-card-fraud-app-1.onrender.com

#### Source Code:
https://github.com/JoanDave1/credit-card-fraud-app
