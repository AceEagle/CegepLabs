from _ast import Lambda

from matplotlib import pyplot as plt
import math
import numpy as np

from scipy.optimize import curve_fit

x = np.linspace(0.16, 0.61, num=46)


y = [-1.526,
     -1.658,
     -1.75,
     -1.804,
     -1.939,
     -2.071,
     -2.147,
     -2.243,
     -2.304,
     -2.4,
     -2.532,
     -2.616,
     -2.672,
     -2.781,
     -2.883,
     -2.94,
     -3.034,
     -3.168,
     -3.265,
     -3.349,
     -3.456,
     -3.518,
     -3.596,
     -3.701,
     -3.816,
     -3.906,
     -3.96,
     -4.054,
     -4.142,
     -4.246,
     -4.348,
     -4.393,
     -4.439,
     -4.57,
     -4.696,
     -4.75,
     -4.837,
     -4.882,
     -4.929,
     -5.015,
     -5.12,
     -5.2,
     -5.244,
     -5.287,
     -5.327,
     -5.383,
     ]

y2 = -8.7507*x-0.2375

# opt, pcov = curve_fit(gaus, x1, y1, p0=[1, mean, sigma])
# a, mu, sigma = popt
# delta_a, delta_mu, delta_sigma = np.sqrt(np.diag(pcov))
# # R^2
# residuals = y1 - gaus(x1, *popt)
# ss_res = np.sum(residuals**2)
# ss_tot = np.sum((y1-np.mean(y1))**2)
# r_squared = 1 - (ss_res / ss_tot)


plt.figure(1)
plt.plot(x, y, color='k', marker='o', markersize=3, linewidth=0, label='Vitesse par rapport au temps')
plt.plot(x, y2, color="blue", label='Équation résultante des coordonnées')
plt.xlabel('Temps (s)')
plt.ylabel('V$_y$ (m/s)')
plt.legend()
plt.grid()
plt.text(0.445, -2.25,'$y = -8.7507x-0.2375$', horizontalalignment='center',
     verticalalignment='center')
plt.savefig('num4.jpg', dpi=600)
