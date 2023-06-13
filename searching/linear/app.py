def linearSearch(arr, k):
    i = 0
    while i < len(arr):
        if arr[i] == k:
            return i
        else:
            i+=1
    return -1

if __name__ == "__main__":
    arr = [5,7,9,12,15,20,24,27,33,40,50,65,72]
    inp = input('enter k\n')
    ans = linearSearch(arr, int(inp))
    print(ans)