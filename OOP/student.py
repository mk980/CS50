class Student:
    def __init__(self, name: str, house: str) -> str:
        self.name = name
        self.house = house
        

    def __str__(self) -> str:
        return f"{self.name} from {self.house}"

    @property
    def name (self):
        return self.name
    
    @name.setter
    def name (self, name):
        if not name:
            raise ValueError ("Missing name")
        self._name = name

    @property
    def house (self):
        return self._house
    
    @house.setter
    def house (self, house: str):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError ("Invalid house")
        self._house = house

    # def charm (self) -> str:  
    #     match self.patronus:
    #         case  "Stag":
    #             return "sd"

def main():
    student = get_student ()
    print (student)
    # print ("Expecto patronum!")
    # print (student.charm())
    
def get_student():
    # student = Student()
    # student.name = input ("Name: ")
    # student.house = input ("House: ")
    name = input("Name: ")
    house = input ("House: ")
    # patronus = input ("Patronus: ")
    
    return  Student(name, house)
    
if __name__ =="__main__":
    main ()
    
    
    
    
    
class Student:
    def __init__(self, name: str, house: str) -> str:
        self.name = name
        self.house = house
        

    def __str__(self) -> str:
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get (cls):
        name = input ("Name: ")
        house = input ("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print (student)


if __name__ =="__main__":
    main ()
    