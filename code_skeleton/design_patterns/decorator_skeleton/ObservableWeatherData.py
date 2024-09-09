from abc import ABC, ABCMeta

from IWeatherData import IWeatherData
from Observable import Observable
from Observer import Observer
from WeatherData import WeatherData
from WeatherDataMeasurements import WeatherDataMeasurements


class ObservableWeatherData(Observable, IWeatherData, ABC):
    def __init__(self, weather_data: WeatherData = None) -> None:
        self._weather_data = weather_data
        self._prev_measurements = None

    def register_observer(self, observer: Observer) -> None:
        self._weather_data.register_observer(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._weather_data.remove_observer(observer)

    def notify_observers(self) -> None:
        self._weather_data.notify_observers()

    def set_measurements(self, measurements: WeatherDataMeasurements) -> None:
        if self._prev_measurements:
            if (abs(measurements.temperature - self._prev_measurements.temperature) >= 1 or
               abs(measurements.humidity - self._prev_measurements.humidity) >= 1 or
               abs(measurements.pressure - self._prev_measurements.pressure) >= 1):
                
                self._prev_measurements = measurements
                self._weather_data.set_measurements(measurements)

        else:
            self._prev_measurements = measurements
            self._weather_data.set_measurements(measurements)

    def get_measurements(self) -> WeatherDataMeasurements:
        self._weather_data.get_measurements()
