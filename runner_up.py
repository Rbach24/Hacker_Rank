 n = int(input())
    arr = map(int, input().split())
    Brr = list(arr)
    x = Brr[0]
    for i in Brr :
        if i > x : 
            x = i
    
    c = Brr.count(x)
    for i in range(0,c):
        Brr.remove(x)
    y = Brr[0]
    for i in Brr :
        if i > y:
            y = i
