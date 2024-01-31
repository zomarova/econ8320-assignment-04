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

    def test10x10(self): 
      result = '  [ 1 1 1 1 1 1 1 1 1 1 ]\n  [ 1 1 1 1 1 1 1 1 1 1 ]\n  [ 1 1 1 1 1 1 1 1 1 1 ]\n  [ 1 1 1 1 1 1 1 1 1 1 ]\n  [ 1 1 1 1 1 1 1 1 1 1 ]\n  [ 1 1 1 1 1 1 1 1 1 1 ]\n  [ 1 1 1 1 1 1 1 1 1 1 ]\n  [ 1 1 1 1 1 1 1 1 1 1 ]\n  [ 1 1 1 1 1 1 1 1 1 1 ]\n  [ 1 1 1 1 1 1 1 1 1 1 ]\n\n'

      mat1 = Matrix(dim=(10,10))

      self.assertEqual(str(mat1), result, "Your Matrix class does not correctly generate\na string representation of a 10x10 matrix\n from a 'dim' argument")
