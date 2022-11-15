def sum(k): # Define the my recursion function with k as input
  if k>0:
    result = k + sum(k-1) #  the input k with the k - 1 until to k - 1 = 0
    print(result) # Show the  of k + k - 1 + k - 2 ...
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
sum(6)
