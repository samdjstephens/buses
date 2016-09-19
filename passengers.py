class PassengerGenerator(object):
    def __init__(self, random_state):
        self.random_state = random_state

    def generate(self):
        raise NotImplementedError


class PoissonRandomPassengerGenerator(PassengerGenerator):
    def __init__(self, random_state, lambda_):
        super(PoissonRandomPassengerGenerator, self).__init__(random_state)
        self.lambda_ = lambda_
        self.new_passenger_in = None
        self.set_new_passenger_in_delay()

    def set_new_passenger_in_delay(self):
        self.new_passenger_in = self.random_state.poisson(self.lambda_)

    def generate(self):
        if self.new_passenger_in == 0:
            passengers = 1
            self.set_new_passenger_in_delay()
        else:
            self.new_passenger_in -= 1
            passengers = 0
        return passengers
