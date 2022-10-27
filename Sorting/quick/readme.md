## quick sort

> first method

- in this method `first` element is the pivot element
- for already sorted array worst case complexity is O(n<sup>2</sup>)
    - worst case complexity happens if the partitioning algo the larges or smallest element as pivot every time
- if the array is reversly sorted `overflow error` will happen if not use infinity value as last element

### time complexity
- best case O(nlogn)
- worst case O(n<sup>2</sup>)
- average case O(nlogn)
```
function quickSort <- arr, low, high
    base case <- recursive call untill low < high

    pivot <- partition(arr, low, high)
    quicksort(arr, low, pivot-1)
    quicksort(arr, pivot+1, high)

function partition <- arr, low, high
    pivot <- arr[low])
    p = low, q = high

    while p < q
        while arr[p] <= pivot 
            p++
        while arr[q] > pivot
            q--
        if p < q
            swap(p, q)
    swap(low, q)
    return q
```

> second method
- `middle` element as pivot
- for already sorted array it will be average case complexity as pivot cant be largest or the smallest element
- no need to use infinity garbage value

```
function quickSort <- arr, low, high
    base case <- recursive call untill low < high

    pivot <- partition(arr, low, high)
    quicksort(arr, low, pivot-1)
    quicksort(arr, pivot+1, high)

function partition <- arr, low, high
    m = (p+q)/2
    pivot <- arr[m]) // change here
    p = low, q = high

    while p < q
        while arr[p] <= pivot 
            p++
        while arr[q] > pivot
            q--
        if p < q
            swap(p, q)
    swap(m, q) // change here
    return q
```

