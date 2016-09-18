class EventLoop(object):
    def __init__(self):
        self.listeners = []

    def register(self, listener):
        self.listeners.append(listener)

    def run(self):
        while True:
            for listener in self.listeners:
                listener.on_time_step()


event_loop = EventLoop()
