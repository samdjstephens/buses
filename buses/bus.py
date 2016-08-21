class Bus(object):
    def __init__(self, init_state, position):
        self.state = init_state
        self.position = position

    def step(self):
        self.state.get_next_allowed_position()