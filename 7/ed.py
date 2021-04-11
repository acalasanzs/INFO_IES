""" class some():
    def __init__(self):
        pass
    def getinput(self):
        def cube():
            print("cube")
        pass
#print(dir(some.getinput()))
def print_msg():
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print("msg")

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg()
another() """

""" a = dict((x,0) for x in range(5) for)
print(a) """
""" options = {
    "cub": [("self","None","range(2)","None","[True,False,False,False]"),5],
    "cono": ("self","None","range(3)","None","[True,False,False,False]")
}
a = options["cub"][0]
print(a) """
print("\u001b[44ma")