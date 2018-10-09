from math import pi, log


class ProductivityIndex:

    def __init__(self, reservoir_permeability, net_thickness, formation_volume_factor, viscosity, p_d):

        self.reservoir_permeability = reservoir_permeability
        self.net_thickness = net_thickness
        self.formation_volume_factor = formation_volume_factor
        self.viscosity = viscosity
        self.p_d = p_d

        self.productivity_index = 2. * pi * self.reservoir_permeability * self.net_thickness / \
                                  (self.formation_volume_factor * self.viscosity * self.p_d)


class TransientFlow(ProductivityIndex):

    def __init__(self, reservoir_permeability, net_thickness, formation_volume_factor, viscosity,
                 E, i, t, phi, ct, rw, skin=0.0):

        t_d = reservoir_permeability * t / (phi * viscosity * ct * rw ** 2)
        p_d = -0.5 * E * i * (-0.25 / t_d) + skin

        ProductivityIndex.__init__(self, reservoir_permeability=reservoir_permeability,
                                   net_thickness=net_thickness,
                                   formation_volume_factor=formation_volume_factor,
                                   viscosity=viscosity,
                                   p_d=p_d)


class SteadyFlow(ProductivityIndex):

    def __init__(self, reservoir_permeability, net_thickness, formation_volume_factor, viscosity, re, rw, skin=0.0):

        p_d = log(re/rw) + skin

        ProductivityIndex.__init__(self, reservoir_permeability=reservoir_permeability,
                                   net_thickness=net_thickness,
                                   formation_volume_factor=formation_volume_factor,
                                   viscosity=viscosity,
                                   p_d=p_d)


class PseudoSteadyFlow(ProductivityIndex):

    def __init__(self, reservoir_permeability, net_thickness, formation_volume_factor, viscosity, re, rw, skin=0.0):

        p_d = log(0.472*re/rw) + skin

        ProductivityIndex.__init__(self, reservoir_permeability=reservoir_permeability,
                                   net_thickness=net_thickness,
                                   formation_volume_factor=formation_volume_factor,
                                   viscosity=viscosity,
                                   p_d=p_d)


