import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd

x_list = [8.0, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]

x_list
# Output: [8.0, 1, 2.5, 4, 28.0]

x_with_nan
# Output: [8.0, 1, 2.5, nan, 4, 28.0]

math.isnan(np.nan), np.isnan(math.nan)
# output: (True, True)

math.isnan(x_with_nan[3]), np.isnan(x_with_nan[3])
# output: (True, True)
