from buses.events import event_loop


class Bus(object):
    def __init__(self, init_state, position):
        self.state = init_state
        self.position = position
        event_loop.register(self)

    def on_time_step(self):
        self.position.on_bus_at_position(self)
        self.position = self.state.get_next_position(self.position)
