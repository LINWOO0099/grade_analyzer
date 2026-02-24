import numpy as np

# Given data
data = np.array([[22.5, 19.0, 31.2, 28.7, 25.1],
                 [17.3, 22.8, 30.5, 26.4, 21.9],
                 [33.1, 29.6, 18.4, 24.0, 27.8],
                 [20.2, 23.5, 31.9, 28.1, 22.6]])

#task  1
print("Original Data:", data.shape)
print("Mean of the data", data .mean())

# task 2
high = data[data > 28]
print("high temperature", high.max())
print("low temperature", high.min())
 
# task 3
normalized = (data - data.min()) / (data.max() - data.min())

print("Normalized Data (rounded to 2 decimals):")
print(np.round(normalized,3))  

