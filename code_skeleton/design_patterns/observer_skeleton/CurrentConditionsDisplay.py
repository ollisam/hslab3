from DisplayElement import DisplayElement
from Observer import Observer
from Observable import Observable


class CurrentConditionsDisplay(DisplayElement, Observer):
    def __init__(self, observable: Observable) -> None:
        self._observable = observable
        self._observable.register_observer(self)
        self._temperature = 0.0
        self._humidity = 0.0
        
    def update(self, observable: Observable) -> None:
        measurements = observable.get_measurements()
        self._temperature = measurements.temperature
        self._humidity = measurements.humidity
        self.display

    def display(self) -> None:
        print(f'Current conditions: {self._temperature}F degrees and {self._humidity}% humidity')

