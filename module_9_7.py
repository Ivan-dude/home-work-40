def is_prime(func):
    def wrapper(*args):
        wrapper_ = func(*args)
        for i in range(2, int(wrapper_ / 2) + 1):
            if wrapper_ % i == 0:
                print("Составное")
                return wrapper_
            print("Простое")
            return wrapper_
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
