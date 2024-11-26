
class Person:
    def __init__(self, first_name, last_name, birth_date, nationality):
        self.first_name = first_name  
        self.last_name = last_name    
        self.birth_date = birth_date  
        self.nationality = nationality 


    def get_data(self):
        return f"Ism: {self.first_name}, Familiya: {self.last_name}, Tug'ilgan sana: {self.birth_date}, Millati: {self.nationality}"

class Student(Person):
    def __init__(self, first_name, last_name, birth_date, nationality, grade, coins):
        super().__init__(first_name, last_name, birth_date, nationality)  
        self.grade = grade         
        self.coins = coins 

    def get_coins(self):
        return self.coins 

    def get_class(self):
        return self.grade  


person = Person("Ali", "Valiyev", "2000-05-15", "O'zbek")
print(person.get_data())  

student = Student("Hasan", "Qodirov", "2005-08-10", "O'zbek", 9, 150)
print(student.get_data()) 
print("Koinlar soni:", student.get_coins()) 
print("Sinf:", student.get_class())  
