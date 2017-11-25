# coding=utf8
import json

data1 = 3
data2 = [
    { "name":"John", "age":31, "city":"New York",
      'lobby':['swim','shoot','race in street'] },
    { "name":"Mary", "age":21, "city":"New York" },
    { "name":"Tom", "age":31, "city":"Los Angels" },
]

jstr1 = json.dumps(data1)
jstr2 = json.dumps(data2)
print (jstr1)
print (jstr2)

obj1 = json.loads(jstr1)
obj2 = json.loads(jstr2)
print obj1
print obj2