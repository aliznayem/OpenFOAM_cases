import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

fn_lst = [0.25, 0.267, 0.289, 0.316, 0.354, 0.408]
ct_lst = [4.18, 4.15, 4.72, 4.93, 4.78, 5.63]
ct_efd_lst = [4.16, 4.1, 4.4, 4.75, 4.56, 5.5]

fn_lst_new = np.linspace(fn_lst[0], fn_lst[5], 50)
f_cubic = interp1d(fn_lst, ct_lst, kind='quadratic')

plt.plot(fn_lst_new, f_cubic(fn_lst_new), 'k-', lw='0.5', label="Present Simulation")
plt.plot(fn_lst, ct_efd_lst, 'k*', label="Experimental")

plt.legend(loc="upper left")
plt.xlabel(r"Froude number, $F_n$")
plt.ylabel(r"Total resistance coefficient, $C_T × 10^3$")
plt.xticks(fn_lst)
plt.ylim(ymin=1, ymax=8)

plt.show()
