import csv

from buses.events import EventLoopListener


class BusPositionRecorder(EventLoopListener):
    def __init__(self, buses, bus_route):
        self.buses = buses
        self.bus_route = bus_route
        self.events = []

    def on_time_step(self, timestep):
        for bus in self.buses:
            self.events.append({
                "t": timestep,
                "bus": bus.name,
                "pos": self.bus_route.get_route_segment_index(bus.route_segment)
            })

    def save_log(self):
        with open("bus_positions.csv", "w") as f:
            csv_writer = csv.DictWriter(f, ["t", "bus", "pos"])
            csv_writer.writeheader()
            csv_writer.writerows(self.events)
