#Problem 28 (08.08.2023)
## Problem Statement - Write a Python program to Create a class named DataPoint to represent a data point in a dataset. Each data point should have attributes like features (a list of numerical values) and label (a string representing the class label). 
#Implement a method that prints out the data point's features and label.
class DataPoint(object):
  def __init__(self, features, label):
    self.features = features
    self.label    = label

  def display(self):
    print(f"Features : {self.features}")
    print(f"Label: {self.label}")

data = DataPoint([1.2,2.6,3.8,4.9,6.7], 'Sample data')
data.display()


#Problem 29 (08.08.2023)
## Problem Statement - Write a Python program to Create a class named DataPreprocessor that takes a dataset (a list of DataPoint instances) as input. 
#Implement methods to calculate the mean and standard deviation of each feature across all data points.

import numpy as np

class DataPreprocessor(object):
  
  def __init__(self, dataset):
    self.dataset = dataset

  def calc_mean(self):
    num_features = len(self.dataset[0].features)
    feature_values = np.array([data.features for data in self.dataset])
    mean = np.mean(feature_values, axis = 0)
    return mean

  def calc_std_dev(object):
    num_features = len(self.dataset[0].features)
    feature_values = np.arrray([data.features for data in self.dataset])
    std_dev = np.std(feature_values, axis = 0)
    return std_dev

class DataPoint(object):
  def __init__(self, features, label):
    self.features = features
    self.label = label

data1 = DataPoint([1.2,2.6,3.9],'A')
data2 = DataPoint([2.4,4.6,6.9[,'B')
data3 = DataPoint([3.1,5.5,7.8],'C')

dataset = np.array([data1,data2,data3])

preprocessor = DataPreprocessor(dataset)
mean = preprocessor.calc_mean()
std  = preprocessor.calc_std_dev(mean)

print("Mean: ", mean)
print("Standard Deviation: ", std)
