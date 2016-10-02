import random

import itertools
import string

from numpy.random import RandomState

from buses import events
from buses.bus import Bus
from buses.bus_route import BusRoute
from buses.passengers import PoissonRandomPassengerGenerator
from buses.route_segments import BusStopSegment, RoadSegment


bus_names = (num for num in xrange(1, 100000))
stop_names = ("".join(letter_comb)
              for letter_comb in itertools.combinations(string.ascii_uppercase,
                                                        3))


def build_objects(factory, n=1):
    return [factory() for _ in xrange(n)]


def bus_stop_factory():
    passenger_generator = PoissonRandomPassengerGenerator(RandomState(), 2)
    init_passengers = random.randrange(2)
    return BusStopSegment(passenger_generator, init_passengers, name=stop_names.next())


def build_buses(n_buses, segments, bus_route):
    segments = segments[:]
    random.shuffle(segments)
    buses = []
    for _ in range(n_buses):
        seg = segments.pop()
        bus = Bus(bus_route, seg, name=bus_names.next())
        buses.append(bus)
    return buses


class BusSimulation(object):
    def __init__(self):
        segments = (build_objects(RoadSegment, 5) +
                    build_objects(bus_stop_factory) +
                    build_objects(RoadSegment, 5))
        self.bus_route = BusRoute(segments)
        self.buses = build_buses(1, segments, self.bus_route)
        self.event_loop = events.EventLoop()
        [self.event_loop.register(bus) for bus in self.buses]
        [self.event_loop.register(seg) for seg in segments]

    def run(self):
        self.event_loop.run()


if __name__ == "__main__":
    bus_simulation = BusSimulation()
    bus_simulation.run()
