class Wizard:
    def __init__(self, name: str) -> str:
        if not name:
            raise ValueError ("Missing name")
        self.name = name
        
        
    

class Student(Wizard):
    def __init__(self, name: str, house: str) -> str:
        super ().__init__(name)
        self.house = house
        
class Professor(Wizard):
    def __init__(self, name: str, subject: str) -> str:
        super ().__init__(name)
        self.subject = subject
        
        
wizard = Wizard ("Ablus")
student = Student("Harry", "Gryffindor")
professor = Professor ("Severus", "Defense against the Dark Arts")