import random

print("Michael Scott or a philosopher?")
class Michael:
    def __init__(self,michael):
        self.michael=michael
class Philosopher:
    def __init__(self,philosophy,names):
        self.philosophy=philosophy
        self.names=names
        



quotes=Philosopher(['"The unexamined life is not worth living."',
                           '"That which does not kill us makes us stronger."',
                           '"You cannot step into the same river twice."',
                           '"Life can only be understood backwards; but it must be lived forwards."',
                           '"I am not afraid of storms, for I am learning how to sail my ship."',],["Socrates", "Nietzsche","Heraclitus","Kierkegaard","Louisa May Alcott"])


hi=Michael(['"“Do I need to be liked? Absolutely not. I like to be liked. I enjoy being liked. I have to be liked. But it’s not like this compulsive need like my need to be praised.”',
         '"Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me."',
         '"And I knew exactly what to do. But in a much more real sense, I had no idea what to do."',
         '"Society teaches us that having feelings and crying is bad and wrong. Well, that is baloney, because grief is not wrong. There is such a thing as good grief."',
         '"Business is like jazz, if you’re not having fun, you’re doing it wrong."',
         '"I am ready to face any challenges that might be foolish enough to face me."',
         '"Today I will do absolutely nothing in an attempt to lessen the effect of an otherwise mundane Monday.”',
         '"You have to play to win. But you also have to win to play."',
         '"Love is the water of life, drink deeply."'])


category = random.choice([quotes.philosophy, hi.michael])
choice = random.choice(category)

print(choice)
guess = input("Michael Scott or a philosopher: ").lower()

if choice in quotes.philosophy:
    index = quotes.philosophy.index(choice)
    print(f"{choice} was quoted by {quotes.names[index]}")
    answer = "philosopher"
else:
    print(f"{choice} was quoted by Michael Scott")
    answer = "michael scott"

while answer != guess:
    print("Wrong answer, try again!")
    guess = input("Michael Scott or a philosopher: ").lower()

print("Correct answer, you did it!")












