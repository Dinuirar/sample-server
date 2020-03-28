from src import app
import unittest


class InterfaceTests(unittest.TestCase):
    HTTP_OK = 200

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self) -> None:
        pass

    def test_index_online(self) -> None:
        result = self.app.get('/index')
        self.assertEqual(result.status_code, self.HTTP_OK)

    def test_telecommands_online(self) -> None:
        result = self.app.get('/telecommands')
        self.assertEqual(result.status_code, self.HTTP_OK)

    def test_telemetry_online(self) -> None:
        result = self.app.get('/telemetry')
        self.assertEqual(result.status_code, self.HTTP_OK)

    def test_photo_online(self) -> None:
        result = self.app.get('/photo')
        self.assertEqual(result.status_code, self.HTTP_OK)


if __name__ == '__main__':
    unittest.main()
