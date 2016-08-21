class BusTravelState(object):
    def __init__(self, bus_route):
        self.bus_route = bus_route

    def get_next_position(self, current_position):
        raise NotImplementedError


class LoadingState(BusTravelState):
    def __init__(self, bus_route):
        super(LoadingState, self).__init__(bus_route)

    def get_next_position(self, current_position):
        return current_position


class TravellingState(BusTravelState):
    def __init__(self, bus_route):
        super(TravellingState, self).__init__(bus_route)

    def get_next_position(self, current_position):
        return self.bus_route.get_next_allowed_position(current_position)
