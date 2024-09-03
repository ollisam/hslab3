from IWeatherData import IWeatherData
from Observable import Observable
from WeatherDataMeasurements import WeatherDataMeasurements
from Observer import Observer

class WeatherData(IWeatherData, Observable):
    def __init__(self) -> None:
        pass

    def register_observer(self, observer: Observer) -> None:
        pass

    def remove_observer(self, observer: Observer) -> None:
        pass

    def notify_observers(self) -> None:
        pass

    def set_measurements(self, measurements: WeatherDataMeasurements) -> None:
        pass

    def get_measurements(self) -> WeatherDataMeasurements:
        pass


