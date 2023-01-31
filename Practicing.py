# Practice for yesterday's question
lst = [1,2,3,4,5,6,7,8,9]
l = -1
o = []
for i in range(len(lst)):
    o.append(lst[l])
    l = l - 1
print(o)