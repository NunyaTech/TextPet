import random
pet = input("""welcome to text pet, a virtual pet played with only text!
In this pet simulator you have to take care  of a virtual pet of your choice!
Which pet would you like? a) dog, b) cat, c) bird, d)hamster (input the letter): """)
if pet == "a" or "dog":
    while True:
        what_to_do = random.randint(1, 3)
        print("Congrats on your new dog!")
        dogName = input("Name Him: ")
        while True:
            if what_to_do == 1:
                dogFood = input(f"Ruff Ruff! {dogName} is hungry! type f to feed him!")
                if dogFood == "f":
                    print(f"Ruff Ruff! Pant! {dogName} is Happy!")
                else:
                    print("Really, you're not feeding your own pet!?")
            elif what_to_do == 2:
                dogDrink = input(f"{dogName} is very thirsty. Type w to satisfy his thirst.")
                if dogDrink == "w":
                    print(f"Pant Pant(gulp, sigh), {dogName} is so grateful you nourished him with water!")
                else:
                    print(f"{dogName} is very unhappy you did not give him water.")
            elif what_to_do == 3:
                dogBathroom = input(f"{dogName} needs to go to the bathroom. Type b to take him out.")
                if dogBathroom == "b":
                    print(f"{dogName} is very satisfied!")
                else:
                    print(f"{dogName} is very unhappy with you.")
if pet == "b" or "cat":
    while True:
        what_to_do2 = random.randint(1, 3)
        print("Congrats on your new cat!")
        catName = input("Name Her: ")
        while True:
            if what_to_do2 == 1:
                catFood = input(f"meow! {catName} is hungry! type f to feed him!")
                if catFood == "f":
                    print(f"meow! {catName} is Happy!")
                else:
                    print("Really, you're not feeding your own pet!?")
            elif what_to_do2 == 2:
                catDrink = input(f"{catName} is very thirsty. Type w to satisfy her thirst.")
                if catDrink == "w":
                    print(f"meow! {catName} is so grateful you nourished her with water!")
                else:
                    print(f"{catName} is very unhappy you did not give her water.")
            elif what_to_do2 == 3:
                catBathroom = input(f"{catName} used the bathroom! Type c to clean her litterbox")
                if catBathroom == "b":
                    print(f"{catName} is very happy with her clean bathroom.")
                else:
                    print(f"Your house is stinking right now. Should have cleaned that litter.")            

                
            
