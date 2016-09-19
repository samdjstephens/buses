from numpy.random import RandomState
import random

from buses import events
from buses.bus import Bus
from buses.bus_route import BusRoute
from buses.bus_segments import BusStopSegment, RoadSegment
from buses.passengers import PoissonRandomPassengerGenerator
from buses.positions import Position


def build_objects(factory, n=1):
    return [factory() for _ in xrange(n)]


def bus_stop_factory():
    passenger_generator = PoissonRandomPassengerGenerator(RandomState(), 2)
    init_passengers = random.randrange(2)
    return BusStopSegment(passenger_generator, init_passengers)


def build_buses(n_buses, positions, bus_route):
    positions = positions[:]
    random.shuffle(positions)
    buses = []
    for _ in range(n_buses):
        pos = positions.pop()
        bus = Bus(bus_route, pos)
        pos.bus = bus
        buses.append(bus)
    return buses


class BusSimulation(object):
    def __init__(self):
        segments = (build_objects(RoadSegment, 5) +
                    build_objects(bus_stop_factory) +
                    build_objects(RoadSegment, 5))
        positions = [Position(segment) for segment in segments]
        self.bus_route = BusRoute(positions)
        self.buses = build_buses(1, positions, self.bus_route)
        self.event_loop = events.EventLoop()
        [self.event_loop.register(bus) for bus in self.buses]
        [self.event_loop.register(pos) for pos in positions]

    def run(self):
        self.event_loop.run()


if __name__ == "__main__":
    bus_simulation = BusSimulation()
    bus_simulation.run()
