import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-matrix" in j:
            exec("".join(i['source']))


class testCases(unittest.TestCase):

    def test3x8(self): 
      result = '  [ 4 6 1 9 10 12 1 7 ]\n  [ 1 2 3 4 5 6 7 8 ]\n  [ 19 0 3 1 10 15 -1 -1 ]\n\n'

      matrixList = [[4,6,1,9,10,12,1,7],
			  [1,2,3,4,5,6,7,8],
			  [19,0,3,1,10,15,-1,-1]]

      mat2 = Matrix(matrixList)

      self.assertEqual(str(mat2), result, "Your Matrix class does not correctly generate\na string representation of a 3x8 matrix\n from a list of lists")
