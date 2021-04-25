def make_arr(a="abcdefghijklmnopqrstuvwxyz"):
    var = []
    for x in a:
        var.append(x)
    return var
var = make_arr()
for i,x in enumerate(var):
    if i < len(var)-1:
        j = var[i+1]
    else:
        j = x
    print(x,j) 