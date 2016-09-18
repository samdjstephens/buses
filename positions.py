class Position(object):
    def __init__(self, route_segment):
        self.route_segment = route_segment
        self.bus = None

    def is_available(self):
        return self.bus is None or self.bus.is_leaving()

    def on_bus_at_position(self):
        self.route_segment.on_bus_at_position(self.bus)

    def on_leave(self):
        self.bus = None

    def on_arrive(self, bus):
        self.bus = bus

    def on_time_step(self):
        self.route_segment.on_time_step()

