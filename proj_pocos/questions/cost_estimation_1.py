# -*- coding: cp1252 -*-

from proj_pocos.cost_estimation.drill_cost import Bit, DrillCost

bit_a = Bit(1000, 15, 14)
bit_b = Bit(3000, 35, 13)
bit_c = Bit(4000, 45, 10)
bit_d = Bit(4500, 65, 11)

trip_time = 10
single_connection_time = 1./60.
rig_cost_per_hour = 12000./24.

Cd_a = DrillCost(bit_a, rig_cost_per_hour, single_connection_time, trip_time=trip_time)
Cd_b = DrillCost(bit_b, rig_cost_per_hour, single_connection_time, trip_time=trip_time)
Cd_c = DrillCost(bit_c, rig_cost_per_hour, single_connection_time, trip_time=trip_time)
Cd_d = DrillCost(bit_d, rig_cost_per_hour, single_connection_time, trip_time=trip_time)

print Cd_a.drill_cost(), Cd_b.drill_cost(), Cd_c.drill_cost(), Cd_d.drill_cost()