import unittest
from hello_world.hello import HelloWorld


class TestHelloWorld(unittest.TestCase):
    def test_WHEN_initialized_THEN_class_exists(self):
        hw = HelloWorld("peace")
        assert isinstance(hw, HelloWorld)

    def test_WHEN_hello_imported_THEN_no_errors(self):
        from hello_world import hello
        print(hello)
