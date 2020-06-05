import ctypes as ct
lib = ct.CDLL(r'C:\Users\sri\Documents\Python_Scripts\c_prog\array_functer.so')

######################################################
fp = ct.CFUNCTYPE(ct.c_int , ct.c_int , ct.c_int) #creating a Function pointer fp
fp_a = fp * 3 #creating the array of type function pointer

##############################
#creating a function pointer for each function 
add = fp(lib.add) 
sub = fp(lib.sub)
mul = fp(lib.mul)

fp_aa = fp_a(add,sub,mul) # defining the array of function pointers

res_add = fp_aa[0](1,5)
res_sub = fp_aa[1](5,3)
res_mul = fp_aa[2](6,3)

print(res_add,res_sub,res_mul)