from DisplayElement import DisplayElement
from Observer import Observer
from Observable import Observable

class ForecastDisplay(DisplayElement, Observer):
    def __init__(self) -> None:
        pass

    def update(self, observable: Observable) -> None:
        pass

    def display(self):
        pass
