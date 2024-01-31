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

    def testBad1(self):
      with self.assertRaises(RuntimeError) as context:
        Matrix([[4,6,1,9,'!',12,1,7],
              [1,2,3,4,5,6,7,8],
              [19,0,3,1,10,15,-1,-1]])
              
      self.assertEqual("Matrix is invalid. Please ensure that all elements are numeric (either float or int).", str(context.exception))
