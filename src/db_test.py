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
db.print_telemetry_history()

(gathered_time, humidity, temperature, pressure, luminosity, lamps, airfan, heater) = db.get_telemetry()
print(f'last telemetry packet gathered on {gathered_time}\n'
      f'humidity: {humidity}, temperature: {temperature}, pressure: {pressure}\n'
      f'luminosity: {luminosity}, lamps: {lamps}, airfan: {airfan}\n'
      f'heater: {heater}')
