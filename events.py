from time import sleep

from buses.log import log


class EventLoopListener(object):
    def on_time_step(self, timestep):
        pass


class EventLoop(object):
    def __init__(self, sleep=2):
        self.listeners = []
        self.sleep = sleep

    def register(self, listener):
        if not isinstance(listener, EventLoopListener):
            raise TypeError("Listener not of type: %s", type(EventLoopListener))
        self.listeners.append(listener)

    def run(self, steps):
        for timestep in xrange(1, steps+1):
            sleep(self.sleep)
            log.debug("\n*** Step ***")
            for listener in self.listeners:
                listener.on_time_step(timestep)

