from mysql.connector import connection
from mysql.connector import Error
from datetime import datetime


class Database:
    def __init__(self):
        self.username = 'user'
        self.password = 'user'
        self.host_address = '127.0.0.1'
        self.database_name = 'mydb'
        self.data = ''
        self.cnx = connection.MySQLConnection()

        try:
            self.cnx = connection.MySQLConnection(user=self.username,
                                                  password=self.password,
                                                  host=self.host_address,
                                                  database=self.database_name)
            self.data = self.cnx.cursor()
        except Error as err:
            print("Unhandled connection error. Quitting application.")
            quit()

    def __del__(self):
        self.cnx.close()

    def get_telemetry(self):
        query = "SELECT * FROM telemetry " \
                "WHERE TRUE "\
                "ORDER BY gathered_time DESC " \
                "LIMIT 1;"
        self.data.execute(query)
        (gathered_time, humidity, temperature, pressure, luminosity, lamps, airfan, heater) = self.data.fetchone()
        return gathered_time, humidity, temperature, pressure, luminosity, lamps, airfan, heater

    def get_telecommands_history(self):
        query = "SELECT * FROM telecommands"
        self.data.execute(query)

    def get_telemetry_history(self):
        query = "SELECT * FROM telemetry"
        self.data.execute(query)

    def print_telecommands_history(self):
        self.get_telecommands_history()
        for (receive_time, telecommand, executed) in self.data:
            print(f"{receive_time}, {telecommand}, {executed}")

    def print_telemetry_history(self):
        self.get_telemetry_history()
        for (gathered_time, humidity, temperature, pressure, luminosity, lamps, airfan, heater) in self.data:
            print(f"{gathered_time}, {humidity}, {temperature}, {pressure}, {luminosity}, {lamps}, {airfan}, {heater}")

    def add_telecommand(self, tc_string):
        query = self.build_tc_query(tc_string)
        self.add_data(query)

    def add_telemetry(self, tm):
        query = self.build_tm_query(tm)
        self.add_data(query)

    def add_data(self, query):
        self.data.execute(query)
        self.cnx.commit()

    @staticmethod
    def build_tc_query(tc_string):
        default = 'FALSE'  # other value: TRUE
        timestamp = datetime.now()
        query = f'INSERT INTO telecommands(receive_time, telecommand, executed) '\
                f'VALUES (\'{timestamp}\', \'{tc_string}\', {default});'
        return query

    @staticmethod
    def build_tm_query(tm):
        timestamp = datetime.now()
        query = f'INSERT INTO telemetry('\
                f'gathered_time, '\
                f'humidity, temperature, pressure, luminosity, lamps, airfan, heater) '\
                f'VALUES '\
                f'(\'{timestamp}\', '\
                f'{tm.humidity}, {tm.temperature}, {tm.pressure}, ' \
                f'{tm.luminosity}, {tm.lamps}, {tm.airfan}, {tm.heater});'
        return query
