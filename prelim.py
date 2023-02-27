import unittest

def far(x):
    return (x-32)*5/9

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(far(32),10)

if __name__ == '__main__':
    unittest.main()