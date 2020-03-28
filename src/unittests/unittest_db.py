import unittest
from src.database import Database
from mysql.connector import Error
from src.telemetry import Telemetry


class TestDBConnection(unittest.TestCase):
    def test_connect(self) -> None:
        try:
            self.database = Database()
        except Error:
            self.fail("DB not connected!!")


class TestDatabaseClass(unittest.TestCase):
    def setUp(self) -> None:
        self.database = Database()

    def tearDown(self) -> None:
        pass

    def test_get_telemetry(self) -> None:
        tm = self.database.get_telemetry()
        self.check_telemetry_values(tm)

    def check_telemetry_values(self, tm) -> None:
        self.assertGreaterEqual(tm.humidity, 0)
        self.assertLessEqual(tm.humidity, 100)

        self.assertGreater(tm.temperature, -50)
        self.assertLess(tm.temperature, 200)

        self.assertGreaterEqual(tm.pressure, 0)
        self.assertLess(tm.pressure, 1100)

        self.assertGreaterEqual(tm.luminosity, 0)

        self.assertGreaterEqual(tm.lamps, 0)
        self.assertLess(tm.lamps, 4)

        self.assertGreaterEqual(tm.airfan, 0)
        self.assertLess(tm.airfan, 3)

        self.assertGreaterEqual(tm.heater, 0)

    def test_build_tc_query(self) -> None:
        self.assertRegex(self.database.build_tc_query('EXAMPLE TC'),
                         'INSERT INTO telecommands.* VALUES.*\'EXAMPLE TC\'.*')

    def test_build_tm_query(self) -> None:
        tm = Telemetry()
        tm.set(humidity=20, temperature=0, pressure=800, luminosity=0.5, lamps=2,
               airfan=3, heater=1, timestamp=self.database.now())
        self.assertRegex(self.database.build_tm_query(tm),
                         'INSERT INTO telemetry.* VALUES.*')


if __name__ == '__main__':
    unittest.main()
