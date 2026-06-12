# 🚀 Customer Churn Prediction Dashboard

Customer retention is one of the most important challenges faced by businesses today. Acquiring a new customer is often more expensive than retaining an existing one, which makes customer churn prediction a valuable business problem.

This project is a Machine Learning-powered web application that predicts whether a customer is likely to leave a service based on key customer attributes such as age, tenure, monthly charges, satisfaction score, and referral activity. The application provides instant predictions along with a confidence score, helping businesses identify customers who may require additional attention and retention strategies.

The entire solution has been built using Python, Scikit-Learn, and Streamlit. A Logistic Regression model was trained on customer data, evaluated using industry-standard metrics, and deployed as an interactive web application that anyone can access through a browser.

## Why This Project?

The objective of this project was not only to build a Machine Learning model but also to understand the complete workflow of a real-world Data Science project, including:

* Data preprocessing and feature selection
* Model training and evaluation
* Model serialization using Joblib
* Building an interactive web application
* Deploying the application to the cloud
* Managing the project using Git and GitHub

Through this project, I gained hands-on experience in transforming a Machine Learning model into a usable product that can deliver predictions in real time.

## Features

The application allows users to enter customer details through an intuitive interface and instantly receive a churn prediction. Along with the prediction, the model also provides a confidence score that indicates how certain the model is about its decision.

Key features include:

* Real-time churn prediction
* Interactive Streamlit dashboard
* Confidence score generation
* Machine Learning-based classification
* Cloud deployment using Streamlit
* User-friendly interface

## Technology Stack

This project was developed using the following technologies:

* Python
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Streamlit
* Git & GitHub
* Streamlit Cloud

## Application Workflow

The prediction process follows a simple workflow:

Customer Data → Feature Scaling → Logistic Regression Model → Prediction → Confidence Score

The trained model analyzes the provided customer information and determines whether the customer is likely to continue using the service or churn.

## Running the Project Locally

Clone the repository:

```bash
git clone https://github.com/kasamvivek/customer-churn-prediction.git
```

Move into the project directory:

```bash
cd customer-churn-prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Future Improvements

This project can be extended further by incorporating additional customer features, experimenting with advanced machine learning models, adding interactive visualizations, and building a complete customer analytics dashboard.

## Author

Kasam Vivek

Artificial Intelligence Student with a strong interest in Data Science, Machine Learning, and AI-powered applications.

GitHub: https://github.com/kasamvivek
