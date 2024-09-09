from DisplayElement import DisplayElement
from IWeatherData import IWeatherData
from Observer import Observer
from Observable import Observable

class ForecastDisplay(DisplayElement, Observer):
    def __init__(self, observable: Observable = None) -> None:
        self._observable = observable
        if self._observable:
            self._observable.register_observer(self)
        self._last_pressure = None
        self._current_pressure = 0

    def update(self, observable: Observable) -> None:
        if isinstance(observable, IWeatherData):
            measurements = observable.get_measurements()
            self._last_pressure = self._current_pressure
            self._current_pressure = measurements.pressure
            self.display()

    def display(self):
        if self._current_pressure > self._last_pressure:
            print('Forecast: Improving weather on the way!')
        elif self._current_pressure < self._last_pressure:
            print('Forecast: Watch out for cooler, rainy weather')
        elif self._current_pressure == self._last_pressure:
            print('Forecast: More of the same')
