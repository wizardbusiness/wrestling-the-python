def binary_search(array, start, end, target):
  if start > end: 
    return -1

  mid = (start + end) // 2

  if target < array[mid]:
    binary_search(array, start, mid - 1, target)
  elif target > array[mid]:
    binary_search(array, mid + 1, end, target)
  elif target == array[mid]:
    print(mid)
    return
  
sorted = [1, 3, 5, 6, 8, 10, 14, 20]

binary_search(sorted, 0, len(sorted), 14)