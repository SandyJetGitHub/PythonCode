def highest_even(numList):
  evenList=[]
  for number in numList:
    if number % 2 == 0:
      evenList.append(number)
  print(evenList)
  return max(evenList)

print(highest_even([10,2,55,99,0,5,66]))
