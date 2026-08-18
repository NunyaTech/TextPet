import random
pet = input("""welcome to text pet, a virtual pet played with only text!
In this pet simulator you have to take care  of a virtual pet of your choice!
Which pet would you like? a) dog, b) cat, c) bird, d)hamster (input the letter): """)
if pet == "a" or "dog":
        print("Congrats on your new dog!")
        Name = input("Name Him: ")
        while True:
            what_to_do = random.randint(1, 3)
            if what_to_do == 1:
                Food = input(f"Ruff Ruff! {Name} is hungry! type f to feed him!")
                if Food == "f":
                    print(f"Ruff Ruff! Pant! {Name} is Happy!")
                else:
                    print("Really, you're not feeding your own pet!?")
            elif what_to_do == 2:
                Drink = input(f"{Name} is very thirsty. Type w to satisfy his thirst.")
                if Drink == "w":
                    print(f"Pant Pant(gulp, sigh), {Name} is so grateful you nourished him with water!")
                else:
                    print(f"{Name} is very unhappy you did not give him water.")
            elif what_to_do == 3:
                Bathroom = input(f"{Name} needs to go to the bathroom. Type b to take him out.")
                if Bathroom == "b":
                    print(f"{Name} is very satisfied!")
                else:
                    print(f"{Name} is very unhappy with you.")
if pet == "b" or "cat":
        what_to_do2 = random.randint(1, 3)
        print("Congrats on your new cat!")
        Name = input("Name Her: ")
        while True:
            if what_to_do2 == 1:
                Food = input(f"meow! {Name} is hungry! type f to feed her!")
                if Food == "f":
                    print(f"meow! {Name} is Happy!")
                else:
                    print("Really, you're not feeding your own pet!?")
            elif what_to_do2 == 2:
                Drink = input(f"{Name} is very thirsty. Type w to satisfy her thirst.")
                if Drink == "w":
                    print(f"meow! {Name} is so grateful you nourished her with water!")
                else:
                    print(f"{Name} is very unhappy you did not give her water.")
            elif what_to_do2 == 3:
                Bathroom = input(f"{Name} used the bathroom! Type c to clean her litterbox")
                if Bathroom == "b":
                    print(f"{Name} is very happy with her clean bathroom.")
                else:
                    print(f"Your house is stinking right now. Should have cleaned that litter.")            
if pet == "c" or "bird":
        what_to_do2 = random.randint(1, 3)
        print("Congrats on your new bird!")
        Name = input("Name Her: ")
        while True:
            if what_to_do2 == 1:
                Food = input(f"chirp! {Name} is hungry! type f to feed her!")
                if Food == "f":
                    print(f"chirp! {Name} is Happy!")
                else:
                    print("Really, you're not feeding your own pet!?")
            elif what_to_do2 == 2:
                Drink = input(f"{Name} is very thirsty. Type w to satisfy her thirst.")
                if Drink == "w":
                    print(f"chirp! {Name} is so grateful you nourished her with water!")
                else:
                    print(f"{Name} is very unhappy you did not give her water.")
            elif what_to_do2 == 3:
                Bathroom = input(f"{Name} used the bathroom! Type c to clean her litterbox")
                if Bathroom == "b":
                    print(f"{Name} is very happy with her clean bathroom.")
                else:
                    print(f"Your house is stinking right now. Should have cleaned that litter.")
                    
