
def nums(n):
    for i in range(0, n+1):
        if i%2==0:
            yield i
        else:
             continue
    
n=int(input())
for i in nums(n):
    print (i, end = ' ')
