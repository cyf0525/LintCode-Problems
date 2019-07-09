import json

"""
studentA = {"id": 1, "name": "jzj"}
studentB = {"id": 2, "name": "dyf"}
students = [studentA, studentB]
print json.dumps(students)
"""

"""
str = "[{\"id\": 1, \"name\": \"jzj\"}, {\"id\": 2, \"name\": \"dyf\"}]"
arr = json.loads(str)
for item in arr:
    print item["id"]
    print item["name"]
"""

str = "{\"123\": {\"456\": {\"score\": \"fjweo\"}, \"789\": {\"score\": 834}},\"score\": 780,\"jfs\":{\"score\":333}}"
arr = json.loads(str)


res=[]

def check(jsonStr):
   for item, value in jsonStr.items():
       if item == "score":
           if value < 60 or isinstance(value,unicode):
               res.append(value)
       elif isinstance(value,dict):
          check(value)

   if len(res):
       return False
   else:
       return True


print check(arr)
