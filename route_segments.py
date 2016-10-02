from buses.log import log


class RouteSegment(object):
    def on_bus_arrive(self):
        pass

    def on_bus_leave(self):
        pass

    def on_time_step(self):
        pass


class RoadSegment(RouteSegment):
    is_available = True

    def on_bus_arrive(self):
        pass

    def on_bus_leave(self):
        pass

    def on_time_step(self):
        pass


class BusStopSegment(RouteSegment):
    def __init__(self, passenger_generator, init_passenger_count=0, name=None):
        super(BusStopSegment, self).__init__()
        self.passenger_generator = passenger_generator
        self.passenger_count = init_passenger_count
        self.is_available = True
        self.name = name

    def __repr__(self):
        return "Stop {}".format(self.name)

    def on_bus_arrive(self):
        self.is_available = False

    def on_bus_leave(self):
        self.is_available = True

    def load_passenger(self):
        if self.passenger_count > 0:
            to_load = 1
            self.passenger_count -= to_load
        else:
            to_load = None
        return to_load

    def on_time_step(self):
        new_passengers = self.passenger_generator.generate()
        self.passenger_count += new_passengers
        if new_passengers == 1:
            log.debug("{}: 1 passenger arrived."
                      " Now there are {}".format(self,
                                                 self.passenger_count))
