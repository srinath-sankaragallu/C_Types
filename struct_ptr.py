import ctypes as ct

#loading the library
lib = ct.CDLL(
        r'C:\Users\sri\Documents\Python_Scripts\c_prog\struct_ptr.so'
        )


def get_c_fun(lib,func_name , arg_type = None , res_type = None):
    try:
        func_name = lib.__getattr__(func_name)
        if arg_type is not None:
            func_name.argtype = arg_type
        if res_type is not None:
            func_name.restype = res_type
        return func_name
    except:
        return None

class student(ct.Structure):
    _fields_ = [('name' , ct.c_char *50) , ('age' , ct.c_int)]
    def __init__(self , name = None , age = None):
        if name is not None:
            self.name = name
            self.age = age
        else:
            exmp1 = get_c_fun(lib,'getInformation' , None , student)()
            self.name = exmp1.name 
            self.age =  exmp1.age
    
    def display(self):
        return get_c_fun(lib , 'display' , ct.POINTER(student) )(ct.byref(self))
    
    def updateinfo(self):
        return get_c_fun(lib , 'updateinfo' , ct.POINTER(student))(ct.byref(self))


s2 = student()
s2.display()
s1 = student(b'lavanya' , 18)
s1.display()
s1.updateinfo()
s1.display()











#     def __init__(self,name = None,age = None ):
#         if name != None:
#             self.name = name
#             self.age = age
#         else:
#             val = lib.getInformation
#             val.res_type = student
#             vals = val()
#             self = val()

#     def display(self):
#         return get_c_fun(lib ,'display' , ct.POINTER(student) , None )(ct.byref(self))

# s1 = student()
# print(s1.name)
# print(s1.age)
# s2 = student(b'Lavanya' , 22)
# s2.display()
