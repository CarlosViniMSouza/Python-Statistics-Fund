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

print(0.2 * 2 + 0.5 * 4 + 0.3 * 8)
# output: 4.8

x = [8.0, 1, 2.5, 4, 28.0]
w = [0.1, 0.2, 0.3, 0.25, 0.15]

w_mean = sum(w[i] * x[i] for i in range(len(x))) / sum(w)
print(w_mean)

# Other way:
w_mean = sum(x_ * w_ for (x_, w_) in zip(x, w)) / sum(w)
print(w_mean)

w, y, z = np.array(w), np.array(x), pd.Series(x)
w_mean = np.average(y, weights=w)
print(w_mean)
# output: 6.95

w_mean = np.average(z, weights=w)
print(w_mean)
# output: 6.95

w = np.array([0.1, 0.2, 0.3, 0.0, 0.2, 0.1])
print((w * y_with_nan).sum() / w.sum())
# output: nan

print(np.average(y_with_nan, weights=w))
# output: nan

print(np.average(z_with_nan, weights=w))
# output: nan
