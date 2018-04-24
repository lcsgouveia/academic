# -*- coding: cp1252 -*-

class Bit:

    def __init__(self, cost, rotating_time, rate_of_penetration):

        self.cost = cost
        self.rotating_time = rotating_time
        self.rate_of_penetration = rate_of_penetration

    def depth_to_drill(self):

        return self.rate_of_penetration * self.rotating_time


class DrillCost:

    # TODO permitir cálculo do custo em intervalo específico de perfuração
    def __init__(self, bit, rig_cost_per_hour, connection_time, trip_time = 'to_calculate', section_length = 30, disconnection_time = 'equal_connection'):

        self.bit = bit
        self.rig_cost_per_hour = rig_cost_per_hour
        self.connection_time = connection_time
        self.section_length = section_length
        self.trip_time = trip_time

        if disconnection_time == 'equal_connection':
            self.disconnection_time = connection_time

    def connections_time(self): #TODO fazer cálculo para intervalo específico de perfuração
        return self.bit.depth_to_drill() * self.connection_time / self.section_length

    def drill_cost(self):

        total_time = self.trip_time + self.connections_time() + self.bit.rotating_time

        return (self.bit.cost + self.rig_cost_per_hour * total_time) / self.bit.depth_to_drill()