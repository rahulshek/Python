# WAP to get output :-  
# input='abcabbcba'
# output={ “a” : 3 ,”b” : 4 , “ c” : 2 }
# o='abcabbcba'

# out={}
# for i in o:
#     out[i]=o.count(i)
# print(out)

#---------------or ----------
# o='abcabbcba'
# out={}
# for i in o:
#     if i not in out:
#         out[i]=1
#     else:
#         out[i]+=1
# print(out)


#------------------------------------------------------------------------------------------------------


# WAP  to get the following out put :-
# input = “ i am also present there”
# output = { “i” :  1 , “a” : 2 , “ o “ : 1 , “e “ :4 }

# ins="i am also present there"
# out={}
# for i in ins:
#     if i in 'AEIOUaeiou':
#         if i not in out:
#           out[i]=1
#         else:
#           out[i]+=1
# print(out)


#------------------------------------------------------------------------------------------------------

# WAP to get the following output:-
# input = [ “python.py” , “pro1.html” , “pro3.py” , “google.com”]
# output = [ “py” , “html” , “py” , “com”]

# a=["python.py" , "pro1.html" , "pro3.py" , "google.com"]
# out=[]
# for i in a:
#     result=i.split('.')
#     out.append(result[-1])

# print(out)

#--------------------------------------------------------------------------------------------------------


# WAP to get the following Output :-
# input =  [ "p1.pt" , "file2.txt" , "file1.py" , "google.com" , "data.txt" ]
# output = { "py" : ["p1" , "file1"] , "txt" : ["file2" , "data"] , "com" : ["google"] } 

input =  [ "p1.py" , "file2.txt" , "file1.py" , "google.com" , "data.txt" ]
out={}
for i in input:
    result=i.split('.')
    if result[-1] not in out:
        out[result[-1]]=[]
        out[result[-1]].append(result[0])
    else:
        out[result[-1]].append(result[0])
print(out)





