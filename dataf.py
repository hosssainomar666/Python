# Import the necessary libraries
import numpy as np
import pandas as pd

# Create a NumPy array
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Create a Pandas series
series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Convert the NumPy array to a data frame
df_array = pd.DataFrame(data)

# Convert the Pandas series to a data frame
df_series = pd.DataFrame(series)

# Print the data frames
print(df_array)
print(df_series)