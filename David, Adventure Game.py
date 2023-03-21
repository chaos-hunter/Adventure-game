name = input("What is your name: ")
print("Welcome to my Adventure Game " + name +" hope you have fun")
print("You are stranded on a foreign planet and must find a way to escape, using your smarts\n")

while True:
    choice = input("Do you want to: \n"
                   "1. Explore the surrounding area for resources\n"
                   "2. Attempt to fix your damaged spaceship\n"
                   "3. Search for signs of intelligent life\n"
                   "4. Build a shelter and wait for rescue\n"
                   "5. Use your emergency beacon to signal for help\n"
                   "Enter your choice (1-5): ")

    if choice == "1":
        print("\nYou explore the area and come across a crashed spaceship.")
        print("You find valuable resources that you can use to fix your own spaceship.\n")
        while True:
            choicerepair = input("Do you want to: \n"
                                  "1. Use the resources to fix your own spaceship\n"
                                  "2. Take the crashed spaceship as your own\n"
                                  "Enter your choice (1-2): ")
            if choicerepair == "1":
                print("\nYou fix your space ship but need one more piece to complete your spaceship")
                print("\n In hopes of finding the piece you need you start wandering unti you hear noise")
                while True:
                    choiceescape = input("Do you want to "
                                         "1. walk towards the noise" 
                                        "2.walk back to your ship\n")
                    if choiceescape == "1":
                        print("When you walk to the noise you find out is a fellow human running away from aliens")
                        print("You see he's crashed ship has the missing part")
                        while True:
                            choiceescape1 = input("Do you want to"
                                                  "1. Try and lore the aliens away from him \n"
                                                  "2. Take the piece and run away back to your ship")
                            if choiceescape1=="1":
                                print("You created a racket that now attracted the aliens to you")
                                print("By doing this all the aliens came after you so you died nobly")
                                print("Mission still failed though")
                                break
                            elif choiceescape1 =="2":
                                print("You run back to your space ship and install the piece")
                                print("Your space ship still needs time to start up")
                                print("The aliens are now heading your way, ")
                                print("you need approximately 5 minutes to get it working ")
                                while True:
                                    choiceescape2 = input("How do you want to distrac them"
                                                  "1. Out run them for five minutes"
                                                  "2. Use your ray gun to fend them off for now"
                                                  "Enter your choice (1-2")
                                    if choiceescape2 == "1":
                                        print("Because you've been walking and running your low on energy")
                                        print("The aliens catch up to and capture you")
                                        print("Mission failed,you were caught")
                                        break
                                    elif choiceescape2 =="2":
                                        print("You fended off the aliens succesfully bying yourself time")
                                        print("Mission successful")
                                        break
                                    else:
                                        print("\nInvalid choice pick (1-2)")


                    elif choiceescape == "2":
                        while True:
                         print("When going back to your ship aliens were waiting there for and have now jumped you")
                        print("You've now been captured, Mission failed")
                        break
                    else:
                        print("\nInvalid choice please enter 1-2")

                break
            elif choicerepair == "2":
                print("\nYou take the crashed spaceship but it explodes as your leaving")
                print("Mission failed\n")
                break
            else:
                print("\nInvalid choice. Please enter 1 or 2.")
        break
    elif choice == "2":
        print("\nYou attempt to fix your spaceship, but you make a critical error.")
        print("The ship explodes, killing you instantly.\n")
        print("You have failed your mission.\n")
        print("Start again")
    elif choice == "3":
        print("\nYou search for signs of intelligent life and encounter a hostile alien species.")
        print("You are captured and become a prisoner for the rest of your life.\n")
        print("You have failed your mission.\n")
        print("Start again")
    elif choice == "4":
        print("\nYou are rescued by a passing spaceship and escape the planet.")
        print("Congratulations! You have completed your mission.\n")
        break
    elif choice == "5":
        print("\n You attracted a deadly alien race to you")
        print("\n they are coming towards you with ray guns")
        while True:
            choicesurvive = input("Do you want to: \n"
                                  "1.Fight them back with your gun\n"
                                  "2.Run away\n"
                                  "Enter your choice (1-2): ")
            if choicesurvive == "1":
                print("\n The aliens killed you because there was just one of you and multiple of them")
                print("Congratulations! You failed your mission by suicide")
                break
            elif choicesurvive == "2":
                print("\nWhile running you spot a bunker")
                while True:
                    choicesurvuve1 = input("Do you want to: \n"
                                           "1. Head to the bunker\n"
                                           "2. Continue running away from the aliens\n"
                                           "Enter your choice(1-2): ")
                    if choicesurvuve1 == "1":
                        print("\n While in the bunker you meet another human there he's asleep")
                        while True:
                            choicesurvive2 = input("Do you want: \n"
                                                   "1. Wake him up\n"
                                                   "2. Leave the bunker\n"
                                                   "Enter your choice (1-2): ")
                            if choicesurvive2 == "1":
                                print("it was a trap by the aliens your now dead")
                                print("Mission failed")
                                break
                            elif choicesurvive2 == "2":
                                print("Your rescue team is now here for you, you survived mission complete!")
                                break
                            else:
                                print("\nInvalid choice. Please enter 1 or 2. ")
                    elif choicesurvuve1 == "2":
                        print("You couldn't out run them now your dead")
                        print("Mission failed")
                        break
                    else:
                        print("\nInvalid choice. Please enter 1 or 2. ")
                break
            else:
                print("\nInvalid choice. Please enter 1 or 2.")
        break


    else:
        print("\nInvalid choice. Please enter a number between 1 and 5.")


