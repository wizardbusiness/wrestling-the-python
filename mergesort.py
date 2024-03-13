
unsorted = [1, 3, 2, 9, 0, -1, -2]
def mergesort(array):
  if len(array) <= 1:
    return array
  
  mid = len(array) // 2
  l = mergesort(array[:mid])
  r = mergesort(array[mid:])

  return merge(l, r)

def merge(l, r):
  sorted = []
  while(len(l) and len(r)):
    if l[0] < r[0]:
      sorted.append(l.pop(0))
    else:
      sorted.append(r.pop(0))
  print(sorted)
  return [*sorted, *l, *r]
  

print(mergesort(unsorted))
