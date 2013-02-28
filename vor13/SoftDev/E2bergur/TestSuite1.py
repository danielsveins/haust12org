import unittest
import functions
from pics import * 

# n.b. the game states and spaces for each test are found randomly.

class testFunctions(unittest.TestCase):
    def test_adjecents(self):
        self.assertEqual(functions.adjecents([EO3, O, X, W, O, X, O,E],2),False)
        self.assertEqual(functions.adjecents([E,W,X,W,X,W,X,EX2],6),True)
        self.assertEqual(functions.adjecents([EO,O,B,O,O,X,O,EX2],6),False)
        self.assertEqual(functions.adjecents([EO2,O,X,X,B,W,B,EX],1),True)
        self.assertEqual(functions.adjecents([EO,X,X,W,B,X,X,E],5),True)
        self.assertEqual(functions.adjecents([EO2,X,X,O,O,X,X,EX2],5),True)
        self.assertEqual(functions.adjecents([EO2,O,B,X,B,O,X,E],6),False)
        self.assertEqual(functions.adjecents([EO,O,B,W,X,X,O,EX],4),True)

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)

