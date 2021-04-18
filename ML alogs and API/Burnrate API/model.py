import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
import pre_process

train = pd.read_csv('train.csv', index_col='Employee ID')

train = pre_process.pre_process_df(train)

X = train.drop(['Burn Rate', 'Date of Joining'], axis=1)
y = train['Burn Rate']

lrm = LinearRegression()

lrm.fit(X, y)


def burn_out_pred(gender, service, wfh_avail, designation, resource_allocation, mental_fatigue_score):
    col = ["Gender", "Company Type", "WFH Setup Available",
           "Designation", "Resource Allocation", "Mental Fatigue Score"]

    # 'Female','Service','No','2','3','3.8'

    sample_df = pre_process.make_df(
        [gender, service, wfh_avail, designation, resource_allocation, mental_fatigue_score], col)
    sample_df = pre_process.pre_process_df(sample_df)

    y_pred = lrm.predict(sample_df)

    return str(round(y_pred[0], 2))
