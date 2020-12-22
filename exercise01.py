def repeats(arr):
  single_digit = []
  
  for x in arr:
    if arr.count(x) == 1:
      single_digit.append(x)
      print(single_digit)
  return sum(single_digit)