'''
most optimized way of threading implementation,
concurrent.futures is used which joins the context in the end automatically
so need to use the statement like join 
'''
import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(1)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    '''
    # method_1 -> simplest form
    f1 = executor.submit(do_something,1)
    f2 = executor.submit(do_something,1)
    print(f1.result())
    print(f2.result())
    # method_1 ends here
    '''

    '''
    # method_3 -> list comprehension
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something,sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    # method_3 ends here
    '''
    
    # method_4 -> using map method
    secs = [5,4,3,2,1]
    results = executor.map(do_something,secs)
    for result in results:
        print(result)
    # method_4 ends here
    
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')