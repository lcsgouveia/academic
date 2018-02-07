# coding: utf-8
import pint

unit = pint.UnitRegistry()

# Exemplo 6.1
gamma = 2.38

rho_agua = 1000 * unit.kilogram / unit.meter**3
gravidade = 9.806 * unit.meter / unit.second**2

gamma_agua = rho_agua * gravidade

gamma_rocha = gamma_agua * gamma

unit.auto_reduce_dimensions = True
print gamma_rocha.to(unit.kilonewton / unit.meter**3)
print gamma_rocha.to(unit.lbf / unit.ft**3)

# Problema 6.2
gradiente_pressao = 3.3
prof = 3000 * unit.ft

pressao = gradiente_pressao * gamma_agua * prof

print pressao.to(unit.kilopascal)