# # import apscheduler as ap
# import shutil
# print(dir(shutil))

# a=iter({
#     'a':10,
#     'b':20
# })

# print(next(a))
# print(next(a))
# print(next(a))

# def gen():
#     for i in range(10):
#         yield i
    
# a=gen()

# print(next(a))
# print(next(a))
# print(next(a))

#? Print vowel using generator

def vowel(s):
    for i in s:
        if i in "aeiouAEIOU":
            yield i

data=vowel("Rahul")
print(next(data))
print(next(data))
# print(next(data))