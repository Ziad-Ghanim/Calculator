import numpy as np
import pandas as pd 

#Create Class Calculator
class DataCalculator:
    # property 
    def __init__(self, data=None):
        if data is not None:
            self.data = np.array(data)
        else:
            self.data = np.array([])
    # creat method for ++
    def add(self, a, b):
        return a + b
    # creat method for --
    def subtract(self, a, b):
        return a - b
    # creat method for *
    def multiply(self, a, b):
        return a+ b 
    # creat method for /  and handling Zero Division Eror
    def divide(self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            print("you can not Division by zero")

    # method for load data from csv file and convert to array
    def load_data_from_csv(self, file_path):
        df = pd.read_csv(file_path)
        self.data = df['values'].to_numpy()
        return self.data
    #method for calculate mean
    def mean(self):
        return np.mean(self.data)
    #method for calculate total
    def total(self):
        return np.sum(self.data)
    #method for return max value in array
    def max_value(self):
        return np.max(self.data)
    #method for return min value from array
    def min_value(self):
        return np.min(self.data)
    

#Run App
if __name__ == '__main__' :
    calc = DataCalculator()
    print(calc.divide(12,1))
    data = calc.load_data_from_csv("C:/Users/Dream/test_project/data.csv")
    print(data.mean())

