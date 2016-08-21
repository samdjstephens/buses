class BusRoute(object):
    def __init__(self, positions):
        self._positions = positions

    def get_next_allowed_position(self, current_position):
        return self._positions[(self._positions.index(current_position) + 1) %
                               len(self._positions)]