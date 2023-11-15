def botE(n1,n2):
    if n1%2 ==0 and n2%2==0:
        return True
    return False
def both0(n1,n2):
    if n1%2 ==0 and n2%2==0:
        return True
    return False
    
    






n = int(input())
i =0
while i < n:
    m = int(input())
    arr = list(map(int,input().split()))
    left =0
    right =1
    while left<right:
        if arr[left]> arr[right] and botE(arr[left],arr[right]):
            arr[left],arr[right]== arr[right],arr[left]
            left+=1
            right+=1
        if arr[left]> arr[right] and both0(arr[left],arr[right]):
            arr[left],arr[right]== arr[right],arr[left]
            left+=1
            right+=1
    if arr.sort == arr:
        print ("yes")
    else:
        print("NO")
    
    i+=1

        
                
    