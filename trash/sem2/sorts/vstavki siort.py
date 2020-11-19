data=[2,6,1,6,9,34,346,87,42,6,2,8,3,2]
for i in range(len(data)):
    j = i - 1
    key = data[i]
    while data[j] > key and j >= 0:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = key
print(data)