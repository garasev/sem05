
import pandas as pd
import numpy as np
import random as rnd
import math as m

 # visualization
import seaborn as sns
import matplotlib.pyplot as plt

train_df = pd.read_csv('train_longevity.csv')
test_df = pd.read_csv('test_longevity.csv')
combine = [train_df, test_df]


def setInterval(age):
    if age <= 70:
        return 1
    if age > 80:
        return 7
    return (age - 71) // 2 + 2

train_df['Age'].fillna(round(train_df['Age'].mean()), inplace=True)
train_df['AgeInterval'] = train_df['Age'].map(lambda v: setInterval(int(v))).astype(int)
