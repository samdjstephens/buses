from buses.bus_travel_states import (BusTravelState, TravellingState,
                                     LoadingState)
from buses.events import event_loop


class Position(object):
    bus_state_type = BusTravelState

    def on_bus_at_position(self, bus):
        pass


class RoadPosition(Position):
    bus_state_type = TravellingState

    def on_bus_at_position(self, bus):
        pass


class StopPosition(Position):
    bus_state_type = LoadingState

    def __init__(self, passenger_generator, init_passenger_count=0):
        self.passenger_generator = passenger_generator
        self.passenger_count = init_passenger_count
        event_loop.register(self)

    def on_bus_at_position(self, bus):
        self.load_passenger()

    def load_passenger(self):
        if self.passenger_count > 0:
            self.passenger_count -= 1
        else:
            pass  # Do what?

    def on_time_step(self):
        self.passenger_count += self.passenger_generator.generate()
