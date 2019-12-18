import time
def calculate_time(func):
    def wrapper(numbers):

        start = time.time()
        result = func(numbers)
        end = time.time()
        print(func.__name__+ " took " + str(end-start))
        return result

    return wrapper


@calculate_time
def multipication(numbers):

    result = []
    for number in numbers:
        result.append(number**3)

    return result

@calculate_time
def collection(numbers):

    result= []
    for number in numbers:
        result.append(number + 2)

    return result

print(multipication(range(10)))
print("")
print(collection(range(10)))
