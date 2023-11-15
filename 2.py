def parity_sort(a):
  i = 0
  j = len(a)-1
  m = sorted(a)
  while i <= j:
    if a[i] > a[j] and a[i] % 2 == 0 and a[j]%2==0:
      a[i], a[j] = a[j], a[i]
      i +=1
      j -= 1
    elif a[i] > a[j] and a[j] % 2 == 1 and a[i] % 2 == 1 :
      a[i], a[j] = a[j], a[i]
      i +=1
      j -= 1
   
    
   
  
  if a == m:
      print("yes")
      print(a)
  else:
      print("No")
      print(a)
    




n = int(input())
i =0
while i < n:
    m= int(input())
    a = list(map(int, input().split()))
    parity_sort(a)
    i+=1
    
    
    
3