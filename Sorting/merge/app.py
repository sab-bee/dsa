def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    l = arr[:mid]
    r = arr[mid:]
    lsa = mergeSort(l)
    rsa = mergeSort(r)
    return merge(lsa, rsa)

def merge(lsa, rsa):
    arr = []
    i = j = 0

    while i < len(lsa) and j < len(rsa):
        if lsa[i] < rsa[j]:
            arr.append(lsa[i])
            i+=1
        else:
            arr.append(rsa[j])
            j+=1
    while i < len(lsa):
        arr.append(lsa[i])
        i+=1
    while j < len(rsa):
        arr.append(rsa[j])
        j+=1
    
    return arr

if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    arr = mergeSort(arr)
    print(arr)