from unittest import TestCase, main
from src import app


class InterfaceTests(TestCase):
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
        result = self.app.post('/post_telecommand')
        self.assertEqual(result.status_code, self.HTTP_OK)

    def test_telemetry_online(self) -> None:
        result = self.app.get('/get_telemetry')
        self.assertEqual(result.status_code, self.HTTP_OK)

    def test_photo_online(self) -> None:
        result = self.app.get('/photo')
        self.assertEqual(result.status_code, self.HTTP_OK)

    def test_error_log_online(self) -> None:
        result = self.app.get('/error_log')
        self.assertEqual(result.status_code, self.HTTP_OK)


if __name__ == '__main__':
    main()
