# WAp to get following  input=[]’hi’,’byee’,’holiday’]
# output={’hii’:3,’byee’:4,’holiday’:7’}

# a=['hii','byee','holiday']
# b={}
# for i in a:
#     b[i]=len(i) #  Add string as key and its length as value to dictionary 'b'
# print(b)

###########################################################################################################

# WAP  to get the following 
# b=’Python is easyi to learn’
# output={’Python’: 6, ’is’ : 2 , ‘easyi’ : ‘iysae’ ,’to’ : 2 , ‘learn’ : ‘nrael’}


# b="Python is easyi to learn"
# c={}
# d=b.split()
# for i in d:
#     if len(i)%2==0: 
#         c[i]=len(i)
#     else:
#        c[i]=i[::-1]
# print(c)


##########################################################################################################

# WAP to get following output:-
# d={’A’ : 65 ,’B’ : 66,………’Z’ :90 }

# out={}
# for i in range(65,91):
#     out[chr(i)]=i
# print(out)


##########################################################################################################

# WAP to get following output:-
# s='HoLIdAY'
# output={'H': 'h', 'o' :'O', 'L': 'l', 'i': 'I', 'd': 'D', 'a': 'A', 'Y': 'y'}
# s='HoLIdAY'
# out={}
# for i in s:
#     if 65<=ord(i)<=90:
#         out[i]=chr(ord(i)+32)
#     elif 97<=ord(i)<=122:
#         out[i]=chr(ord(i)-32)
# print(out)

# s='HoLIdAY'
# out={}
# for i in s:
#     out[i]=i.swapcase()
# print(out)

##########################################################################################################
    
# WAP to get the following out put :-    
# a={ "star" : 10 , "byee" : 30 , "moon": 80 }
# output={ 10 : ‘star’ , 30 : ‘byee’ , 80 ; ‘moon’ }

# a={ "star" : 10 , "byee" : 30 , "moon": 80 }
# b={}
# c=list(a.keys())
# d=list(a.values())
# for i in d:
#     b[i]=c[d.index(i)] 
# print(b)

# WAP to get the following out put :-
# s=[ 12,3.4, ‘hello’, False, ‘bye’ , ‘python’,8+9j ]
# output={ “hello” : “ho” , “bye” : “be” , “python” : “pn” }

# s=[ 12,3.4, "hello", False, "bye" , "python",8+9j ]
# a={}
# for i in s:
#     if type(i)==str:
#         a[i]=i[0]+i[-1]
# print(a)
    
