class RouteSegment(object):
    def on_bus_at_position(self, bus):
        pass

    def on_time_step(self):
        pass


class RoadSegment(RouteSegment):
    def on_bus_at_position(self, bus):
        pass

    def on_time_step(self):
        pass


class BusStopSegment(RouteSegment):
    def __init__(self, passenger_generator, init_passenger_count=0):
        super(BusStopSegment, self).__init__()
        self.passenger_generator = passenger_generator
        self.passenger_count = init_passenger_count

    def on_bus_at_position(self, bus):
        self.load_passenger(bus)

    def load_passenger(self, bus):
        if self.passenger_count > 0:
            to_load = 1
            self.passenger_count -= to_load
        else:
            to_load = 0
        bus.load_passengers(to_load)

    def on_time_step(self):
        self.passenger_count += self.passenger_generator.generate()
