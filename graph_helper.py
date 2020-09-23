from turtle import pd
from matplotlib import pyplot as plt
import curve_fit as curve_fit
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import glob
import numpy as np

def set_ticks(axes, xMajor, xMinor, xFormat, yMajor, yMinor, yFormat):
    # FAMOUS TICKS
    axes.xaxis.set_major_locator(MultipleLocator(xMajor))
    axes.xaxis.set_major_formatter(FormatStrFormatter(xFormat))
    axes.xaxis.set_minor_locator(MultipleLocator(xMinor))
    axes.yaxis.set_major_locator(MultipleLocator(yMajor))
    axes.yaxis.set_major_formatter(FormatStrFormatter(yFormat))
    axes.yaxis.set_minor_locator(MultipleLocator(yMinor))

def get_data(path, delimiter):
    with open(path, 'r') as file:
        allData = []
        data = np.loadtxt(file, delimiter=delimiter)
        allData.append(data)
        allData = np.asarray(allData)
        return allData


popt, pcov = curve_fit(gaus, x1, y1, p0=[1, mean, sigma])
a, mu, sigma = popt
delta_a, delta_mu, delta_sigma = np.sqrt(np.diag(pcov))
# R^2
residuals = y1 - gaus(x1, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y1-np.mean(y1))**2)
r_squared = 1 - (ss_res / ss_tot)

def gaus(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

fit_param = []

## Fig1
df1 = pd.read_csv('gaussien.csv', sep=";", header=1)
x1 = df1.to_numpy().T[0].astype(float)
y1 = df1.to_numpy().T[1].astype(float)

x1_fit = np.linspace(x1[0], x1[-1], 1000)
plt.plot(x1_fit, gaus(x1_fit, *popt), linewidth=0.5, alpha=0.75, color='C0')