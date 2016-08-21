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