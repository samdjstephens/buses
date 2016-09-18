class PassengerGenerator(object):
    def __init__(self, random_state):
        self.random_state = random_state

    def generate(self):
        raise NotImplementedError


class PoissonRandomPassengerGenerator(PassengerGenerator):
    def __init__(self, random_state, lambda_):
        self.lambda_ = lambda_
        super(PoissonRandomPassengerGenerator, self).__init__(random_state)

    def generate(self):
        return self.random_state.poisson(self.lambda_)
