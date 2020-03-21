from db_connection import Database
from telemetry import Telemetry


db = Database()

tm = Telemetry()
tm.humidity = 90
tm.temperature = 23
tm.pressure = 990
tm.luminosity = 0.7
tm.lamps = 1
tm.airfan = 1
tm.heater = 1

db.add_telemetry(tm)
db.add_telecommand('TURN ON HEATER')
db.print_telecommands_history()
db.print_telemetry()
