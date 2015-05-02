import unittest as test

class RunTest(test.TestCase):
    def test_cases(self):
        self.assertEquals(createDict(['a', 'b', 'c', 'd'], [1, 2, 3]), {'a': 1, 'b': 2, 'c': 3, 'd': None})
        self.assertEquals(createDict(['a', 'b', 'c'], [1, 2, 3, 4]), {'a': 1, 'b': 2, 'c': 3})

if __name__ == '__main__':

    def createDict(keys, values):
        """
        Dictionary from two lists
        """
        d = {}

        for idx, v in enumerate(keys):
            if idx < len(values):
                d[v] = values[idx]
            else:
                d[v] = None
        return d

    test.main()