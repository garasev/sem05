def print_list(n):
    for i in range(n):
        print(i + 1, end=' ')
    print()

count = int(input())

result = []

for _ in range(count):
    n = int(input())
    result.append(n)

for i in range(count):
    print(result[i])
    print_list(result[i])
