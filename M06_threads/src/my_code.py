import threading
import concurrent.futures as cf
import time

#heavy_computing for test purposes!
#You may modify the function if necessary
if __name__ == "__main__":
    def heavy_computing(idx):
        print('->heavy_computing('+str(idx)+')')
        time.sleep(10)
        print('<-heavy_computing('+str(idx)+')')
        return idx, idx*idx

def start_threads(f, N):
    executor = cf.ThreadPoolExecutor(max_workers=N)
    futures = []
    
    for idx in range(N):
        futures.append(executor.submit(f, idx))
    return futures

def wait_threads(th_list):

    results = []

    for future in cf.as_completed(th_list):
        idx, value = future.result()
        results.append(value)  
    
    results.sort()  
    return results

#Test software under this if        
if __name__ == "__main__":
    N=10

    #print('None started')
    th_list=start_threads(heavy_computing, N)
    #print(th_list)
    #print('Wait...')
    ret=wait_threads(th_list)
    print('All futures completed')
    print(ret)
