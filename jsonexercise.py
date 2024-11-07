import json

personDict = {"name": "John", "age": 38}
print('Python object:', personDict)

# Convert to JSON. dumps() konventerer et Python objekt til en JSON-streng
personJson = json.dumps(personDict)
print('JSON objekt:', personJson)

# Convert to Python dict. loads() konventerer en JSON-streng til et Python objekt
personDictv2 = json.loads(personJson)
print('Python object:', personDictv2)
print('Printer age property:', personDictv2["age"])

# Opretter en liste med dictionaries
jsonString = '[{"name": "John", "age": 38}, {"name": "Jane", "age": 28}]'

ListPersons = json.loads(jsonString)
print('Python name property:', ListPersons[1]["name"])


# testString = “{“name”: “tes”t”name”,”age”:2}”
# print(testString)