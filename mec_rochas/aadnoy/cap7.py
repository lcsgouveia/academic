# coding: utf-8
import pint

ureg = pint.UnitRegistry()

# Exemplo 7.1
porosity = 0
rho_rocha = 2.67 * ureg.gram / ureg.cm ** 3
h = 10 * ureg.meter
gravidade = 9.81 * ureg.meter / ureg.second ** 2

sigma_normal = rho_rocha * gravidade * h
sigma_efet = sigma_normal - porosity

print sigma_normal.to(ureg.kilopascal)
print sigma_efet.to(ureg.kilopascal)

# Exercício 7.1
porosity = 0.2

sigma_normal = sigma_normal * (1 - 0.2)
print sigma_normal.to(ureg.kilopascal)

# Exercício 7.2
rho_agua = 1000 * ureg.kilogram / ureg.meter ** 3
sigma_normal = sigma_normal + rho_agua * gravidade * h * (1. - porosity)

print sigma_normal.to(ureg.kilopascal)