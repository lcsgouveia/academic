from proj_pocos.well_stimulation.fracking.fracking_design import Fracking

Vf = 216.5
kf = 60000
k1 = 0.5
hf = 65
re = 2100
rw = 0.328
s = 5

my_frac_1 = Fracking(reservoir_permeability=k1, propant_permeability=kf, propant_volume=Vf, frac_height=hf,
                     well_radius=rw, drenage_radius=re, skin_before=s)

print my_frac_1.get_frac_length(), my_frac_1.get_frac_width()*12, my_frac_1.folds_of_increase()