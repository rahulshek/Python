
class A:
    property1=10

class B:
    property2=20

class C:
    property3=30

class D(A,B,C):
    pass

print(D.property1)
print(D.property2)
print(D.property3)