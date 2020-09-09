# 09/09/2020 Kristin Kim, SSW 567 HW 01: Testing triangle classification

import unittest

def classifyTriangle(a,b,c):
    if a+b<c or a+c<b or c+b<a:
        return "NotATriangle"
    elif a==b==c:
        return "Equilateral"
    elif a==b or a==c or b==c:
        return "Isosceles"
    elif a^2+b^2==c^2:
        return "Right"
    else:
        return "Scalene"

def runClassifyTriangle(a,b,c):
    #print the outcome #sep=""takes a default spacing between ,
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")

#print(runClassifyTriangle(10,10,12))

#UNITTEST
class TestTriangles(unittest.TestCase):
    def setUp(self):
        pass

    def testNotATriangle(self):
        #self.assertEqual(a,b,msg=None)
        self.assertEqual(classifyTriangle(5, 6, 13), 'NotATriangle')
        self.assertNotEqual(classifyTriangle(5, 6, 9), 'NotATriangle')
        self.assertEqual(classifyTriangle(3, 4, 20), 'NotATriangle')
    def testEquilateral(self):
        self.assertEqual(classifyTriangle(4,4,4),'Equilateral')
        self.assertNotEqual(classifyTriangle(5, 6, 13), 'Equilateral')
        self.assertNotEqual(classifyTriangle(4,5,4),'Equilateral')
        self.assertNotEqual(classifyTriangle(4,5,13),'Equilateral')

    def testIsosceles(self):
        self.assertEqual(classifyTriangle(4, 5, 4), 'Isosceles')
        self.assertEqual(classifyTriangle(4, 6, 4), 'Isosceles')
        self.assertNotEqual(classifyTriangle(3, 5, 4), 'Isosceles')
        self.assertNotEqual(classifyTriangle(9, 5, 4), 'Isosceles')

    def testRight(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')
        self.assertNotEqual(classifyTriangle(3, 7, 5), 'Right')

    def testScalene(self):
        self.assertEqual(classifyTriangle(3, 4, 2), 'Scalene')
        self.assertEqual(classifyTriangle(3, 8 ,7), 'Scalene')
        self.assertEqual(classifyTriangle(6, 7, 8), 'Scalene')

if __name__=='__main__':
    unittest.main()
