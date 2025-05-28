import numpy as np

# Create a 4x5 array with random integer values between 0 and 100
arr = np.random.randint(0, 100, size=(4, 5))
print(arr)

np.save('data.npy', arr)
print("Data saved to data.npy")

# Load the saved array from the file
loaded_arr = np.load('data.npy')  
print("Data loaded from data.npy")
print(loaded_arr)