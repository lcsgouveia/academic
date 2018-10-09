import numpy as np
from matplotlib.pyplot import plot, show
from numpy.matlib import rand

from proj_pocos.well_stimulation.fracking.productivity_index import PseudoSteadyFlow

re = 6400
rw = 1.

k = float(rand(1))
h = float(rand(1))
B = float(rand(1))
mu = float(rand(1))

j_no_skin = PseudoSteadyFlow(k, h, B, mu, re, rw, skin=0.0).productivity_index

skins = np.linspace(-5, 25, 100)
folds_of_increase = []
for s in skins:

    j = PseudoSteadyFlow(k, h, B, mu, re, rw, skin=s).productivity_index

    folds_of_increase.append(j / j_no_skin)


plot(skins, folds_of_increase)
show()