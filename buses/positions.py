from buses.bus_travel_states import (BusTravelState, TravellingState,
                                     LoadingState)


class Position(object):
    bus_state_type = BusTravelState


class RoadPosition(Position):
    bus_state_type = TravellingState


class StopPosition(Position):
    bus_state_type = LoadingState
