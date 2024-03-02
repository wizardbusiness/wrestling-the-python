def quicksort(array, start, end):
  if start > end: 
    return
  
  partition_index = partition(array, start, end)

  quicksort(array, start, partition_index - 1)
  quicksort(array, partition_index + 1, end)

  return

def partition(array, start, end):
  pivot = array[end]
  partition_index = start
  
  for i in range(start, end):
    if array[i] < pivot:
      array[i], array[partition_index] = array[partition_index], array[i] 
      partition_index += 1

  array[partition_index], array[end] = array[end], array[partition_index]

  return partition_index

unsorted = [1, 3, 0, 6, 20, 2]

quicksort(unsorted, 0, len(unsorted) - 1)

print(unsorted)