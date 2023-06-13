def binarySearch(arr, k, l, r):
    if l > r:
        return -1

    mid = (l+r)//2
    if arr[mid] == k:
        return mid
    
    if k < arr[mid]:
        return binarySearch(arr, k, l, mid-1)
    else:
        return binarySearch(arr, k, mid+1, r)

if __name__ == "__main__":
    arr = [5,7,9,12,15,20,24,27,33,40,50,65,72]
    inp = input('enter k\n')
    ans = binarySearch(arr, int(inp), 0, len(arr)-1)
    print(ans)