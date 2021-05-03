def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                arr[j], arr[min] = arr[min], arr[j]
    return arr


x = [6, 3, 0, 5, 2, 1, 4]
print(selection_sort(x))