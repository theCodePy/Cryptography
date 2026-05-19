import json

p = 37
g = 2

dic = {}
for a in range(2, 37):
    for k in range(2,37):
        mod = (((g**a)%p)**k)%p
        if mod not in dic:
            dic[mod] = []
        dic[mod].append((a,k))

# json.dumps(dic, indent=4)
print(dic)