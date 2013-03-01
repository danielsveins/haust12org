import unittest
import functions
from pics import * 

# n.b. the game states and spaces for each test are found randomly.
# In general most perameters for the tests are determined randomly with a game state generation
# and random number generators in python scripts writen explicitly for that purpose.
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

    def test_moveLegal(self):
        self.assertEqual(functions.moveLegal([E,O,X,O,B,O,X,EX],1,4,'PX'),False)
        self.assertEqual(functions.moveLegal([EO2,X,O,X,B,W,B,E],4,6,'PX'),False)
        self.assertEqual(functions.moveLegal([EO2,W,B,X,O,O,B,EX],4,5,'PO'),False)
        self.assertEqual(functions.moveLegal([EO2,W,B,O,B,O,B,EX3],2,2,'PO'),True)
        self.assertEqual(functions.moveLegal([E,W,O,W,B,X,O,EX],3,7,'PX'),False)
        self.assertEqual(functions.moveLegal([E,W,O,W,B,X,O,EX],3,7,'PO'),False)

    def test_isWon(self):
        self.assertEqual(functions.isWon([EO3,O,B,O,X,O,X,EX],'PX'),False)
        self.assertEqual(functions.isWon([EO2,W,B,W,X,O,O,EX2],'PO'),False)
        self.assertEqual(functions.isWon([EO,W,X,X,X,W,X,E],'PO'),False)
        self.assertEqual(functions.isWon([EO3,W,O,W,O,O,X,EX3],'PX'),False)
        self.assertEqual(functions.isWon([EO2,W,B,W,X,O,B,EX3],'PO'),False)
        self.assertEqual(functions.isWon([E,W,B,W,B,W,B,EX],'PO'),True)
        self.assertEqual(functions.isWon([E,W,B,W,B,W,B,EX],'PX'),False)
        self.assertEqual(functions.isWon([E,W,X,W,O,O,B,EX2],'PO'),False)
        self.assertEqual(functions.isWon([E,W,B,O,O,O,X,EX],'PX'),False)

    def test_Move(self):
        self.assertEqual(functions.Move([EO3,X,X,W,B,X,B,E],2,7,'PO'),[EO3,X,X,W,B,X,B,E])
        self.assertEqual(functions.Move([E,W,O,O,O,O,B,EX3],4,0,'PX'),[E,W,O,O,O,O,B,EX3])
        self.assertEqual(functions.Move([E,W,O,O,O,O,B,EX3],1,6,'PO'),[E,W,O,O,O,W,O,EX3])
        self.assertEqual(functions.Move([EO,X,O,X,O,W,B,EX],4,1,'PX'),[EO,X,O,X,O,W,B,EX])
        self.assertEqual(functions.Move([EO,X,O,X,O,W,B,EX],1,0,'PX'),[EO,W,O,X,O,W,B,EX])

    def test_getLegalMoves(self):
        self.assertEqual(functions.getLegalMoves([E,X,B,O,X,O,O,EX2],2,'PO'),[[7, 7], [6, 5], [1, 2]])
        self.assertEqual(functions.getLegalMoves([EO,O,B,X,O,X,X,E],2,'PO'),[[2, 3], [0, 1], [2, 2]])
        self.assertEqual(functions.getLegalMoves([EO3,W,O,X,X,W,B,E],2,'PX'),[[1, 2], [3, 4], [2, 2]])


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)

