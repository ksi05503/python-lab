from permutation_generator import PermutationGenerator 
import itertools
import unittest

class TestPermutationGenerator(unittest.TestCase):
    def test_permutations(self):
        p = PermutationGenerator('ABC')
        expected = set(sorted(['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']))
        actual = set(sorted(p.get_table().keys()))
        self.assertEqual(expected, actual)

    def test_permutations_with_duplicates(self):
        p = PermutationGenerator('AAB')
        expected = set(sorted(['AAB', 'ABA', 'BAA']))
        actual = set(sorted(p.get_table().keys()))
        self.assertEqual(expected, actual)

    def test_permutations_with_repeating_characters(self):
        p = PermutationGenerator('ABB')
        expected = set(sorted(['ABB', 'BAB', 'BBA']))
        actual = set(sorted(p.get_table().keys()))
        self.assertEqual(expected, actual)

    def test_permutations_with_empty_string(self):
        p = PermutationGenerator('')
        expected = set([''])
        actual = set(p.get_table().keys())
        self.assertEqual(expected, actual)

    def test_permutations_with_single_character(self):
        p = PermutationGenerator('A')
        expected = set(['A'])
        actual = set(p.get_table().keys())
        self.assertEqual(expected, actual)

    def test_permutations_with_long_string(self):
        p = PermutationGenerator('ABCDE')
        expected = set(sorted(''.join(x) for x in itertools.permutations('ABCDE')))
        actual = set(sorted(p.get_table().keys()))
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()


## ......
## ----------------------------------------------------------------------
## Ran 6 tests in 0.000s
##
## OK