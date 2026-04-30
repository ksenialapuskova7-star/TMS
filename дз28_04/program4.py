import time


def dec(input_function):
    def output_function(*args):
        start = time.time()
        input_function(*args)
        end = time.time()
        result = end - start
        print(f"Время выполнения функции: {result:.6f}")

    return output_function


@dec
def function_sum(x, y):
    result = x
    for _ in range(y):
        result += 1
    print(f"сумма: {result}")


function_sum(3, 1000000)
