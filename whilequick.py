def partition(l, h, arr):
    pivot = arr[l]
    i = l+1
    j = h
    while True:
        while (i <= j) and arr[j] >= pivot:
          j -= 1
        while (i <= j) and (arr[i] <= pivot):
          i += 1
        if (i <= j):
          arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quicksort(l, h, arr):
  if (l < h):
    j = partition(l, h, arr)
    quicksort(l, j-1, arr)
    quicksort(j+1, h, arr)
  return arr


arr2 = [1,6,98,4,23,3,7,65,9,2]
print(quicksort(0, len(arr2)-1, arr2))
