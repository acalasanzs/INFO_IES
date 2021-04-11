def some():
    val = ["first","second"]
    def first():
        print("msg")
    def second():
        print("second")
    fu = eval(val[1])
    return fu

""" foo = some()
foo() """
class cs:
    def __init__(self):
        self.a = "D"
        self.get()
    def get(self):
        def a():
            print("a")
        a()
fi = cs()