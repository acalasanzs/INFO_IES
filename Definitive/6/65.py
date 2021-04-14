def a65():
    res = input("Digues números: ")
    a = res.split()
    total = 0
    for x in a:
        total += int(x)
    return total
print(a65())