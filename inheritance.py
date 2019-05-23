#in super no need of self
class A:
    def __init__(self):
        print("I am in A")
class B():
    def __init__(self):
        #super().__init__("aaa")
        print("i am in B")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("i am in C")
obj1=C()        
        
