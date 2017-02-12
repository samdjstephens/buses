import random

import itertools
import string

from numpy.random import RandomState

from buses import events
from buses import log
from buses.bus import Bus
from buses.bus_route import BusRoute
from buses.event_recorder import BusPositionRecorder
from buses.passengers import PoissonRandomPassengerGenerator
from buses.route_segments import BusStopSegment, RoadSegment


bus_names = (num for num in xrange(1, 100000))
stop_names = ("".join(letter_comb)
              for letter_comb in itertools.chain(
                list(string.ascii_uppercase),
                itertools.combinations(list(string.ascii_uppercase), 2),
                itertools.combinations(list(string.ascii_uppercase), 3)))


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
        segments = (build_objects(RoadSegment, 50) +
                    build_objects(bus_stop_factory) +
                    build_objects(RoadSegment, 100) +
                    build_objects(bus_stop_factory) +
                    build_objects(RoadSegment, 30))
        log.log.info("Running with {} segments".format(len(segments)))
        self.bus_route = BusRoute(segments)
        self.buses = build_buses(2, segments, self.bus_route)
        self.position_recorder = BusPositionRecorder(self.buses, self.bus_route)
        self.event_loop = events.EventLoop(sleep=0)
        [self.event_loop.register(bus) for bus in self.buses]
        [self.event_loop.register(seg) for seg in segments]
        self.event_loop.register(self.position_recorder)

    def run(self):
        self.event_loop.run(100000)
        self.position_recorder.save_log()


if __name__ == "__main__":
    bus_simulation = BusSimulation()
    bus_simulation.run()
