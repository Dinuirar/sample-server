from mysql.connector import connection
from mysql.connector import Error
from src.telemetry import Telemetry
from datetime import datetime


class Database:
    def __init__(self):
        self.username = 'user'
        self.password = 'user'
        self.host_address = '127.0.0.1'
        self.database_name = 'mydb'
        self.cnx = connection.MySQLConnection()
        self.cursor = None

        try:
            self.connect()
        except Error as err:
            print("Unhandled connection error.")
            raise Error

    def __del__(self):
        self.cnx.close()

    def connect(self) -> None:
        self.cnx = connection.MySQLConnection(user=self.username,
                                              password=self.password,
                                              host=self.host_address,
                                              database=self.database_name)
        self.cursor = self.cnx.cursor()

    @staticmethod
    def build_select_top_query(column: str, table: str) -> str:
        return f"SELECT {column} from {table} ORDER BY {column} DESC LIMIT 1;"

    def get_next_id(self, column: str, table: str) -> int:
        query = self.build_select_top_query(column, table)
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        while row is None:
            return 0
        return row[0] + 1

    def get_next_tm_id(self) -> int:
        return self.get_next_id("tm_id", "telemetry")

    def get_next_tc_id(self) -> int:
        return self.get_next_id("tc_id", "telecommands")

    def get_next_err_id(self) -> int:
        return self.get_next_id("error_id", "error_log")

    def get_telemetry(self) -> Telemetry:
        query = "SELECT * FROM telemetry " \
                "WHERE TRUE "\
                "ORDER BY gathered_time DESC " \
                "LIMIT 1;"
        self.cursor.execute(query)
        (gathered_time, humidity, temperature, pressure, luminosity, lamps, airfan, heater, tm_id) = \
            self.cursor.fetchone()
        tm = Telemetry()
        tm.set(humidity=humidity,
               temperature=temperature,
               pressure=pressure,
               luminosity=luminosity,
               lamps=lamps,
               airfan=airfan,
               heater=heater,
               timestamp=gathered_time)
        return tm

    def add_telecommand(self, tc_string: str) -> None:
        query = self.build_tc_query(tc_string)
        self.add_data(query)

    def add_telemetry(self, tm: Telemetry) -> None:
        query = self.build_tm_query(tm)
        self.add_data(query)

    def add_error(self, error: str) -> None:
        query = self.build_error_query(error)
        self.add_data(query)

    def add_data(self, query: str) -> None:
        self.cursor.execute(query)
        self.cnx.commit()

    def build_tc_query(self, tc_string) -> str:
        was_executed = 'FALSE'
        timestamp = datetime.now()
        tc_id = self.get_next_tc_id()
        query = f'INSERT INTO telecommands(receive_time, telecommand, executed, tc_id) '\
                f'VALUES (\'{timestamp}\', \'{tc_string}\', {was_executed}, {tc_id});'
        return query

    def build_tm_query(self, tm) -> str:
        timestamp = datetime.now()
        tm_id = self.get_next_tm_id()
        query = f'INSERT INTO telemetry('\
                f'gathered_time, '\
                f'humidity, temperature, pressure, luminosity, lamps, airfan, heater, tm_id) '\
                f'VALUES '\
                f'(\'{timestamp}\', '\
                f'{tm.humidity}, {tm.temperature}, {tm.pressure}, ' \
                f'{tm.luminosity}, {tm.lamps}, {tm.airfan}, {tm.heater}, {tm_id});'
        return query

    def build_error_query(self, error: str) -> str:
        timestamp = datetime.now()
        error_id = self.get_next_err_id()
        query = f'INSERT INTO error_log'\
                f'(timestamp, message, error_id) '\
                f'VALUES '\
                f'(\'{timestamp}\', \'{error}\', {error_id});'
        return query

    def get_next_unexecuted_tc(self) -> (str, int):
        query = "SELECT tc_id, telecommand " \
                "FROM telecommands " \
                "WHERE executed = FALSE " \
                "ORDER BY tc_id ASC LIMIT 1"
        self.cursor.execute(query)
        try:
            (tc_id, unexecuted_tc) = self.cursor.fetchone()
            return unexecuted_tc, tc_id
        except TypeError:
            return 'empty', None

    def set_tc_as_executed(self, tc_id) -> None:
        query = f"UPDATE telecommands " \
                f"SET executed=TRUE " \
                f"WHERE tc_id={tc_id};"
        self.cursor.execute(query)

    def get_last_photo_name(self) -> str:
        query = "SELECT tc_id " \
                "FROM telecommands " \
                "WHERE telecommand = 'TAKE PHOTO' " \
                "ORDER BY tc_id DESC LIMIT 1"
        self.cursor.execute(query)

        data = self.cursor.fetchone()
        if data is not None:
            photo_id = data[0]
        else:
            photo_id = 0
        photo_name = "sample_photo" + str(photo_id) + ".png"

        return photo_name
