

```
function mergeSort <- arr
  base case -> return the array if len of the array <= 1
  mid <- array length / 2

  L[] <- all the values before mid (including mid)
  R[] <- all the values after mid

  lsa <- mergeSort(L) // get left sorted array through recursive call
  rsa <- mergeSort(R) // get right sorted array through recursive call

  return merge(lsa, rsa) // send both array to merge

function merge <- lsa, rsa
  sorted[] // empty array

  i=j=0
  while i < lsa & j < rsa
    if L[i] < R[j]
      sorted[] <- L[i]
      i++
    else 
      sorted[] <- R[j]
      j++

  // now add all the elements that are left after sorting
  while i < lsa
    sorted[] <- L[i++] 

  while j < rsa
    sorted[] <- R[j++]

  return sorted
```

![merge](https://i.ibb.co/XjnNbTJ/Frame-1.png)