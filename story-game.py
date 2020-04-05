#== comparison
#< less than
#<= less than equal to
#> greater than
#>= greater than equal to

# or One needs to be true
# and Both need be true to be true
# not oppisite of True or False

"""Build a story game with different scenarios using if statements.
Make sure you use the health variable to keep track of health and have the users health change
in different scenarios"""
health = 100
#Set health by doing health = health + or - <number here>
print("You are on a journey to explore the world when you find a dungeon in a hazy mist.")
choice = input("Do you enter the dungeon or go back into the mist? (Y/N)")

if choice == "Y":
    #Examples
    print("You enter the dungeon.")
    print("Its pitch back except for a single torch.")
    choice = input("Do you grab the torch? (Y/N) ")
    if choice == "Y":
        print("You shine the light in the room and see two large doors; A large door and a small door")
        door =input("Do you enter the large door or the small door. (L/S) ")
        if door =="L":
            print("You push with all your might to enter the large door")
            print("You place the torch in an empty holster on the wall which somehow magically light the rest of them")
            print("You find yourself in what looks like a weapons locker with another door at the far end")
            print("On Left side of the wall you see there is a sword and shield ")
            print("On the Right you see a Wand and wizard hat")
            choice =input("Which one do you grab? (L/R) ")
            if choice == "L":
                print("You grab the sword and shield and gain 50 health")
                health = health + 50
                print(f"Health is increased to {health}!")
                print("You enter the door at the far end of the room")
                print("I GOT LAY AND GAVE U SO YOU WIN IF YOU CHOOSE THIS PASS CONGRATS LOL")
            elif choice == "R":
                print("You grab ahold of the wand and put on the hat")
                print("You feel a strange sensation and get teleported to another room")
                print("The room seems empty except for a cauldron with a strange green boiling liquid?")
                choice =input("A whisper is heard saying which would you like to drop the hat or the wand? (H/W) ")
                if choice == "H":
                    print("The hat dissolves and a shadoow creeps out and comsumes you body")
                    print("Game Over")
                elif choice == "W":
                    print("The wand sinks to the bottom of the cauldron and you notice the caldroun bubbling, you back away but its too late.")
                    print("the cauldron explode sending metal flying towards you")
                    print("Dying on the floor you see a figure reaching for you hat and thanks you for releasing it")
                    print("The last image you see is the building crubling and the figure walking away")
                    print("GAME OVER!")

        elif door == "S":
            print("You squeeze through the small door only to find that it leave now where after crawling for a while decide to turn back")
            print("On your way back you notice the whole getting bigger and bigger.") 
            print("Right as soon as your able to stand up you finds yourself on the outside of your home town") 
            print("You decide to call it a day and go home. THE END")              
    elif choice == "N":
        print("Unable to see anything you decide to wander in the darkness and fall into a pit")
        health = health - 100
        print("You Died!")
        print("Game Over")
elif choice == "N":
    print("You go back into the mist.")
    print("You wander for days only to find yourself back at the dungeons entrance")
    health = health - 50 
    print("You lose 20 health from wandering in the mist")
    print("Health is now {health}!")
    print("Do you enter the dungeon or go back into the mist")
    choice = input("Yes or No? (Y/N)")
    if choice == "Y":
        print("A small child comes out from the dungeon.")
    elif choice == "N":
        print("You decide going back into the mist is the better idea")
        print("You notice something strange with the mist like its heavier than normal")
        print("An arrow swoops by, grazes you and you lose 5 health!")
        health = health - 5 
        print("Current health is {health}!")
        print("Do you continue into the mist? (Y/N)")
        if choice == "Y":
            print("You hear yelling in the distance and make haste towards the sound")
            print("A large scale battle is going with orcs and mages and elves")
            print("Do you join the orcs, mages or elves?")
            choice = input("O/M/E?")
            if choice == "O":
                print("You walk towards the orcs hoping they help you only to get torn apart by one of the small ones!")
                print("GAME OVER!")
            elif choice =="M":
                print("Enchanted by the mages you run by in order to help the but unknowlingly a stray bolt comes hurdling towards you. Instantly killing you.")
                print("GAME OVER!")
            elif choice == "E":
                print("As the elves are on the far side of the field you decide to run towards them seeking to aide")
                print("Trying to get their attention you go yell that you are coming to help")
                print("Unaware of you actions due to not knowing the human language. The elves see you as a hostile and send an barrage of arrows to you")
                print("You get shot all over and bleed out in the middle of the battle field.")
                print("Game over")
        elif choice == "N":
            print("After wandering for what seems like eons you see a town further in the mist.")
            print("Because of several day without food or water you run farther into the mist desperate to survive")
            print("The town turns out to be a mirage You are swallowed up by the mist never to be seen again")
            health = health - 100
            print(f"Health is {health}! GAME OVER!")