from sympy import isprime

tests = int(input())
for i in range(tests):
    n = int(input())
    target = n * 2
    for j in range(2, target // 2 + 2):
        if isprime(j) and isprime(target- j):
            print(j, target-j)
            break
