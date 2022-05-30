
import time
import threading
import concurrent.futures

st = time.perf_counter()

def doJob(secs):
    print(f"Starting {threading.current_thread().name}")
    print(f"Sleeping for {secs} second's.....{threading.current_thread().name}")
    time.sleep(secs)
    print(f"Just got up from sleep.....{threading.current_thread().name}")
    print(f"Ending {threading.current_thread().name}")
    return "Hello"

with concurrent.futures.ThreadPoolExecutor() as exector:
    thrd1 = exector.submit(doJob, 3)
    thrd2 = exector.submit(doJob, 3)

    res1 = thrd1.result()
    res2 = thrd2.result()

et = time.perf_counter()

print(res1)
print(res2)

print(f"Completed the task in {round(et - st, 2)} seconds.......")
