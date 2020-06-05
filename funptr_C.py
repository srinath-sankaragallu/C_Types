import ctypes as ct

lib = ct.CDLL(r'C:\Users\sri\Documents\Python_Scripts\c_prog\funptr2.so')

addone = lib.addone
addtwo = lib.addtwo

res = lib.f(5 , addtwo)
print(res)

@ct.CFUNCTYPE(ct.c_int ,ct.c_int )
def addthree(n):
    return n + 3

i = ct.c_int(5)
res1 = lib.f(i , addthree)

print(res1)



