import os

def main():
    print("hello")
    url = "curl http://0.0.0.0:2224/fast"
    count = 50
    x = 0
    while count > x:
        print (x)
        y = os.system("curl http://0.0.0.0:2224/fast")
        print(y)
        x += 1
main()


