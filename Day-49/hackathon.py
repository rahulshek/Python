#Print the sub array of the given list 
a=[3,1,2,1,1,1,5]
out=[]
target=6


# counter=0
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        # out.append(a[i:j:])
        e=len(a[i:j:])
        # print(e)
        # print(len(a[i:j:]))
        if e>1:
            w=sum(a[i:j:])
            # print(w)
            if w==target:
                # counter+=1
                out.append(a[i:j:])
                # print(len(a[i:j:]))

print(len(out[-1]))
print(out)


        