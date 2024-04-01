import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

data = pd.read_csv("housing.csv")
data.dropna(inplace=True)
# data.info()
from sklearn.model_selection import train_test_split

x = data.drop(['median_house_value'],axis= 1)
y = data['median_house_value']

x_train, x_test, y_train, y_test =train_test_split(x,y,test_size=0.2)

train_data = x_train.join(y_train)

print(train_data)

print(train_data.hist(figsize = (15,8)))