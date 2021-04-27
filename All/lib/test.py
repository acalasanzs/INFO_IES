load = ["John","Mark","Zoe"]
dic = dict.fromkeys(range(len(load)),"")
for x in dic:
    dic[x] = load[x]
print(dic)