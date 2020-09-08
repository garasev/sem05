import unittest
from main import calc_dist_matrix
from main import calc_dist_recur
from main import calc_dist_recur_matrix
from main import calc_dist_damerau


class TestDist(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(self.function('', ''), 0)
        self.assertEqual(self.function('a', ''), 1)
        self.assertEqual(self.function('', 'a'), 1)

    def test_different(self):
        self.assertEqual(self.function('a', 'a'), 0)
        self.assertEqual(self.function('ab', 'a'), 1)
        self.assertEqual(self.function('a', 'ab'), 1)
        self.assertEqual(self.function('ab', 'aс'), 1)0


class TestLevMatrix(TestDist):
    def setUp(self):
        self.function = calc_dist_matrix

    def test_spec(self):
        self.assertEqual(self.function('ab', 'ba'), 2)
        self.assertEqual(self.function('abc', 'cba'), 2)


class TestLevRec(TestDist):
    def setUp(self):
        self.function = calc_dist_recur

    def test_spec(self):
        self.assertEqual(self.function('ab', 'ba'), 2)
        self.assertEqual(self.function('abc', 'cba'), 2)


class TestLevMatrixRec(TestDist):
    def setUp(self):
        self.function = calc_dist_recur_matrix

    def test_spec(self):
        self.assertEqual(self.function('ab', 'ba'), 2)
        self.assertEqual(self.function('abc', 'cba'), 2)


class TestDamLevMatrix(TestDist):
    def setUp(self):
        self.function = calc_dist_damerau

    def test_spec(self):
        self.assertEqual(self.function('ab', 'ba'), 1)
        self.assertEqual(self.function('abc', 'cba'), 2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLevMatrix)
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLevRec))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLevMatrixRec))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDamLevMatrix))

    unittest.TextTestRunner().run(suite)
