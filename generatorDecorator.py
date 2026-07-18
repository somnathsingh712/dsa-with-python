import sys
def traditional(n):
    result = []      # Use a list instead of a dictionary
    for i in range(n):
        result.append(i)
    return result

print(traditional(6))


def generator(n):
    for i in range(n):
        yield i

gen = generator(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



huge_list=[i**2 for i in range(100_000_00000000)]
huge_gen=(i**2 for i in range(10_000_000))

print(f"size of list: {sys.getsized(huge_list)/(1024**2):.2f}Mb")
print(f"zie of gen: {sys.getsizeof(huge_gen)} Bytes")


def simple_decorator(func):
    def wrapper(*args,**kwargs):
        print("excute before target")
        result=func(*args,**kwargs)
        print("after execution")
        return result
    return wrapper

@simple_decorator
def greet(name):
    print(f"hello, {name}")


from functools import wraps
import time
import random

def repeat(max_attempt,delay):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            attempts=0
            while attempts<max_attempt:
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    attempts+=1
                    print(f"attempt {attempts}/{max_attempt} failed:{e}")
                    if attempts>= max_attempt:
                        print("max attempts reached")
                        raise e
                    print(f"retrying in {delay}seconds...")
                    time.sleep(delay)
            
        return wrapper
    return decorator_repeat

@repeat(max_attempt=3,delay=2)
def slow_network_call():
    import random
    print("making network call...")
    if random.random()<0.7:
        raise ConnectionError("Network Error")
    return "success!"

slow_network_call()

if __name__ == "__main__":
    try:
        result = slow_network_call()
        print(f"Final Result: {result}")
    except ConnectionError:
        print("The program gracefully handled the final failure.")