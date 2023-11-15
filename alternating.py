for _ in range(int(input())):
    n = int(input())
    a= list(map(int,input().split()))
    
    left = 0  # Left pointer
    right = 0  # Right pointer
    s = 0  # Sum of the maximum subarray
    mx = a[0]  # Maximum element
    
    while right < n:
        if a[right] * mx < 0:
            s += mx
            mx = a[right]
            left = right
        else:
            mx = max(mx, a[right])
        
        right += 1
    
    s += mx
    
    print(s)