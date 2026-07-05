import random
pet = input("""welcome to text pet, a virtual pet powered by only text!
in this pet simulator you have to take care  of a virtual pet of your choice!
which pet would you like? a) dog, b) cat, c) bird, d)hamster (input the letter): """)
what_to_do = random.randint(1, 4)
if pet == "a":
    print("Congrats on your new dog!")
    dogName = input("Name Him: ")
    if what_to_do == 1:
        dogFood1 = input(f"Ruff Ruff! {dogName} is hungry! type f to feed him!")
        if dogFood1 == "f":
            print(f"Ruff Ruff! Pant! {dogName} is Happy!")
        else:
            print("Really, you're not feeding your own pet!?")
    elif what_to_do == 2:
        
