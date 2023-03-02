from numba import njit

@njit
def series_max(s):
   return s.max()