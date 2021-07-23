A = int(input("Enter your number: "))

import time

for i in range(100):
    print(A + i)
    if i < 99:
        time.sleep(0.25)