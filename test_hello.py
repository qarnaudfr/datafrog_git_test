import unittest
from hello import greet


class TestHello(unittest.TestCase):

    def test_hello(self):
        people = [
            'colin',
            'pierre'
        ]
        printout = greet(people)
        self.assertListEqual(['hello colin', 'hello pierre'], printout)
