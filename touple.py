data=(11,21,51,123)
#ata=(11,21,51,123)
#data=(11,21,51,123)
print(data)
print(data[2])
print("output using for")
for no in data:
    print(no,end="  ")
print()

print("output using for with index")
for i in range(0,len(data)):
    print(data[i],end="  ")
print()

print("outpit using while with index")
i=0
while(i<len(data)):
    print(data[i],end="     ")
    i=i+1
print()