def parity_sort(a):
      i = 0
      j = 1
      sorted_once = False
      while j < len(a):
           if a[i] > a[j] and a[i] % 2 == 0 and a[j]%2==0:
                 a[i], a[j] = a[j], a[i]
                 sorted_once = True
                 i =0
                 j =1
           elif a[i] > a[j] and a[j] % 2 == 1 and a[i] % 2 == 0 :
                 a[i], a[j] = a[j], a[i]
                 sorted_once = True
                 i =0
                 j =1
           i +=1
           j +=1
  
      if sorted_once:
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
    