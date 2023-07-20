# Displaying TimeStamp After every Second

import time as tm

while True:
    start = tm.localtime()
    print(start)
    tm.sleep(1)
    time_input = input("Press Enter to Stop.")
