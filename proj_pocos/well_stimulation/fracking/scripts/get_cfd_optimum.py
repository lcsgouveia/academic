import numpy as np
from matplotlib.pyplot import plot, xscale, show
from numpy.matlib import rand, log
from scipy.misc import derivative

from proj_pocos.well_stimulation.fracking.fracking_design import Fracking, CincoLeySamaniego

my_frac_design = Fracking()

print my_frac_design.cfd

cfds = np.linspace(1e-1, 100, 1000)
y = []
for cfd in cfds:

    cinco = CincoLeySamaniego(cfd=cfd)

    y.append(cinco.polynomial_factor + 0.5 * log(cfd))


plot(cfds, y)
xscale("log")
show()