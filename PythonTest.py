import concurrent.futures
import time

start = time.perf_counter()
def todo(seconds):
    print(f'sleeping for {seconds} seconds')
    time.sleep(seconds)
    return f'sleep done...in {seconds} seconds'

with concurrent.futures.ThreadPoolExecutor() as ex:
    secs = [5,4,3,2,1]
    results = [ex.submit(todo, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

end = time.perf_counter()
time_gap = round(end-start, 2)

print(f'Finished in {time_gap} seconds.')