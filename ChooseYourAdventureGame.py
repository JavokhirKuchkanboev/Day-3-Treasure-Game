print("Welcome to the adventure game! \n Your mission is to find a treasure.")
right_left = input("You are at a crossroad. \nWould you like to go right or left? \n Type r/l")
if right_left.lower() == "l":
    swim_wait = input("You have a lake in front \n Boat may come. Do you Wait or Swim \n Type w/s")
    if swim_wait.lower() == "w":
        door_color = input("you have arrived one building with several doors \n Which color do you choose? \n Type "
                           "r for red or b for blue or y for yellow \n ")
        if door_color.lower() == "y":
            print("You Found the treasure")
        elif door_color.lower() == "r":
            print("You are burned by fire")
        elif door_color.lower() == "b":
            print("You are eaten by beast")

        else: print("You don't have any door yet")

    else: print("Attacked by Crocodile \n Game Over")

else: print("You Fall into a hole. \n Game Over!")