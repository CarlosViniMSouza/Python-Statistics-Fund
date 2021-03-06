import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt

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

result = scipy.stats.describe(y, ddof=1, bias=False)

print(result)
# output: DescribeResult(nobs=9, minmax=(-5.0, 41.0), mean=11.622222222222222, variance=228.75194444444446, skewness=0.9249043136685094, kurtosis=0.14770623629658886)

"""
print(result.nobs())
# output: 9
"""

print(result.minmax[0])
# output: -5.0

print(result.minmax[1])
# output: 41.0

print(result.mean)
# output: 11.622222222222222

print(result.variance)
# output: 228.75194444444446

print(result.skewness)
# output: 0.9249043136685094

print(result.kurtosis)
# output: 0.14770623629658886

result = z.describe()

print(result)
"""
output:

count     9.000000
mean     11.622222
std      15.124548
min      -5.000000
25%       0.100000
50%       8.000000
75%      21.000000
max      41.000000
dtype: float64
"""

x = list(range(-10, 11))
y = [0, 2, 2, 2, 2, 3, 3, 6, 7, 4, 7, 6, 6, 9, 4, 5, 5, 10, 11, 12, 14]
x1, y1 = np.array(x), np.array(y)
x2, y2 = pd.Series(x1), pd.Series(y1)

n = len(x)
x_mean, y_mean = sum(x) / n, sum(y) / n
cov_xy = (sum((x[k] - x_mean) * (y[k] - y_mean) for k in range(n)) / (n - 1))
print(cov_xy)

cov_matrix = np.cov(x1, y1)
print(cov_matrix)
# output: array([[38.5       , 19.95      ],
#               [19.95      , 13.91428571]])

print(x1.var(ddof=1))
# output: 38.5

print(y1.var(ddof=1))
# output: 13.914285714285711

cov_xy = x2.cov(y2)
print(cov_xy)
# output: 19.95

cov_xy = y2.cov(x2)
print(cov_xy)
# output: 19.95

x_var = sum((item - x_mean)**2 for item in x) / (n - 1)
y_var = sum((item - y_mean)**2 for item in y) / (n - 1)

x_std, y_std = x_var ** 0.5, y_var ** 0.5
cor_cof = cov_xy / (x_std * y_std)

print(cor_cof)
# output: 0.861950005631606

cor_cof, p_value = scipy.stats.pearsonr(x1, y1)

print(cor_cof, "\n", p_value)
# output:
# 0.861950005631606
# 5.122760847201171e-07

corr_matrix = np.corrcoef(x1, y1)

print(corr_matrix)
# output: array([[1.        , 0.86195001],
#               [0.86195001, 1.        ]])

scipy.stats.linregress(x1, y1)
# output: LinregressResult(slope=0.5181818181818181, intercept=5.714285714285714, rvalue=0.861950005631606, pvalue=5.122760847201164e-07, stderr=0.06992387660074979)

result = scipy.stats.linregress(x1, y1)
cor_cof = result.rvalue

print(cor_cof)
# output: 0.861950005631606

cor_cof = x2.corr(y2)
print(cor_cof)
# output: 0.8619500056316061

cor_cof = y2.corr(x2)
print(cor_cof)
# output: 0.861950005631606

vector = np.array([[1, 1, 1],
                   [2, 3, 1],
                   [4, 9, 2],
                   [8, 27, 4],
                   [16, 1, 1]])

print(vector)
"""
output:

array([[ 1,  1,  1],
       [ 2,  3,  1],
       [ 4,  9,  2],
       [ 8, 27,  4],
       [16,  1,  1]])
"""

print(np.mean(vector))
# output: 5.4

print(vector.mean())
# output: 5.4

print(np.median(vector))
# output: 2.0

print(vector.var(ddof=1))
# output: 53.40000000000001

print(np.mean(vector, axis=0))
# output: array([6.2, 8.2, 1.8])

print(vector.mean(axis=0))
# output: array([6.2, 8.2, 1.8])

print(np.mean(vector, axis=1))
# output: array([ 1.,  2.,  5., 13.,  6.])

print(vector.mean(axis=1))
# output: array([ 1.,  2.,  5., 13.,  6.])

print(np.median(vector, axis=0))
# output: array([4., 3., 1.])

print(np.median(vector, axis=1))
# output: array([1., 2., 4., 8., 1.])

print(vector.var(axis=0, ddof=1))
# output: array([ 37.2, 121.2,   1.7])

print(vector.var(axis=1, ddof=1))
# output: array([  0.,   1.,  13., 151.,  75.])

print(scipy.stats.gmean(vector))  # here, the default is axis=0
# output: array([4.        , 3.73719282, 1.51571657])

print(scipy.stats.gmean(vector, axis=1))
# output: array([1.        , 1.81712059, 4.16016765, 9.52440631, 2.5198421 ])

print(scipy.stats.describe(vector, axis=None, ddof=1, bias=False))
# output: DescribeResult(nobs=15, minmax=(1, 27), mean=5.4, variance=53.40000000000001, skewness=2.264965290423389, kurtosis=5.212690982795767)

print(scipy.stats.describe(vector, ddof=1, bias=False))  # axis=0 by default
# output: DescribeResult(nobs=5, minmax=(array([1, 1, 1]), array([16, 27,  4])), mean=array([6.2, 8.2, 1.8]), variance=array([ 37.2, 121.2,   1.7]), skewness=array([1.32531471, 1.79809454, 1.71439233]), kurtosis=array([1.30376344, 3.14969121, 2.66435986]))

print(scipy.stats.describe(vector, axis=1, ddof=1, bias=False))
# output: DescribeResult(nobs=3, minmax=(array([1, 1, 2, 4, 1]), array([ 1,  3,  9, 27, 16])), mean=array([ 1.,  2.,  5., 13.,  6.]), variance=array([  0.,   1.,  13., 151.,  75.]), skewness=array([0.        , 0.        , 1.15206964, 1.52787436, 1.73205081]), kurtosis=array([-3. , -1.5, -1.5, -1.5, -1.5]))

row_names = ['first', 'second', 'third', 'fourth', 'fifth']
col_names = ['A', 'B', 'C']

df = pd.DataFrame(vector, index=row_names, columns=col_names)
print(df)
"""
output:

         A   B  C
first    1   1  1
second   2   3  1
third    4   9  2
fourth   8  27  4
fifth   16   1  1
"""

print(df.mean())
"""
output:

A    6.2
B    8.2
C    1.8
dtype: float64
"""

print(df.var())
"""
output:

A     37.2
B    121.2
C      1.7
dtype: float64
"""

df.mean(axis=1)
"""
output: 

first      1.0
second     2.0
third      5.0
fourth    13.0
fifth      6.0
dtype: float64
"""

df.var(axis=1)
"""
output: 

first       0.0
second      1.0
third      13.0
fourth    151.0
fifth      75.0
dtype: float64
"""

print(df['A'])
"""
output: 

first      1
second     2
third      4
fourth     8
fifth     16
Name: A, dtype: int64
"""

print(df['A'].mean())
# output: 6.2

print(df['A'].var())
# output: 37.20000000000001

print(df.values)
"""
output: 

array([[ 1,  1,  1],
       [ 2,  3,  1],
       [ 4,  9,  2],
       [ 8, 27,  4],
       [16,  1,  1]])
"""

print(df.to_numpy())
"""
output: 

array([[ 1,  1,  1],
       [ 2,  3,  1],
       [ 4,  9,  2],
       [ 8, 27,  4],
       [16,  1,  1]])
"""

print(df.describe())
"""
output: 

              A          B        C
count   5.00000   5.000000  5.00000
mean    6.20000   8.200000  1.80000
std     6.09918  11.009087  1.30384
min     1.00000   1.000000  1.00000
25%     2.00000   1.000000  1.00000
50%     4.00000   3.000000  1.00000
75%     8.00000   9.000000  2.00000
max    16.00000  27.000000  4.00000
"""

print(df.describe().at['mean', 'A'])
# output: 6.2

print(df.describe().at['50%', 'B'])
# output: 3.0

plt.style.use('ggplot')

np.random.seed(seed=0)

x, y, z = np.random.randn(1000), np.random.randn(100), np.random.randn(10)

fig, ax = plt.subplots()

ax.boxplot((x, y, z), vert=False, showmeans=True, meanline=True,
           labels=('x', 'y', 'z'), patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'purple'},
           meanprops={'linewidth': 2, 'color': 'red'})

plt.show()

hist, bin_edges = np.histogram(x, bins=10)

print(hist)
# output: array([  9,  20,  70, 146, 217, 239, 160,  86,  38,  15])

print(bin_edges)
"""
output:

array([-3.04614305, -2.46559324, -1.88504342, -1.3044936 , -0.72394379,
       -0.14339397,  0.43715585,  1.01770566,  1.59825548,  2.1788053 ,
        2.75935511])
"""

fig, ax = plt.subplots()

ax.hist(x, bin_edges, cumulative=False)
ax.set_xlabel('x')
ax.set_ylabel('Frequency')

plt.show()

fig, ax = plt.subplots()

ax.hist(x, bin_edges, cumulative=True)
ax.set_xlabel('x')
ax.set_ylabel('Frequency')

plt.show()

x, y, z = 128, 256, 1024

fig, ax = plt.subplots()
ax.pie((x, y, z), labels=('x', 'y', 'z'), autopct='%1.1f%%')

plt.show()

x = np.arange(21)
y = np.random.randint(21, size=21)
err = np.random.randn(21)

fig, ax = plt.subplots()

ax.bar(x, y, yerr=err)
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()

x, y = np.arange(21), (5 + 2 * x + 2) * np.random.randn(21)
slope, intercept, r, *__ = scipy.stats.linregress(x, y)
line = f'Regression Line: y={intercept: .2f} + {slope: .2f}x, r={r: .2f}'

fig, ax = plt.subplots()

ax.plot(x, y, linewidth=0, marker='s', label='Data points')
ax.plot(x, intercept + slope * x, label=line)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(facecolor='white')

plt.show()

matrix = np.cov(x, y).round(decimals=2)

fig, ax = plt.subplots()

ax.imshow(matrix)
ax.grid(False)

ax.xaxis.set(ticks=(0, 1), ticklabels=('x', 'y'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('x', 'y'))

ax.set_ylim(1.5, -0.5)

for i in range(2):
    for j in range(2):
        ax.text(j, i, matrix[i, j], ha='center', va='center', color='w')

plt.show()

matrix = np.corrcoef(x, y).round(decimals=2)

fig, ax = plt.subplots()

ax.imshow(matrix)
ax.grid(True)  # The default is False

ax.xaxis.set(ticks=(0, 1), ticklabels=('x', 'y'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('x', 'y'))

ax.set_ylim(1.5, -0.5)

for i in range(2):
    for j in range(2):
        ax.text(j, i, matrix[i, j], ha='center', va='center', color='w')

plt.show()

# TODO: Heatmaps is the next sub-topic.
