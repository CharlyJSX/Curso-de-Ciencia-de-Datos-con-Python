import json

# some JSON:
x =  '{ "name":"John", "age": "30", "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:

print(type(x))
print(type(y))

for z in y:
    print(z , " " , y[z])

print(x)
print(y)