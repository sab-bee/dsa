def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2

  L = arr[:mid]  # left part of the array
  R = arr[mid:] # right part of the array

  lsa = mergeSort(L) # left sorted array
  rsa = mergeSort(R) # right sorted array

  return merge(lsa, rsa)

def merge(L, R): # merge previously sorted arrays
  sorted = []  # out of place array
  
  i=j=0
  while i < len(L) and j < len(R):
    if L[i] < R[j]:
      sorted.append(L[i])
      i+=1
    else:
      sorted.append(R[j])
      j+=1
  
  while i < len(L):
    sorted.append(L[i])
    i+=1

  while j < len(R):
    sorted.append(R[j])
    j+=1

  return sorted


if __name__ == "__main__" :
  arr = [45, 25, 31, 66, 54, 87]
  arr = mergeSort(arr)
  print(arr)