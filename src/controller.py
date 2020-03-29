from time import sleep
from src.database import Database
from src.telemetry import Telemetry


class Controller:
    def __init__(self) -> None:
        self.database = Database()

    def run(self) -> None:
        humidity = 850
        while True:
            print("Controller running")
            tm = Telemetry()
            tm.set(humidity=humidity,
                   temperature=30,
                   pressure=15,
                   luminosity=0.8,
                   lamps=1,
                   airfan=0,
                   heater=1,
                   timestamp=self.database.now())
            self.database.add_telemetry(tm)
            humidity += 1
            sleep(1)
