class Bus(object):
    def __init__(self, bus_route, position):
        self.bus_route = bus_route
        self.position = position

    def on_time_step(self):
        if self.position.bus_is_leaving:
            self.update_position()
        self.position.on_bus_at_position()

    def update_position(self):
        self.position.on_leave()
        self.position = self.bus_route.get_next_position()
        self.position.on_arrive(self)

    def load_passengers(self, n_passengers):
        if n_passengers == 0:
            self.set_state("moving")
        else:
            self.set_state("stopped")

    def set_state(self, state):
        self.state = state

