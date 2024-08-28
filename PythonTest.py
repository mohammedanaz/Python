import concurrent.futures
import time

start = time.perf_counter()
def todo(seconds):
    print(f'sleeping for {seconds} seconds')
    time.sleep(seconds)
    return 'sleep done'

with concurrent.futures.ThreadPoolExecutor() as ex:
    results = [ex.submit(todo, 1) for _ in range(10)]
    for f in results:
        print(f.result())

end = time.perf_counter()
time_gap = round(end-start, 2)

print(f'Finished in {time_gap} seconds.')