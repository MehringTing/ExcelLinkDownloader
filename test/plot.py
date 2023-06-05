import numpy as np
import matplotlib.pyplot as plt

# Juwairia's data:
a = [4, -6, 9]
b = [2, 7, 1]
c = [3, 3, 1]
d = [4, 0, -3]
data = np.array([a, b, c, d])

data_shape = np.shape(data)


# Take negative and positive data apart and cumulate
def get_cumulated_array(data, **kwargs):
    cum = data.clip(**kwargs)
    cum = np.cumsum(cum, axis=0)
    d = np.zeros(np.shape(data))
    d[1:] = cum[:-1]
    return d


cumulated_data = get_cumulated_array(data, min=0)
cumulated_data_neg = get_cumulated_array(data, max=0)

# Re-merge negative and positive data.
row_mask = (data < 0)
cumulated_data[row_mask] = cumulated_data_neg[row_mask]
data_stack = cumulated_data

cols = ["g", "y", "b", "c"]

fig = plt.figure()
ax = plt.subplot(111)

for i in np.arange(0, data_shape[0]):
    ax.bar(np.arange(data_shape[1]), data[i], bottom=data_stack[i], color=cols[i], )

plt.show()