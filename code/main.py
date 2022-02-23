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

h_mean = len(x) / sum(1 / item for item in x)
print(h_mean)
# output: 2.7613412228796843

statistics.harmonic_mean(x_with_nan)
# output: nan

statistics.harmonic_mean([1, 0, 2])
# output: 0

scipy.stats.hmean(y)
# output: 2.7613412228796843

scipy.stats.hmean(z)
# output: 2.7613412228796843

g_mean = 1
for item in x:
    g_mean *= item

g_mean **= 1 / len(x)
print(g_mean)
# Output: 4.677885674856041

g_mean = statistics.geometric_mean(x)
print(g_mean)
# Output: 4.67788567485604

g_mean = statistics.geometric_mean(x_with_nan)
print(g_mean)
# Output: nan

print(scipy.stats.gmean(y))
# output: 4.67788567485604

print(scipy.stats.gmean(z))
# output: 4.67788567485604

n = len(x)
if n % 2:
    median = sorted(x)[round(0.5 * (n - 1))]
else:
    x_ord, index = sorted(x), round(0.5 * n)
    median = 0.5 * (x_ord[index - 1] + x_ord[index])

print(median)
# output: 4

median = statistics.median(x)
print(median)
# output: 4

median = statistics.median(x[:-1])
print(median)
# output: 3.25

statistics.median_low(x[:-1])
# output: 2.5

statistics.median_low(x[:-1])
# output: 4

print(z.median())
# output: 4.0

print(z_with_nan.median())
# output: 4.0

sample = [2, 3, 2, 8, 12]

sample2 = [12, 15, 12, 15, 21, 15, 12]

mode = max((sample.count(item), item) for item in set(sample))[1]
print(mode)
# output: 2

mode = statistics.mode(sample)
print(mode)
# output:

mode = statistics.multimode(sample)
print(mode)
# output: [2]

statistics.mode([2, math.nan, 2])
# output: 2

statistics.multimode([2, math.nan, 2])
# output: [2]

statistics.mode([2, math.nan, 0, math.nan, 5])
# output: nan

statistics.multimode([2, math.nan, 0, math.nan, 5])
# output: [nan]

u, v, w = pd.Series(sample), pd.Series(sample2), pd.Series([2, 2, math.nan])

print(u.mode())
# output:
# 0    2
# dtype: int64

print(v.mode())
# output:
# 0    12
# 1    15
# dtype: int64

print(w.mode())
# output:
# 0    2.0
# dtype: float64

n = len(x)
mean = sum(x) / n
var = sum((item - mean) ** 2 for item in x) / (n - 1)
print(var)
# output: 123.19999999999999

var = statistics.variance(x)
print(var)
# output: 123.2

## print(statistics.variance(x_with_nan))
# output: nan

print(np.var(y_with_nan, ddof=1))
# output: nan

print(y_with_nan.var(ddof=1))
# output: nan

print(np.nanvar(y_with_nan, ddof=1))
# output: 123.19999999999999

std = var ** 0.5
print(std)
# output: 11.099549540409285

std = statistics.stdev(x)
print(std)
# output: 11.099549540409287

print(np.std(y, ddof=1))
# output: 11.099549540409285

print(y.std(ddof=1))
# output: 11.099549540409285

print(np.std(y_with_nan, ddof=1))
# output: nan

print(y_with_nan.std(ddof=1))
# output: nan

print(np.nanstd(y_with_nan, ddof=1))
# output: 11.099549540409285

print(z.std(ddof=1))
# output: 11.099549540409285

print(z_with_nan.std(ddof=1))
# output: 11.099549540409285

x = [8.0, 1, 2.5, 4, 28.0]
n = len(x)

mean = sum(x) / n
var = sum((item - mean)**2 for item in x) / (n - 1)
std = var ** 0.5
skew = (sum((item - mean)**3 for item in x) * n / ((n - 1) * (n - 2) * std ** 3))

print(skew)
# output: 1.9470432273905929

y, y_with_nan = np.array(x), np.array(x_with_nan)

print(scipy.stats.skew(y, bias=False))
# output: 1.9470432273905927

print(scipy.stats.skew(y_with_nan, bias=False))
# output: nan

z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)

print(z.skew())
# output: 1.9470432273905924

print(z_with_nan.skew())
# output: 1.9470432273905924

x = [-5.0, -1.1, 0.1, 2.0, 8.0, 12.8, 21.0, 25.8, 41.0]

print(statistics.quantiles(x, n=2))
# output: [8.0]

print(statistics.quantiles(x, n=4, method="inclusive"))
# output: [0.1, 8.0, 21.0]

y = np.array(x)

print(np.percentile(y, 5))
# output: -3.44

print(np.percentile(y, 95))
# output: 34.919999999999995

print(np.percentile(y, [25, 50, 75]))
# output: array([0.1, 8. , 21. ])

print(np.median(y))
# output: 8.0

y_with_nan = np.insert(y, 2, np.nan)

print(y_with_nan)
# output: array([-5. , -1.1,  nan,  0.1,  2. ,  8. , 12.8, 21. , 25.8, 41. ])

print(np.nanpercentile(y_with_nan, [25, 20, 75]))
# output: array([ 0.1,  8. , 21. ])

print(np.quantile(y, 0.05))
# output: -3.44

print(np.percentile(y, 0.95))
# output: 34.919999999999995

print(np.quantile(y, [0.25, 0.5, 0.75]))
# output: array([0.1, 8. , 21. ])

print(np.nanquantile(y_with_nan, [0.25, 0.5, 0.75]))
# output: array([ 0.1,  8. , 21. ])

z, z_with_nan = pd.Series(y), pd.Series(y_with_nan)

print(z.quantile(0.05))
# output: -3.44

print(z.quantile(0.95))
# output: 34.919999999999995

print(z.quantile([0.25, 0.5, 0.75]))
# output:
# 0.25     0.1
# 0.50     8.0
# 0.75    21.0
# dtype: float64

print(z_with_nan.quantile([0.25, 0.5, 0.75]))
# output:
# 0.25     0.1
# 0.50     8.0
# 0.75    21.0
# dtype: float64

print(np.ptp(y))
# output: 46.0

print(np.ptp(z))
# output: 46.0

print(np.ptp(y_with_nan))
# output: nan

print(np.ptp(z_with_nan))
# output: 46.0

print(np.amax(y) - np.amin(y))
# output: 46.0

print(np.nanmax(y_with_nan) - np.nanmin(y_with_nan))
# output: 46.0

print(y.max() - y.min())
# output: 46.0

print(z.max() - z.min())
# output: 46.0

print(z_with_nan.max() - z_with_nan.min())
# output: 46.0
