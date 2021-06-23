import unittest
from src.pub import *
from src.drink import *
from src.customer import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Yawning Portal", 100)

    def test_pub_has_name(self):
        self.assertEqual("The Yawning Portal", self.pub.name)