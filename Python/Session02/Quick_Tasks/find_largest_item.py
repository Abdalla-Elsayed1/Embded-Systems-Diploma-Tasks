x=[2,4,5,7,8,5,4,10]
#cpp method
bv=0
for i in range(len(x)):
    if x[i]>bv:
        bv=x[i]
print(bv)
#------------------------
x.sort()
print(x[-1])
#---------------------
print(max(x))