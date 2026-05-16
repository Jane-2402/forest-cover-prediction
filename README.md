# Forest Cover Prediction System 🌲

## Project Overview

The Forest Cover Prediction System is a Machine Learning project that predicts the type of forest cover based on geographical and environmental features. The project uses classification algorithms to identify forest cover categories accurately and provides predictions through a Streamlit web application.

---

# Business Problem

Forest departments and environmental organizations need to identify forest cover types efficiently for:

- Forest management
- Wildlife conservation
- Land monitoring
- Environmental planning
- Disaster prevention
- Ecological research

Manual identification of forest cover is time-consuming and expensive. This project automates the prediction process using Machine Learning techniques.

---

# Solution

This project uses Machine Learning classification models to predict forest cover types from environmental features such as elevation, road distance, fire point distance, soil type, and wilderness area.

A Random Forest Classifier was used as the final model because it provided the best accuracy.

The project also includes a Streamlit web application where users can enter feature values and get real-time predictions with forest images.

---

# Dataset Used

Forest Cover Type Dataset

The dataset contains:
- Geographical features
- Soil type information
- Wilderness area information
- Cover type labels

Target Variable:
- Cover_Type

---

# Libraries Used

## Data Handling
- pandas
- numpy

## Visualization
- matplotlib
- seaborn

## Machine Learning
- scikit-learn

## Model Saving
- pickle

## Web Application
- streamlit

## Image Processing
- PIL

---

# Machine Learning Models Used

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

Final Selected Model:
- Random Forest Classifier

---

# Features Used

Selected Important Features:

1. Elevation
2. Horizontal_Distance_To_Roadways
3. Horizontal_Distance_To_Fire_Points
4. Wilderness_Area1
5. Wilderness_Area3
6. Wilderness_Area4
7. Soil_Type3
8. Soil_Type10
9. Soil_Type38
10. Soil_Type39

---

# Project Workflow

## Step 1: Import Libraries
Imported all required Python libraries.

---

## Step 2: Load Dataset
Loaded Forest Cover dataset using pandas and sklearn.

---

## Step 3: Data Exploration
Performed:
- Dataset inspection
- Null value checking
- Correlation analysis
- Statistical summary

---

## Step 4: Data Visualization
Created graphs:
- Correlation heatmap
- Confusion matrix
- Feature importance graph
- Cover type distribution graph

---

## Step 5: Feature Selection
Used:
- SelectKBest
- f_classif

Selected top important features for better model performance.

---

## Step 6: Train-Test Split
Split dataset into:
- Training data
- Testing data

Using:
- train_test_split()

---

## Step 7: Model Training
Trained:
- Logistic Regression
- Decision Tree
- Random Forest

---

## Step 8: Model Evaluation
Evaluated models using:
- Accuracy Score
- Confusion Matrix
- Classification Report

---

## Step 9: Feature Importance
Used Random Forest feature importance to identify the most influential features.

---

## Step 10: Model Saving
Saved trained Random Forest model using pickle.


## Streamlit Web App

Built a Streamlit application for user interaction.

Features:

User input
Real-time prediction
Forest image display
Prediction mapping


## Project Results
Random Forest achieved the best performance.
Important features significantly improved prediction accuracy.
The web app provides easy and interactive predictions.



## Future Improvements
Deploy application online
Add dropdown-based inputs
Improve UI design
Add more visualizations
Use advanced boosting algorithms



## Conclusion

The Forest Cover Prediction System successfully predicts forest cover types using Machine Learning techniques. The project demonstrates the complete Machine Learning workflow from data preprocessing to deployment using Streamlit.
