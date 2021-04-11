import time
class timing:
    def Timer(timer,dig = 2):
        now = time.time()
        future = now + float(timer)
        while time.time() < future:
            if dig < 1:
                print(int(future - time.time()),end="s\r")
            else:
                print(round(future - time.time(),int(dig)),end="s\r")
        else:
            print("Time Out!")
    def Counter(dig = 2):
        global stop
        stop = False
        n = time.time()
        while True:
            print(round(time.time()-n,dig),end="s\r")
            if stop:
                break
    def stop():
        stop = True
        print("stop")
a = timing
a.Counter()
a.stop()