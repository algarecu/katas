'''
Categorize New Member
'''
import unittest as test


class RunTest(test.TestCase):
    def test_cases(self):
        self.assertEquals(openOrSenior([[45, 12], [55, 21], [19, -2], [104, 20]]), ['Open', 'Senior', 'Open', 'Senior'])
        self.assertEquals(openOrSenior([[16, 23], [73, 1], [56, 20], [1, -1]]), ['Open', 'Open', 'Senior', 'Open'])


if __name__ == '__main__':

    def openOrSenior(data):
        mylist = list()
        for i in data:
            if i[0] >= 55 and i[1] > 7:
                mylist.append('Senior')
            else:
                mylist.append('Open')
        return mylist

    test.main()