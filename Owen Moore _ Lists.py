#Owen Moore
#March 28, 2017
#Unit 5 Lesson 1, Lists

#Intro
print("Oh no! \n",
      "The fairy princess has lost her sacred muffin!",)
input()

print("The evil villian, Maltheus the Destroyer, is the one who has stolen her muffin. \n")

input()

print("The princess has now tasked you to retrieve her muffin!")

input()

print("You are handed a cursed elven sword that traps a person's soul inside, \n",
      "and you are handed a golden shield that is fireproof.")

input()

print("You must go immidiately! \n")

inventory = ["elven sword", "shield"]

print("You leave the castle, and head out on your own!\n")

print("As you head out to go to Maltheus, you realize that you have no clue where he lives! \n")

print("You turn around to go back to the castle to ask where Maltheus lives... ")

input()

print("But when you turn around the castle is not there!")

input()

print("You then remember that the fairy princess's castle moves, and so it makes sense that it is gone. \n")

input()

print("To find out where Maltheus lives you travel to the local bar and inn to stay the night. \n")

input()

print("As you enter the inn you see beautiful contemparary designs of a newly renovated building. \n",
      "It is beautiful!")
      
input()

print("'Hello there!' \n")

input()

print("You turn around and standing behind you is a short and stuby dwarf. \n")

input()

print(" 'The name's Jarred. \n",
      "I am the inn keeper here and proud owner of this fine establishment. \n",
      "It's also newly renovated!' \n")

input()
      
print("You look at him bewildered, and think to yourself that for such a stubby guy, he has so much energy'.")

input()

name = input("'What is your name?' (choose a name for yourself) \n")

input()

print(" 'Alrighty then, how may I help you ", name,"?'")

input()

print("You tell him all about your quest, and how you are trying to find out where Maltheus lives.")

input()

print(" 'Oh! I know Maltheus! \n",
      "He's actually a pretty good guy when he's not being evil.' ")

input()

print("'Why don't you go to the bar and grab a drink. \n",
      "While you are there you can grab a GPS from my bartender, \n",
      "the GPS already has his adress plugged in. I was just there the other day at a party!'")

input()

print("You head over to the bar and see Jarred standing behind the bar, except he has a beret.")

input()

print("You come up to the bar and say, \n"
      "'Hey Jarred! I thought that you were the inn keeper.'")

input()

print(" 'Hello ", name, "you must be thinking of my brother. \n",
      "My name Gustav my brother told me about you. You're looking for the GPS. \n",
      "Here, I'll go get it for you.' \n",
      "He bends to grab the GPS from under the table. \n")

input()

print("Okay, here you go.\n",
      "He hands you the GPS.")

inventory.append("GPS")
    
input()

print("Congratulations! \n",
      "You now have ", len(inventory), "items in your possesion! \n")

input()

print("You put your GPS in your bag and turn back to Gustav. \n",
      "'Would you like a drink while you are here?' asks Gustav.")

input()

anSwr = input("Enter yes or no. (make sure to spell exactly how it is shown) \n")

if anSwr == "yes":
    print("'Okay here you go.' Gustav hands you a drink.")
else:
    print("'Okay, that's fine. I am here if you need one.'")

print("You thank Gustav for the help and go sit at a table by the fireplace.")

input()

print("As you sit down at the table, \n",
      "a scrawny elf holding a pot of steamy oatmeal comes up to you.")

input()

print("'Is it alright if I sit with you?'")

input()

eLf = input(""" You consider your options.
          Do you want this weird scrawny guy to sit with you?
          yes or no (enter exactly as shown)
          """)
if eLf == "yes":
    print("You tell him yes and he sits down across from you with is oatmeal. \n",\
          "'So,' hes says to you. 'Are you interested in mexican salamanders?'")

    input()

    print("'What?' you ask him confused. \n")

    input()

    print("'You know axolotls, commonly known as the mexican salamander.'")

    input()

    print("You have no idea what he is talking about, and stare at him blankly.")

    input()

    print("'Well, anyway... Mexican salamanders are pretty awsome! \n"
          "I have a few with me if you want one.'")

    axoLotl = input("""Do you want an axolotl?
                       If yes, enter yes. Else enter no
                      (make sure it is typed exactly as it is shown)
                      """)
    if axoLotl == "yes":
        print("He hand you an axolotl and then runs away with out looking back.")

        inventory.append("axolotl")

        print("Congratulations you now have an axolotl in your posession!\n",
              "You now have ", len(invetory),"items.")
        input()

        print("Well, that was weird, you think to yourself.")

        input()

        print("After sitting by the warm fire for a while\n",
              "you stand and go back to the front desk in the inn to get a room for the night.")

        input()

        print("You wait at the front desk for Jarred but he doesn't come. \n",
              "There is a little bell which you aggressively ring the bell.")

        input()

        print("Out of the back room come Jarred but he has a blond wig \n",
              "that is clearly taped to his head.")

        input()

        print("'Hi '", name,"! My brothers told me all about you and your quest. \n",
              "Would you like a room for the night?")

        input()

        print("You tell him yes.")

        input()

        print("'Okay, cool. All I need is a form of payment. \n",
              "Unfortunately we only accept payment in Mexican Salamanders. \n",
              "Do you happen to have any?'")
        input()

        print("You tell him yes and hand him it.")

        input()

        inventory.remove("axolotl")

        print("'Okay here you go!' \n",
              "He hand you a room key.")

        iventory.append("room key")

        print("You now have a room key!")

        input()

        print("You head up to your room and fall asleep for the night.\n")
        
        input("Press Enter To Exit. \n")
        
    else:
        print("He stands and throws his steamy oatmeal at your face!\n",
              "As it its your face you realize that you are allergic to oatmeal!\n"
              "You then pass out from the oatmeal, and your quest is over.")

        input("Press enter key to exit.")
else:
    print("You tell him no and he walks away in a depressed manner. \n",
          "Unfortunately for you he had a few friends who are way bigger and stronger than he. \n",
          "They chase you all the way out of the tavern and into the forrest where you proceed to get lost.\n",
          "You became so lost that you live the rest of your years in the forrest until you grow old and die.")

    input("Press Enter Key to Exit.")


