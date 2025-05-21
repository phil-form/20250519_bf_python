def fibonacci(n):
    a, b = 0, 1

    fib = []
    while a < n:
        fib.append(a)
        a, b = b, a + b

    return fib