def twosum(array, target):
  hash = {}
  for i in range(len(array)):
    if target - array[i] in hash: return [hash[target - array[i]], i]
    hash[array[i]] = i
  return False


print(twosum([12, 3], 15))