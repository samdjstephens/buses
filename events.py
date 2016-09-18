from time import sleep


class EventLoop(object):
    def __init__(self, sleep=2):
        self.listeners = []
        self.sleep = sleep

    def register(self, listener):
        self.listeners.append(listener)

    def run(self):
        while True:
            sleep(self.sleep)
            print "Step"
            for listener in self.listeners:
                listener.on_time_step()
