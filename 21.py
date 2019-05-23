# _a=10 #protected
# __b=10 #private
# a=10 #public
#same function name with diff no. of parameter is not accepted
# def __init__(self):
#for default constructer
#self point to current obj
'''
def abc(a,b,c):
    return a+b+c
def ab(a,b):
    return a+b
print("sum three parameter:",abc(2,3,4))
print("sum two parameter:",ab(2.5,9))
'''
'''
class uni():
    def __init__(self):
        print("hy")
    def full(self):
        print("bye")
obj=uni()
obj.full()
correct
'''
'''
class uni():
    def __init__(self):
        print("hy")
    def full():
        print("bye")
obj=uni()
obj.full()
error
'''


'''
class uni():
    def __init__(self):
        print("hy")
    def full():
        print("bye")
obj=uni()
uni.full()
run correctly
'''
'''
object is super class and every class is sub class
#we can declare variabl outside the class with the help of object 
#creation of constructor
class myclass:
    def __init__(self,first,last):
    self.first=first
    self.last=last
    self.fullname=self.first+" "+self.last;
    print("constructor is called")
//object creation
obj1=myclass('name','last');
print(obj1.fullname)

'''

'''


'''




#----------------------------------------------------------
#def exam
#def rollno
count=0
total=0
d1={}
d={}
i=1
class university:
    def __init__(self,first,last):
        global total
        self.first=first
        self.last=last
        total+=1
        print("welcome",first,last)
    def exam(self):
        global count
        count=count+1
        print("total number of students is:",count)
    def rollno(self,rn):
        self.roll=str(rn)
        d1.update({'rollno':self.roll})
        d.update({i:d1})
        print("your roll number is 16MH1A05"+self.roll)
        print(d1)
    def marks(self,marks):
        print("your score is ",marks)
    def completed():
        pass
    def result(self,score):
        if(score>35):
            print("pass")
        else:
            print("Fail")
    def tstudent(self):
        print("total number of students is ",total)
obj=university("prafulla","raj")
obj2=university("bell","rd")
obj2.exam()
obj2.rollno(46)
obj2.marks(55)
obj2.result(55)
obj.tstudent()

    
    



