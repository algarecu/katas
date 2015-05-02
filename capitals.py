import unittest as test

if __name__ == '__main__':
    class RunTest(test.TestCase):
        def test_cases(self):
            self.assertEquals(capitals('CodEWaRs'), [0, 3, 4, 6])

    def capitals(word):
        mylist = []
        for k, v in enumerate(word):
            if v.isupper():
                mylist.append(k)
        return mylist

    test.main()
