from unittest import TestCase, main
from src.controller import Controller


class TestController(TestCase):
    def setUp(self) -> None:
        self.controller = Controller()

    def tearDown(self) -> None:
        pass

    def test_function(self) -> None:
        self.assertTrue(True)


if __name__ == '__main__':
    main()
