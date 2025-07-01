a=[1,1,2,2,1,4,4,5,3,4,6,5,7,8,6,18,8,1]
high=a[0]
for i in a:
    if i>high:
        high=i
print(high)