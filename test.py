import unittest
import main
class Testmain(unittest.TestCase):
    def asub(self):
        param="a"
        res=main.add(param)
        self.assertEqual(res,25)
        print(res)
print(unittest.main())