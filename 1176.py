T = int(input())
fibonacci = [0, 1]

for i in range(2, 61):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

for _ in range(T):
    N = int(input())
    print(f"Fib({N}) = {fibonacci[N]}")
