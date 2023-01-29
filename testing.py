import unittest
import main
class Testmain(unittest.TestCase):
    def whatever(self):
        param=20
        res=main.add(param)
        self.assertEqual(res,25)
       
if __name__=='__main__':
   (unittest.main())