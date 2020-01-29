import logging

class UnimplementedError(Exception):
    """Raised when no Implementation exists."""
    pass


class NoConnectionError(Exception):
    """No connection with Environment. Make sure to connect before running experiments."""
    pass


class ExperimentsRunningError(Exception):
    """Experiments are still running. Make sure experiments are finished before collecting the results."""
    pass


class EnvironmentBase(object):
    def __init__(self):
        self._logger = logging.getLogger('Environment logger')
        self._connected = False
        self._inputs = None
        self._outputs = None
        self._experiments_finished = None

    def connect(self):
        self._inputs = []
        self._outputs = []
        self._experiments_finished = True
        self._logger.info('Connected to Environment.')

    def disconnect(self):
        self._inputs = None
        self._outputs = None
        self._experiments_finished = None
        print('Disconnected from the Environment.\nInputs and Outputs are cleared.')

    def run_experiments(self, input_data):
        if not self._connected:
            raise NoConnectionError
        self._experiments_finished = False

    def are_experiments_finished(self):
        if not self._connected:
            raise NoConnectionError
        return self._experiments_finished

    def get_experiments_results(self):
        if not self._connected:
            raise NoConnectionError
        if not self.are_experiments_finished():
            raise ExperimentsRunningError
        return self._outputs
