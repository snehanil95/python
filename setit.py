
data={11,21,51,123,11}

data1={1,'ehfg',90.09,True}

print(data)
print(data1)
data.add(34)
print("data after insersion 34")
print(data)
data.remove(51)
print("data after removal 51")
print(data)
data.discard(11)
print("after discarts",data)
print("output using for")
for no in data:
    print(no,end="  ")
print()


