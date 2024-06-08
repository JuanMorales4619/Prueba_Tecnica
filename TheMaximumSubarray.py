def maxSubarray(arr):
    max_current = max_global = arr[0]
    
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    
    max_subsequence = 0
    has_positive = False
    
    for num in arr:
        if num > 0:
            max_subsequence += num
            has_positive = True

    if not has_positive:
        max_subsequence = max(arr)
    
    return [max_global, max_subsequence]

print(maxSubarray([2,-1,2,3,4,-5]))