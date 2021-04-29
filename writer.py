import pandas as pd 
import numpy as np 

def dump_data(data):
    dataframe = pd.DataFrame(data) 
    print(dataframe)
    dataframe.to_csv("data.csv")
