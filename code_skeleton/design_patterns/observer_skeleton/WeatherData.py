from IWeatherData import IWeatherData
from Observable import Observable
from WeatherDataMeasurements import WeatherDataMeasurements
from Observer import Observer

class WeatherData(IWeatherData, Observable):
    def __init__(self) -> None:
        self._observers = []
        self._measurements = None

    def register_observer(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def set_measurements(self, measurements: WeatherDataMeasurements) -> None:
        self._measurements = measurements
        self.notify_observers()

    def get_measurements(self) -> WeatherDataMeasurements:
        return self._measurements


