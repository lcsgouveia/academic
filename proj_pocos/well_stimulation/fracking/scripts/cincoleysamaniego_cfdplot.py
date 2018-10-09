import numpy as np
from matplotlib.pyplot import plot, show, xscale
from numpy.matlib import rand

from proj_pocos.well_stimulation.fracking.fracking_design import CincoLeySamaniego

cfds = np.linspace(1e-1, 1000, 1000)
polynomial_factors = []
for cfd in cfds:

    cinco = CincoLeySamaniego(cfd=cfd)

    polynomial_factors.append(cinco.polynomial_factor)


plot(cfds, polynomial_factors)
xscale("log")
show()
