sample = [0, -1, 5, -2, 3]
left = 0
right = len(sample) - 1
while left <= right:
    for i in range(left, right, +1):
        if sample[i] > sample[i + 1]:
            sample[i], sample[i + 1] = sample[i + 1], sample[i]
    right -= 1
    print(sample)
    for i in range(right, left, -1):
        if sample[i - 1] > sample[i]:
            sample[i], sample[i - 1] = sample[i - 1], sample[i]
    left += 1
    print(sample)
print(sample)