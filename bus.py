from buses.bus_state import Travelling, AtBusStop
from buses.events import EventLoopListener
from buses.route_segments import BusStopSegment
from buses.log import log


class Bus(EventLoopListener):
    def __init__(self, bus_route, route_segment, name=None):
        self.bus_route = bus_route
        self.route_segment = route_segment
        self.state = Travelling
        self.name = name

    def __repr__(self):
        return "Bus {}".format(self.name)

    def on_time_step(self, *args):
        log.debug("{}: {}".format(self, self.state))
        if self.state == AtBusStop:
            bus_stop = self.route_segment
            self.load_passengers_from(bus_stop)
        elif self.state == Travelling:
            self.update_position()

    def update_position(self):
        self.route_segment.on_bus_leave()
        self.route_segment = self.bus_route.get_next_allowed_segment(self.route_segment)
        self.route_segment.on_bus_arrive()
        if isinstance(self.route_segment, BusStopSegment):
            self.set_state(AtBusStop)

    def load_passengers_from(self, bus_stop):
        passenger = bus_stop.load_passenger()
        if passenger is None:
            self.set_state(Travelling)
        else:
            log.debug("{}: Passenger got on bus {}".format(self.route_segment,
                                                           self))
            self.set_state(AtBusStop)

    def set_state(self, state):
        self.state = state
