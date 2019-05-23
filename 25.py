#obj2._animal.__df
class animal:
    accept=0
    a=['dog','cat','rat']
    def __init__(self,species):
        if species not in animal.a:
            raise ValueError("this is not animals")
        else:
            animal.accept+=1
class dog(animal):
    def __init__(self,species):
        self.species=species
        super().__init__(self.species)
        if self.accept==1:
            self.breed()
        else:
            raise ValueError("this is not animals")
    def breed(self):
        b=input("Enter the breed")
            
obj=dog('hen')
obj2=animal('dog')
