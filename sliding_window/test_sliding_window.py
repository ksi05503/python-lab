import unittest
from sliding_window import SlidingWindow

class TestSlidingWindow(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.window_size = 3
        self.window = SlidingWindow(self.data, self.window_size)

    def test_len(self):
        self.assertEqual(len(self.window), len(self.data) - self.window_size + 1)

    def test_getitem(self):
        self.assertEqual(self.window[1], (2, 3, 4))
        self.assertEqual(self.window[:2], [(1, 2, 3), (2, 3, 4)])

    def test_count(self):
        self.assertEqual(self.window.count((2, 3, 4)), 1)
        self.assertEqual(self.window.count((1, 2, 3)), 1)
        self.assertEqual(self.window.count((1, 2, 5)), 0)

    def test_index(self):
        self.assertEqual(self.window.index((2, 3, 4)), 1)
        self.assertEqual(self.window.index((1, 2, 3)), 0)
        with self.assertRaises(ValueError):
            self.window.index((1, 2, 5))

    def test_iteration(self):
        expected_windows = [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
        for actual, expected in zip(self.window, expected_windows):
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

## .....
## ----------------------------------------------------------------------
## Ran 5 tests in 0.000s
##
## OK