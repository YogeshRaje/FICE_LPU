import pandas as pd
from numba import njit, prange

# Dataset for analysis
FNAME = "employees.csv"


# This function gets compiled by Numba* and multi-threaded
@njit(parallel=True)
def get_analyzed_data():
    df = pd.read_csv(FNAME)
    s_bonus = pd.Series(df['Bonus %'])
    s_first_name = pd.Series(df['First Name'])

    # Use explicit loop to compute the mean. It will be compiled as parallel loop
    m = 0.0
    for i in prange(s_bonus.size):
        m += s_bonus.values[i]
    m /= s_bonus.size

    names = s_first_name.sort_values()
    return m, names


# Printing names and their average bonus percent
mean_bonus, sorted_first_names = get_analyzed_data()
print(sorted_first_names)
print('Average Bonus %:', mean_bonus)
