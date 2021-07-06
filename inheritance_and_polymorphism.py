class Person:
    def move(self):
        print("Person: Moves 4 paces")
    def rest(self):
        print("Person: Gains 4 health points")
        
class Doctor(Person):
    def heal(self):
        print("Doctor: Heals 10 health points")

class Fighter(Person):
    def fight(self):
        print("Fighter: Do 10 health points of damage")
    def move(self):
        print("Fighter: Moves 6 paces")
        
class Wizard(Doctor):
    def cast_spell(self):
        print("Wizard: Turns invisble")
    def heal(self):
        print("Wizard: Heals 15 health points")
    
    
character1=Wizard()
character2=Fighter()
character3=Doctor()

party = [character1, character2, character3]

# example of move method being called on a list of instances of different class types
for character in party:
    character.move()

# example of len function behaving in different ways depending on context
string_len = len("abcdefgh")
print(f"len: string = {string_len}")

list_len = len(party)
print(f"len: party = {list_len}")

dict = {"name" : "aaa", "phone" : "12345678"}
dict_len = len(dict)
print(f"len: dict = {dict_len}")