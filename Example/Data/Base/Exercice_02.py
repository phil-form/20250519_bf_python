i, j = 0, 1
fib = []

while i < 89:
    #i, j = j, i + j
    temp = i
    i = j
    j = temp + j
    fib.append(i)

print(fib)
