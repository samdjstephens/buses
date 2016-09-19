import logging

log = logging.getLogger("buses")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())


class Bus(object):
    def __init__(self, bus_route, position):
        self.bus_route = bus_route
        self.position = position
        self.state = "moving"

    def on_time_step(self):
        if self.state == "leaving":
            log.debug("leaving bus stop")
            self.update_position()
            self.set_state("moving")
        elif self.state == "moving":
            log.debug("travelling")
            self.update_position()
            self.position.on_bus_at_position()
        elif self.state == "stopped":
            log.debug("bus stopped")
            self.position.on_bus_at_position()

    def update_position(self):
        self.position.on_leave()
        self.position = self.bus_route.get_next_allowed_position(self.position)
        self.position.on_arrive(self)

    def load_passengers(self, n_passengers):
        log.debug("{} passengers loading on bus".format(n_passengers))
        if n_passengers == 0:
            self.set_state("leaving")
        else:
            self.set_state("stopped")

    def set_state(self, state):
        self.state = state

    def is_leaving(self):
        return self.state in ["leaving", "moving"]
