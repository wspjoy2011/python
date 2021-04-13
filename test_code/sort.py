import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


lst = [random.randint(1, 255) * x for x in range(20)]
insertion_sort(lst)


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]



lst = [random.randint(1, 255) * x for x in range(20)]
selection_sort(lst)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


lst = [random.randint(1, 255) * x for x in range(20)]
bubble_sort(lst)


def count_sort(lst):
    result = []
    count_lst = [0] * (max(lst) + 1)
    for now in lst:
        count_lst[now] += 1
    for num in range(len(count_lst)):
        for i in range(count_lst[num]):
            result.append(num)
    return result


lst = [random.randint(1, 255) * x for x in range(20)]
print(count_sort(lst))
