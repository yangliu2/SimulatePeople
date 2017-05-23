import unittest
from src.People import People
from random import Random
from mock import patch


class TestPeople(unittest.TestCase):

    def setUp(self):
        self.people = People()
        random = Random(777)

    def tearDown(self):
        self.people = None

    def test_getMomGenes(self):
        mom = 'momGenes'
        expected = 'momGenes'
        actual = self.people.getMomGenes('momGenes')
        self.assertEqual(expected, actual)

    def test_generateDefault(self):
        self.people.generateDefaults()
        self.assertEqual(0, self.people.age)
        self.assertTrue(self.people.height)
        self.assertTrue(self.people.weight)
        self.assertTrue(self.people.lifeSpan)

    @patch('random.randint') # match the random gen
    def test_randomGender(self, random_call):
        random_call.return_value = 0 # just to match the random
        actual = self.people.randomGender() 
        expected = 'MALE'
        self.assertEqual(expected, actual)
        

if __name__ == '__main__':
    unittest.main()
    # to run specific unit test file
    # python -m unittest discover -s tests -p 'test_People.py'