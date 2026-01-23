import threading
import concurrent.futures as cf
import time

_counter_lock = threading.Lock()
_counter = 0


def external_function():
    global _counter
    with _counter_lock:
        _counter += 1

def external_count():
    global _counter
    with _counter_lock:
        return _counter

#Sample function for test purposes
def computing5s(thr_id):
    time.sleep(5)
    external_function()
            
    return thr_id, thr_id*thr_id

def init_values(f):
    f_values={}
    N = 50

    executor = cf.ThreadPoolExecutor(max_workers=50)

    futures = [executor.submit(f, i) for i in range(N)]
    for future in cf.as_completed(futures):
        idx, val = future.result()
        f_values[idx] = val
    return f_values

#Test software under this if        
if __name__ == "__main__":
    start = time.time()
    ret = init_values(computing5s)
    end = time.time()
    print(f"Execution time: {end-start:.2f} s")
    print(ret)
    print("function called:", external_count(), "times")