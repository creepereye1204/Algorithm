
def solution(sequence):

    l = len(sequence)
    arr1 = [sequence[i]*((-1)**i) for i in range(l)]
    arr2 = [sequence[i]*((-1)**(i+1)) for i in range(l)]
    for i in range(1, l):
        arr1[i] += arr1[i-1]
        arr2[i] += arr2[i-1]

    return max(max(arr1)-min(arr1), max(arr2)-min(arr2))
