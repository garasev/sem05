

def bubble(arr, n):
    counter = 0
    counter += 2
    i = 0
    while i < n - 1:
        counter += 3
        j = i + 1
        counter += 1
        while j < n:
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
            j += 1
            counter += 2
        i += 1
        counter += 2
    print(counter)
    return arr


def selection(arr, n):
    counter = 0
    counter += 2
    i = 0
    while i < n - 1:
        counter += 2
        counter += 2
        counter += 1
        counter += 3
        j = i + 1
        mina = arr[i]
        mini = i
        while j < n:
            counter += 2
            if arr[j] < mina:
                mina = arr[j]
                mini = j
            j += 1
        tmp = arr[i]
        arr[i] = arr[mini]
        arr[mini] = tmp
        i += 1
    print(counter)
    return arr


if __name__ == '__main__':
    bubble([1, 2, 3, 4, 5, 6], 6)
    selection([1, 2, 3, 4, 5, 6], 6)