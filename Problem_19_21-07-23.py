#Problem 19 (21-07-2023)
#Problem Statement: Write a python program to Plot the sine function over the interval [−π,π] using matplotlib.

import matplotlib.pyplot as plt
import numpy as np

def sine(x):

 # Args:    x- The x-coordinates of the points to plot.

  y = np.sin(x)
  plt.plot(x, y)
  plt.xlabel("x")
  plt.ylabel("sin(x)")
  plt.show()

if __name__ == "__main__":
  x = np.linspace(-np.pi, np.pi, 100)
  sine(x)
