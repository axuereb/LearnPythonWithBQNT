class Dog:

    def __init__(self, **kwargs):
    
        self.name = kwargs.get('name', 'Max')
        self.age = kwargs.get('age', 1)
        self.breed = kwargs.get('breed', 'alsatian')
        
        print("Woof")
   
    def __repr__(self):
        return '''<Dog name={name} breed={breed} age={age} {id}>'''.format(**self.__dict__, id=id(self)) 
       
    @staticmethod    
    def bark(): #notice this is a static method - it does not require self 
        print("Woof, Woof!")

dog1 = Dog()
dog1.bark()

dog2 = Dog(name='Rex', age=2)
dog2.bark()

(dog1, dog2)
