# Burn Rate Predictor API

This is a machine learning model that predicts a person's burn out using some personal and professional data about the person.

## The Dataset
The data was collected from Kaggle. It can be found [here](https://www.kaggle.com/redwankarimsony/hackerearth-employee-burnout-challenge).

## Running in localhost

To run this model some python packages are required which can be installed using the given requirements.txt file by entering the following command in the terminal:

```
pip install -r requirements.txt
```

To run the flask file as local host use the command
```
python app.py
```
## The Model

We initially performed a comparitive study on various Machine Learning models and how well they perform on our Dataset.
After analysing the results we come to know that the top performing models are Linear Regression and XGBoost with R<sup>2</sup> Scores of 92.05% and 92.9% respectively.
Due to high training times taken by XGBoost and there not being a massive difference in the R<sup>2</sup> scores,
we choose to implement the Linear Regression model into our Web App.

![linar reg flow](https://user-images.githubusercontent.com/47575172/115266986-50376880-a156-11eb-9474-f849e89dd1e4.png)

