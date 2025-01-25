# Fraud Detection in E-Commerce

## Overview
This project focuses on developing a predictive model to detect fraudulent transactions in e-commerce platforms The primary goal was to optimize the recall for fraud detection while minimizing false negatives to reduce potential financial losses. Using Python and machine learning techniques, the model identifies suspicious patterns, enabling businesses to mitigate financial losses and enhance security.

## Key Highlights
- Dataset size: 290,000+ transactions
- Features: 15 optimized features
- Model: XGBoost
- Performance:
     - AUC: 0.884
     - Accuracy: 94%
     - Recall (Fraud): 49%
     - Precision (Fraud): 43%

## Project Steps
1. Data Exploration: Cleaned and analyzed raw data, addressing issues like negative values and outliers.
1. Feature Engineering: Created domain-specific features like is_low_amount, log-transformed amounts, and transaction flags.
1. Model Training: Used XGBoost with hyperparameter tuning (RandomSearchCV) and cost-sensitive learning to optimize recall for fraud detection.
1. Threshold Optimization: Fine-tuned decision thresholds to balance business trade-offs between recall and precision.
1. Evaluation: Achieved a significant improvement in fraud recall (+20%) with reduced false negatives.

## Repository Structure
Refer to the repository layout above.

## Getting Started
1. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/your_username/fraud-detection-project.git
   cd fraud-detection-project
   pip install -r requirements.txt
   ```

## How to Run
Run the notebooks in the notebooks folder sequentially or use the scripts in the src folder for a streamlined process.

## Workflow:
- Use the scripts in the src/ folder for reusable logic.
- Use the Jupyter notebooks in notebooks/ to prototype, analyze, and finalize steps.

# Data Access and Download Instructions
This project relies on external data to train and evaluate the fraud detection model. Follow the steps below to download and prepare the data for use.

1. Data Source
The dataset used in this project can be accessed from the following location:

Source: [Dataset Link](https://www.kaggle.com/datasets/shriyashjagtap/fraudulent-e-commerce-transactions)

2. Download Instructions
Visit the dataset source page.
Download the file(s) to your local machine:
File Name: Fraudulent_E-Commerce_Transaction_Data.csv (or other files provided by the dataset).
Ensure that the downloaded dataset is in the following structure:
```kotlin
data/
├── raw/
│   ├── transaction_data.csv
└── processed/
```
3. Organizing Data
Create a folder named data/ in the root directory of the project (if it doesn’t already exist).
Inside data/, create two subfolders:
raw/: Store the original dataset here.
processed/: Processed/cleaned datasets will be saved here during runtime.

5. Example Setup
Here’s how your project directory should look after downloading the dataset:
```css
fraud-detection-project/
├── data/
│   ├── raw/
│   │   ├── transaction_data.csv
│   ├── processed/
├── src/
├── notebooks/
├── README.md
├── requirements.txt
```
