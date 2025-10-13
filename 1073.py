n = int(input())
count = 0
if 5 < n < 2000:
    for i in range(2, n + 2, 2):
        i = i ** 2
        count = count + 2
        print(f'{count}^2 = {i}')