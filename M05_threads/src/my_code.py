import threading
import time

#heavy_computing for test purposes!
#You may modify the function if necessary
if __name__ == "__main__":
    def heavy_computing(idx):
        print('->heavy_computing('+str(idx)+')')
        time.sleep(10)
        print('<-heavy_computing('+str(idx)+')')

def start_threads(f, N):
    threads = []
    for idx in range(N):
        th = threading.Thread(target=f, args=(idx,))
        th.start()
        threads.append(th)
    return threads

def wait_threads(th_list):
    for th in th_list:
        th.join()

#Test software under this if
if __name__ == "__main__":
    N = 5
    th_list=start_threads(heavy_computing, N)
    wait_threads(th_list)

