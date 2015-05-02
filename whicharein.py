import unittest as test

a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']


class RunTest(test.TestCase):
    def test_cases(self):
        self.assertEquals(in_array(a1, a2), r)


if __name__ == '__main__':
    def in_array(array1, array2):
        mylist = []

        for x in array1:
            for y in array2:
                if x in y:
                    mylist.append(x)
        finalList = list(set(mylist))
        return sorted(finalList)

    test.main()