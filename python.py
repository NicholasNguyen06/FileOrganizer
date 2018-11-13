import os
import datetime

def main():
    print('Hello world')
    print('The answer to 4 x 2 = ' + str(multiplication(4,2)))
    print('The answer to 4 ^ 2 = ' + str(powerOf(2,4)))
    for filename in os.listdir(os.getcwd()):
        x = os.stat(filename).st_ctime
        print(datetime.datetime.fromtimestamp(x))

def multiplication(x, y):
    return x * y;

def powerOf(x,y):
    return x**y;

main()
