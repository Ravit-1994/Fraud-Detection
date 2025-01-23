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
