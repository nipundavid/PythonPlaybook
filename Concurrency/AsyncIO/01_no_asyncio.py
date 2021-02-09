'''
There is no asyncio and,
the time taken to make 3 calls of count()
is took ~3 seconds
'''
import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(3):
        count()


start = time.perf_counter()
main()
elapsed = time.perf_counter() - start
print(f"executed in {elapsed:0.2f} seconds.")