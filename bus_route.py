class BusRoute(object):
    def __init__(self, positions):
        self._positions = positions

    def get_next_allowed_position(self, current_position):
        next_position_ix = ((self._positions.index(current_position) + 1) %
                            len(self._positions))
        next_position = self._positions[next_position_ix]
        if not next_position.is_available():
            next_position = self.get_next_allowed_position(next_position)
        return next_position
