print("how to use list data type")

values = [12,21,23,43]
print(values)

print(type(values))

print(len(values))

print(values[0])
print(values[1])
print(values[2])
print(values[3])

values.append(23)

print(values)

values.remove(21)
print(values)

values.append(43)
print(values)

print(type(values[0]))

values.append(21.32)
print(values)

values.insert(3,11)
print(values)

values.insert(15,23)
print(len(values))
print(values)