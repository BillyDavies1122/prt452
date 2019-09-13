import unittest
from assignment1Refactored import *


class TestAssignment1(unittest.TestCase):
    #test the upper range is detected correctly
    def testUpperRange(self):
        num = 0
        self.assertTrue(correctRange(num))
    #test the lower range is detected correctly
    def testLowerRange(self):
        num = 101
        self.assertTrue(correctRange(num))
    #test that a correct answer is identified
    def testCorrectAnswerCheck(self):
        input = 5
        randNum = 5
        total = 0
        self.assertTrue(checkUserAnswer(input,randNum,total))
    #test that an incorrect answer is identified
    def testWrongAnswerCheck(self):
        input = 5
        randNum = 6
        total = 0
        self.assertFalse(checkUserAnswer(input,randNum,total))
    #check that only numeric input is allowed and no empty
    def testcheckForNumeric(self):
        input ="Hello World!"
        self.assertTrue(numericCheck(input))
        input ="$$$ ### 777 asdads"
        self.assertTrue(numericCheck(input))
        input = ""
        self.assertTrue(numericCheck(input))



unittest.main()
