'''
Simple threading implemented,
the time taken to make 10 calls of do_something()
is took around 2 seconds
'''
import time
import threading

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(1)
    print(f'Done Sleeping...{seconds}')


threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1])
    t.start()
    threads.append(t)


for t in threads:
    t.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')