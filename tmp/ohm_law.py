import lib.environments.base as base


class OhmLawEnvironment(base.EnvironmentBase):
    def __init__(self):
        super().__init__()

    def connect(self):
        super().connect()

    def disconnect(self):
        super().disconnect()

    def run_experiments(self, input_data):
        super().run_experiments(input_data)
        self._inputs = input_data
        self._outputs = [x[0] * x[1] for x in self._inputs]
        self._experiments_finished = True

    def are_experiments_finished(self):
        return super().are_experiments_finished()

    def get_experiments_results(self):
        return super().get_experiments_results()
