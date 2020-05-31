from time import sleep
from datetime import datetime
from src.database import Database
from src.telemetry import Telemetry
import shutil
import os


class Controller:
    humidity = 850
    temperature = 20
    pressure = 15
    airfan = 0
    lamps = 1

    def __init__(self) -> None:
        self.database = Database()

    def run(self) -> None:
        while True:
            sleep(1)

            tm = self.take_telemetry()
            self.database.add_telemetry(tm)

            (tc, tc_id) = self.database.get_next_unexecuted_tc()
            if tc_id is not None:
                self.process_tc(tc)
                if tc == "SHUTDOWN":
                    print("shutting down...")
                    self.database.set_tc_as_executed(tc_id)
                    self.database.add_error("SHUTDOWN telecommand received")
                    os._exit(0)
                self.database.set_tc_as_executed(tc_id)

    def process_tc(self, tc: str) -> None:
        if tc == "TAKE PHOTO":
            self.take_photo()
        elif tc == "TURN ON LIGHTS":
            pass
        elif tc == "TURN OFF LIGHTS":
            pass
        elif tc == "TURN ON AIRFAN":
            pass
        elif tc == "TURN OFF AIRFAN":
            pass
        else:
            pass

    def take_photo(self) -> None:
        photo_name = self.database.get_last_photo_name()
        print("taking photo: " + photo_name)

        # TODO
        origin = 'src\\static\\example.png'
        target = f'src\\static\\{photo_name}'
        shutil.copyfile(origin, target)

        print("photo taken")

    @staticmethod
    def take_telemetry() -> Telemetry:
        # TODO
        Controller.humidity = Controller.humidity + 1
        Controller.temperature = Controller.temperature + 1
        Controller.pressure = Controller.pressure + 1

        tm = Telemetry()
        tm.set(humidity=Controller.humidity,
               temperature=Controller.temperature,
               pressure=Controller.pressure,
               luminosity=0.0,
               lamps=Controller.lamps,
               airfan=Controller.airfan,
               heater=0,
               timestamp=datetime.now())

        return tm
