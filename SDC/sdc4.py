import time
import numpy as np
import pandas as pd
from numba import njit

@njit
def perf_series_max(s):                  # <-- unboxing
   start_time = time.time()              # <-- time inside Numba JIT code
   res = s.max()
   finish_time = time.time()             # <-- time inside Numba JIT code
   return finish_time - start_time, res  # <-- boxing

s = pd.Series(np.random.ranf(size=100000))
exec_time, res = perf_series_max(s)
print("Execution time in JIT code: ", exec_time)