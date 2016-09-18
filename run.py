from numpy.random import RandomState
import random

from buses.bus import Bus
from buses.bus_route import BusRoute
from buses.bus_segments import BusStopSegment, RoadSegment
from buses.passengers import PoissonRandomPassengerGenerator
from buses.positions import Position


def build_objects(factory, n=1):
    return [factory() for _ in xrange(n)]


def bus_stop_factory():
    passenger_generator = PoissonRandomPassengerGenerator(RandomState(), 1)
    init_passengers = RandomState().randrange(10)
    return BusStopSegment(passenger_generator, init_passengers)


def build_buses(n_buses, positions, bus_route):
    positions = positions[:]
    random.shuffle(positions)
    return [Bus(bus_route, pos) for i, pos in zip(range(n_buses), positions)]


class BusSimulation(object):
    def __init__(self):
        segments = 20 * (build_objects(RoadSegment, 10) +
                         build_objects(bus_stop_factory) +
                         build_objects(RoadSegment, 10))
        positions = [Position(segment) for segment in segments]
        self.bus_route = BusRoute(positions)
        self.buses = build_buses(10, positions, self.bus_route)


if __name__ == "__main__":
    bus_simulation = BusSimulation()