
# #? WAP to ge the following output
# input = "Hi it is easy "
# # out={"Hii":3 , "it":2 , "is":1 , "easy":1}

# out = {}
# for i in input.split():
#     out[i]=len(i)

# print(out)


# a='PyTHon'
# lower=""
# upper=""
# for i in a:
#     if 'A'<=i<='Z':
#         upper=upper+i
#     elif 'a'<=i<='z':
#         lower=lower+i
# print(upper+lower)


# a='PyTHONNative'
# lower=""
# upper=""
# for i in a:
#     if 'A'<=i<='Z':
#         upper=upper+i
#     elif 'a'<=i<='z':
#         lower=lower+i
# print(lower+upper)



a='P@#yn26at^&i5v'
chr=0
num=0
sp=0
for i in a:
    if 'A'<=i<='Z' or 'a'<=i<='z':
        chr+=1
    elif '0'<=i<='9':
        num+=1
    else:
        sp+=1
print(chr,num,sp)