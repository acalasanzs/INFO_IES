from functools import cache

@cache
def fib(n): 
    return n if n <= 1 else fib(n-1)+fib(n-2)

def main():
    for i in range(100):
        print(i,fib(i))
    print("done")

if __name__ == "__main__":
    main()