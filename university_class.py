class AICTE:
    def __init__(self):
        print("AICTE")
class university(AICTE):
    def __init__(self):
        print("there are 3 college under me")
class du(university):
    def __init__(self):
        print("i am du")
    def exam(self):
        print("exam completed in du")
    def result(self):
        print("results of du are out")
class sriram(university):
    def __init__(self):
        print("you are in sriram")
    def exam(self):
        print("now you can give exam of sriram")
    def result(self):
        print("result of sriram are out")
class hansraj(university):
    def __init__(self):
        print("u are in hansraj")
    def exam(self):
        print("now you can give exam of hansraj")
    def result(self):
        print("result of hansraj are out")
class E(du,sriram,hansraj):
    def __init__(self):
        print("first you have to clear du exam ")
        super().__init__()
    def exam(self):
        super().exam()
        super().result()
        print("you can give rest exam")
    def result(self):
        print("result will be displayed soon")
obj1=E()        
obj1.exam()
obj1.result()
