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
        print("Execute before target")
        result=func(*args,**kwargs)
        print("After execution")
        return result
    return wrapper


@simple_decorator
def greet(name):
    print(f"hello, {name}")

greet("Alice")