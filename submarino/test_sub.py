import unittest
from submarino import Submarino


class submarino_test(unittest.TestCase):

    def setUp(self):
        self.submarino1 = Submarino()
        self.submarino2 = Submarino()

    def test1(self):
        command = 'LMRDDMMUU'
        expected = [-1, 2, 0, 'NORTE']
        result = self.submarino1.run(command)
        self.assertEqual(result, expected)


    def test2(self):
        command = 'RMMLMMMDDLL'
        expected = [2, 3, -2, 'SUL']
        result = self.submarino2.run(command)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()


