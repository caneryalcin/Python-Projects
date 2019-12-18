import time

def multipication(numbers):
    result = []
    start = time.time()
    for number in numbers:
        result.append(number**3)
    print("Func. multipication took " + str(time.time() - start))
    return result

def collection(numbers):
    result= []
    start = time.time()
    for number in numbers:
        result.append(number + 2)
    print("Func. collection took " + str(time.time() - start))
    return result


print(multipication(range(10)))
print("")
print(collection(range(10)))
