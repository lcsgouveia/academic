from cmath import log, sqrt

from numpy.matlib import rand
from scipy.misc import derivative
from scipy.optimize import fsolve

from proj_pocos.well_stimulation.fracking.productivity_index import PseudoSteadyFlow, ProductivityIndex


class CincoLeySamaniego:

    def __init__(self, cfd):

        self.cfd = cfd
        self.u = log(self.cfd)

        self.polynomial_factor = (1.65 - 0.328 * self.u + 0.116 * self.u ** 2) / \
                                 (1 + 0.18 * self.u + 0.064 * self.u ** 2 + 0.005 * self.u ** 3)

    def pseudo_skin(self, frac_length, well_radius):

        return log(well_radius/frac_length) + self.polynomial_factor


class Fracking:

    def __init__(self, reservoir_permeability=None, propant_permeability=None, propant_volume=None, frac_height=None,
                 formation_volume_factor=None, viscosity=None, drenage_radius=None, well_radius=None,
                 skin_before=None, cfd='optimal'):

        self.reservoir_permeability = reservoir_permeability
        self.propant_permeability = propant_permeability
        self.propant_volume = propant_volume
        self.frac_height = frac_height
        self.formation_volume_factor = formation_volume_factor
        self.viscosity = viscosity
        self.drenage_radius = drenage_radius
        self.well_radius = well_radius
        self.skin_before = skin_before
        self.cfd = cfd if cfd is not 'optimal' else self.get_optimal_cfd()

    def get_optimal_cfd(self):

        f = lambda cfd: 0.5 * log(cfd) + CincoLeySamaniego(cfd).polynomial_factor
        df = lambda cfd: derivative(f, cfd, dx=1e-6)

        return fsolve(df, 2)

    def get_frac_length(self):

        return sqrt(self.propant_volume * self.propant_permeability /
                    (self.cfd * self.frac_height * self.reservoir_permeability))

    def get_frac_width(self):

        return sqrt(self.cfd * self.propant_volume * self.reservoir_permeability /
                    (self.frac_height * self.propant_permeability))

    def get_productivity_index_before(self):

        return PseudoSteadyFlow(reservoir_permeability=self.reservoir_permeability,
                                net_thickness=self.frac_height,
                                formation_volume_factor=self.formation_volume_factor,
                                viscosity=self.viscosity,
                                re=self.drenage_radius,
                                rw=self.well_radius,
                                skin=self.skin_before).productivity_index

    def get_productivity_index_after(self):

        new_p_d = log(0.472*self.drenage_radius) + \
                  0.5*log(
            self.frac_height*self.reservoir_permeability /
            (self.propant_volume*self.propant_permeability)
        ) + 0.5*log(self.cfd) + CincoLeySamaniego(cfd=self.cfd).polynomial_factor

        return ProductivityIndex(reservoir_permeability=self.reservoir_permeability,
                                net_thickness=self.frac_height,
                                formation_volume_factor=self.formation_volume_factor,
                                viscosity=self.viscosity,
                                p_d=new_p_d)

    def folds_of_increase(self):

        return (log(0.472*self.drenage_radius/self.well_radius) + self.skin_before) / \
               (log(0.472*self.drenage_radius /
                    sqrt(self.propant_permeability * self.propant_volume /
                         (self.frac_height * self.reservoir_permeability)))
                + 1.619020167)


