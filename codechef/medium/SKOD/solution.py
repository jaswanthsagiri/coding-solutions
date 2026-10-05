# cook your dish here
i=int(input())
for _ in range(i):
    m=int(input())
    arr=list(map(int,input().split()))
    tot=sum(arr)
    min_v=min(arr)
    print(tot-min_v)