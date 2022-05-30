
import time
import threading

st = time.perf_counter()


def doJob():
    print(f"Starting {threading.current_thread().name}........")
    print(f"Sleeping for 3 seconds...........{threading.current_thread().name}")
    time.sleep(3)
    print(f"Just got up from sleep..........{threading.current_thread().name}")
    print(f"Completing the task {threading.current_thread().name}")


thrd1 = threading.Thread(target=doJob, name="thrd01")
thrd2 = threading.Thread(target=doJob, name="thrd02")

thrd1.start()
thrd2.start()

thrd1.join()
thrd2.join()

et = time.perf_counter()
print(f"Completed the task in {round(et - st, 2)} seconds")

