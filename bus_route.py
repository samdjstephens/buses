class BusRoute(object):
    def __init__(self, route_segments):
        self._segments = route_segments

    def get_next_allowed_segment(self, current_segment):
        next_segment_ix = ((self.get_route_segment_index(current_segment) + 1) %
                            len(self._segments))
        next_segment = self._segments[next_segment_ix]
        if not next_segment.is_available:
            next_segment = self.get_next_allowed_segment(next_segment)
        return next_segment

    def get_route_segment_index(self, route_segment):
        return self._segments.index(route_segment)
