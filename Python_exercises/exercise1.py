userName = input("Please tell me Your name ")
userAge = int(input("Please tell me Your age "))
userAgeIn100Years = userAge + 100
print ("Dear", userName, "in 100 years You will be", userAgeIn100Years, "years old!")

value1 = int(input("Please give first number "))
value2 = int(input("Please give second number "))

print ("First number:", value1, "Second number:", value2)

class Animal:
    __size = 0
    __age = 0
    __type = 0
    __friendly = False
    __value = 0
    value2 = 0
    
    def __init__(self, size, age, type, friendly):
        self.__size = size
        self.__age = age
        self.__type = type
        self.__friendly = friendly
        self.__value = 30
        self.value2 = 10

    def __calculateValue2(self):
        self.value2 = 100
    def toString(self):
        return "No elo :D"
    

class Pies(Animal):
    __name = "Nameless"
    __sound = "Wow wow"
    __food = "meat"
    __owner = "Nobody :("

    def __init__(self, size, age, type, name, owner):
        super(Pies, self).__init__(size, age, type, True)
        self.__name = name
        self.__owner = owner

    def toString(self):
        return "I am a dog. My name is", self.__name, "My owner is", self.__owner
        
zwierzak = Animal(10, 10, 5, True)
print (zwierzak.toString())
print (zwierzak.value2)
piesel = Pies(20, 5, "Golden Labrador Retriver", "Sola", "Andrzej")
print (piesel.toString())

