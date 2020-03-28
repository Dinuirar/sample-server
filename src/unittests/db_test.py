from src.database import Database
from src.telemetry import Telemetry


db = Database()

tm = Telemetry()
tm.set(humidity=90,
       temperature=23,
       pressure=999,
       luminosity=0.9,
       lamps=2,
       airfan=0,
       heater=1,
       timestamp=0)

db.add_telemetry(tm)
db.add_telecommand('TURN ON HEATER')
db.print_telecommands_history()
db.print_telemetry_history()
