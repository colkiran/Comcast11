import stat
import time
import threading

st = time.perf_counter()

def doJob(secs, tname):
    print(f"Starting {tname}")
    print(f"Sleeping for {secs} second's.....{tname}")
    time.sleep(secs)
    print(f"Just got up from sleep.....{tname}")
    print(f"Ending {tname}")

threads = []

for i in range(100):
    t = threading.Thread(target=doJob, name="thrd"+str(i), args=[3, "thrd"+str(i)])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

et = time.perf_counter()
print(f"Completed the task in {round(et - st, 2)} seconds.......")

