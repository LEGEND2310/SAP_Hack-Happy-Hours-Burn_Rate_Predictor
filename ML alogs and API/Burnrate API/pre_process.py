import numpy as np
import pandas as pd


def pre_process_df(data):
    gender = {'Female': 1, 'Male': 0}
    company_type = {'Service': 1, 'Product': 0}
    wfh_setup_avail = {'No': 0, 'Yes': 1}

    data['Gender'] = [gender[i] for i in data['Gender']]
    data['Company Type'] = [company_type[i] for i in data['Company Type']]
    data['WFH Setup Available'] = [wfh_setup_avail[i]
                                   for i in data['WFH Setup Available']]

    data['Designation'] = data['Designation'].astype('int64')
    data['Resource Allocation'] = data['Resource Allocation'].astype('float64')

    data.dropna(inplace=True)

    return data


def make_df(arr, col_names):
    arr = np.array(arr).reshape(1, 6)
    return pd.DataFrame(arr, columns=col_names)
