
# code is executed sequentially     => Synchronous execution of code

import time
st = time.perf_counter()

def doJob():
    print("Job started......")
    print("Job rested for 3 secs.....")
    time.sleep(3)

    print("Just got up from sleep ......")

doJob()
doJob()
# doJob()
# doJob()
# doJob()


et = time.perf_counter()
print(f"Completed the execution in {round(et - st, 2)} seconds")
