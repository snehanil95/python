batches={"PPA":18000,"lb":16500,"python":12345,"angular":2342,"PPA":"ascx"}
print(batches)

for x in batches:
    print(x)
print()
for x in batches:
    print(x,batches[x])
print()
for x in batches:
    print(x,batches.get(x))
print()
keyBat=batches.keys()
print(type(keyBat))

val=batches.values()
print(val)

for i in range(0,len(batches)):
    print(keyBat[i],end="      ")
    print(val[i])-