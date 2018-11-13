import os
import datetime

def main():
    for filename in os.listdir(os.getcwd()):
        x = os.stat(filename).st_ctime
        print(datetime.datetime.fromtimestamp(x))

main()
