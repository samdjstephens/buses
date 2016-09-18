class Position(object):
    def __init__(self, route_segment):
        self.route_segment = route_segment
        self.bus = None
        self.bus_is_leaving = False

    def is_available(self):
        return self.bus is not None and self.bus_is_leaving

    def on_bus_at_position(self, bus):
        self.route_segment.on_bus_at_position(bus)

    def on_leave(self):
        self.bus = None

    def on_arrive(self, bus):
        self.bus = bus
