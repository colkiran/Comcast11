
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

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [6, 5, 4, 3, 2, 1]
    results = [executor.submit(doJob, sec) for sec in secs]

    for res in concurrent.futures.as_completed(results):
        print(res.result())

et = time.perf_counter()

print(f"Completed the task in {round(et - st, 2)} seconds.......")