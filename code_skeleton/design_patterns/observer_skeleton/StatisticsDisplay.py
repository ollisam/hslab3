from DisplayElement import DisplayElement
from IWeatherData import IWeatherData
from Observer import Observer
from Observable import Observable


class StatisticsDisplay(DisplayElement, Observer):
    def __init__(self, observable: Observable = None) -> None:
        self._observerable = observable
        if self._observerable:
            self._observerable.register_observer(self)
        self._temp_sum = 0.0
        self._num_measurements = 0
        self._max_temp = -1000
        self._min_temp = 1000

    def update(self, observable: Observable) -> None:
        if isinstance(observable, IWeatherData):
            measurements = observable.get_measurements()
            temp = measurements.temperature
            self._temp_sum += temp
            self._num_measurements += 1

            if self._max_temp < temp:
                self._max_temp = temp

            if self._min_temp > temp:
                self._min_temp = temp

        self.display()

    def display(self) -> None:
        avg_temp = self._temp_sum / self._num_measurements
        print(f'Avg/Max/Min temperature = {avg_temp:.1f}/{self._max_temp:.1f}/{self._min_temp:.1f}')

