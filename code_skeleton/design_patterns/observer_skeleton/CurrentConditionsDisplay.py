from DisplayElement import DisplayElement
from Observer import Observer
from Observable import Observable
from IWeatherData import IWeatherData


class CurrentConditionsDisplay(DisplayElement, Observer):
    def __init__(self, observable: Observable = None) -> None:
        self._observable = observable
        if self._observable:
            self._observable.register_observer(self)
        self._temperature = 0.0
        self._humidity = 0.0
        
    def update(self, observable: Observable) -> None:
        if isinstance(observable, IWeatherData):
            measurements = observable.get_measurements()
            self._temperature = measurements.temperature
            self._humidity = measurements.humidity
            self.display()

    def display(self) -> None:
        print(f'Current conditions: {self._temperature:.1f}F degrees and {self._humidity:.1f}% humidity')

