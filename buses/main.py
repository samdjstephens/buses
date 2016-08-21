class BusRoute(object):
    def __init__(self, positions):
        self._positions = positions

    def get_next_allowed_position(self, current_position):
        return self._positions[(self._positions.index(current_position) + 1) %
                               len(self._positions)]


class Position(object):
    bus_state_type = BusTravelState


class RoadPosition(Position):
    bus_state_type = TravellingState


class StopPosition(Position):
    bus_state_type = LoadingState


class Bus(object):
    def __init__(self, init_state, position):
        self.state = init_state
        self.position = position

    def step(self):
        self.state.get_next_allowed_position()


class BusTravelState(object):
    def __init__(self, position, bus_route):
        self.position = position
        self.bus_route = bus_route

    def get_next_position(self):
        raise NotImplementedError


class LoadingState(BusTravelState):
    def __init__(self, position, bus_route):
        super(LoadingState, self).__init__(position, bus_route)

    def get_next_position(self):
        pass


class TravellingState(BusTravelState):
    def __init__(self, position, bus_route):
        super(TravellingState, self).__init__(position, bus_route)

    def get_next_position(self):
        self.position = self.bus_route.get_next_allowed_position(self.position)


class EventLoop(object):
    pass
