import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd

x_list = [8.0, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]

print(x_list)
# Output: [8.0, 1, 2.5, 4, 28.0]

print(x_with_nan)
# Output: [8.0, 1, 2.5, nan, 4, 28.0]

print(math.isnan(np.nan), np.isnan(math.nan))
# output: True True

print(math.isnan(x_with_nan[3]), np.isnan(x_with_nan[3]))
# output: True True

y, y_with_nan = np.array(x_list), np.array(x_with_nan)
z, z_with_nan = pd.Series(x_list), pd.Series(x_with_nan)

mean = sum(x_list) / len(x_list)
print(mean)
# output: 8.7

mean = statistics.mean(x_list)
print(mean)
# output: 8.7

mean = statistics.fmean(x_list)
print(mean)
# output: 8.7

mean = statistics.mean(x_with_nan)
print(mean)
# output: nan

mean = statistics.fmean(x_with_nan)
print(mean)
# output: nan

mean = np.mean(y)
print(mean)
# output: 8.7

mean = y.mean()
print(mean)
# output: 8.7

print(np.mean(y_with_nan))
# output: nan

print(y_with_nan.mean())
# output: nan

print(np.nanmean(y_with_nan))
# uotput: 8.7
