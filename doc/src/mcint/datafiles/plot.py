import numpy as np
from  matplotlib import pyplot as plt
# Load in data file
data = np.loadtxt("autocor.dat")
# Make arrays containing x-axis and binding energies as function of A
x = data[:,0]
corr = data[:,1]
plt.plot(x, corr ,'ro')
plt.axis([0,1000,-0.2, 1.1])
plt.xlabel(r'$d$')
plt.ylabel(r'$C_d$')
plt.title(r'autocorrelation function for RNG')
plt.savefig('autocorr.pdf')
plt.show()
