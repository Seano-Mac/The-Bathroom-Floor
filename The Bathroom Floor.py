# The Bathroom Floor - A text-based escape room made by Seano Mac in February 2024
# www.git-hub.com/Seano-Mac
# Have fun playing.

import sys                    # import the libraries required for the typewriter effect
from time import sleep

# Set the dependencies for the game to default
 
    # Set all of the rooms as unvisited for roomchange feature
 
has_visited_bathroom = False
has_visited_landing = False
has_visited_bedroom = False
has_visited_hall = False
has_visited_living_room = False
has_visited_kitchen = False
has_visited_garden = False
has_visited_car = False
 
    # Set all of the items as not in your possession
 
        # Bathroom
 
has_screwdriver = False
has_toilet_roll = False
has_bathroom_key = False

        # Landing
        
has_back_door_key = False
has_tin_foil = False

        # Bedroom

has_hair_pin = False
has_tv_remote = False

        # Hall
        
has_batteries = False

        # Living Room
        
has_gate_key = False

        # Kitchen

has_car_keys = False
has_sandwich = False
        
        # Garden
        
# None Required
        
        # Car
        
# None Required
 
 
    # Set the variables for the actions to default
 
        # Bathroom
 
has_bathroom_key_fallen = False
is_bathroom_door_locked = True
is_toilet_roll_under_door = False
is_key_on_toilet_roll = False

        # Landing
        
is_landing_table_locked = True

        # Bedroom
        
is_bedroom_light_on = False
are_wardrobe_doors_open = True

        # Hall

is_kitchen_door_locked = True

        # Living Room
        
is_tv_on = False
has_combination = False
        
        # Kitchen
        
is_back_door_locked = True
        
        # Garden
        
has_moved_rock = False
stood_in_poop = False
is_gate_open = False
        
        # Car
        
# None Required
        
# Code the Intro

    # Artwork

def print_art():
    print("\n                                                             ")
    print("                 #####   #   #  #####                          ")
    print("                   #     #   #  #                              ")
    print("                   #     #####  ###                            ")
    print("                   #     #   #  #                              ")
    print("                   #     #   #  #####                          ")       
    print("                                                               ")
    print(" ####    ###   #####  #   #  ####    ###    ###   #   #        ")
    print(" #   #  #   #    #    #   #  #   #  #   #  #   #  ## ##        ")
    print(" ####   #####    #    #####  ####   #   #  #   #  # # #        ")
    print(" #   #  #   #    #    #   #  #   #  #   #  #   #  #   #        ")
    print(" ####   #   #    #    #   #  #   #   ###    ###   #   #        ")
    print("                                                               ")
    print("           #####  #       ###    ###   ####                    ")
    print("           #      #      #   #  #   #  #   #                   ")
    print("           ###    #      #   #  #   #  ####                    ")
    print("           #      #      #   #  #   #  #   #                   ")
    print("           #      #####   ###    ###   #   #                   ")
    print("                                                               ")
    print("                                                               ")
    
    # Typewriter effect
    
def typewriter():
    global line_1
    for x in line_1:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.1)
        
    # Intro text
    
def intro(): # Set the function for the intro
    global line_1 # access the global variables required to run the funcion
    print_art() # print the ascii art and large font text
    line_1 = "\n\nWelcome to The Bathroom Floor.  A text-based escape room made by Sean McDonnell in February 2024."
    typewriter()              # and print a short introduction message.
    play = input("\nWould you like to play? (yes/no): ") # ask the user if they would like to play
    if play == "yes" or play == "YES" or play == "Yes": # if yes
        line_1 = "\n\nEnter X in the menu to quit the game, or enter R to change rooms.\n\n\nThe Bathroom Floor.\n\n"
        typewriter()
        Bathroom() # start game
    else:
        quit
        
#  ####    #       ###    ####  #####   ####
#  #   #   #      #   #  #      #      #
#  ####    #      #####  #      ###     ###
#  #       #      #   #  #      #          #
#  #       #####  #   #   ####  #####  ####

# Set the functions for the places
 
def Bathroom (): # When entering the Bathroom
    global line_1
    global has_visited_bathroom # access the global variables required to run the function
    if has_visited_bathroom == False: # and check if it is your first time here to decide whether to include the intro speech.
        line_1 = "\nYou wake up and look around.  You appear to be in a bathroom... How did you get here?  You stand up and check your surroundings...\nThe door is closed.  There is a toilet with some toilet roll, a cabinet, a sink and a bath.\n" # If it is your first time here, print the intro speech
        typewriter ()# add the code for the typewriter
        has_visited_bathroom = True # change the variable to say that you have now visited the bathroom so that you can travel here
        print_bathroom_options() # then print the Bathroom menu.
    else: # If it is not your first time here
        line_1 = "\nYou are in the bathroom...\n" # Print the default message for the Bathroom
        typewriter() # use the typewriter function for the typewriter effect
        print_bathroom_options() # Then print the Bathroom menu.
   
def Landing(): # When entering the Landing
    global line_1
    global has_visited_landing # access the global variables required to run the function
    if has_visited_landing == False: #  and check to see if it is your first time here to decide whether to include the intro speech.
        line_1 = "\nYou walk out onto the Landing and have a look around.  There is a table with a vase on it, and a rug on the floor.  It's a bit dark, but you can make out the entrance to a Bedroom on your left, and a window at the end of the Landing by the stairs.\n" # If it is your first time here, include the intro speech
        typewriter() # use the typewriter function for the typewriter effect
        has_visited_landing = True # change the variable to say that we have now visited the Landing
        print_landing_options() # then print the Landing menu.
    else: # If it is not your first time here
        line_1 = "\nYou enter the Landing...\n" # print the default message for the Landing
        typewriter() # use the typewriter function for the typewriter effect
        print_landing_options() # and print the Landing menu.
   
def Bedroom(): # When entering the Bedroom
    global line_1
    global has_visited_bedroom # access the global variables required to run the function
    if has_visited_bedroom == False: # and check to see if it is your first time here to decide whether to include the intro speech.
        line_1 = "\nYou walk into the Bedroom.  It's nothing out of the ordrinary.  There is a dresser with a mirror above it straight ahead, a wardrobe to the left with the doors open, and a bed to the right.\n" # If it is your first time here, print the intro speech
        typewriter() # use the typewriter function for the typewriter effect
        has_visited_bedroom = True # change the variable to say that you have now visited the Bedroom so that you can travel here.
        print_bedroom_options() # then print the Bedroom menu.
    else: # If it is not your first time here
        line_1 = "\nYou enter the Bedroom...\n"  # Print the default message for the Bedroom
        typewriter() # use the typewriter function for the typewriter effect
        print_bedroom_options() # and print the Bedroom menu.

def Hall(): # When entering the Hallway
    global line_1
    global has_visited_hall # access the global variables required to run the function
    if has_visited_hall == False: # and check to see if it if your first time here to decide whether to include the intro speech.
        line_1 = "\nYou walk down the stairs, and into the Hallway.  There are 3 doors. There is a painting on the wall, and a battery-powered radio on a small side table.\n" # If it is, then print the intro message
        typewriter() # use the typewriter function for the typewriter effect
        has_visited_hall = True # change the variable to say that you have now visitied the Hallway so that you can travel here
        print_hall_options() # then print the Hallway menu.
    else: # If it is your first time here
        line_1 = "\nYou enter the Hallway...\n" # Print the default messag for the Hallway
        typewriter() # use the typewriter function for the typewriter effect
        print_hall_options() # then return to the Hallway menu.
        
def Living_Room(): # When entering the Living Room
    global line_1
    global has_visited_living_room # access the global variables required to run the function
    if has_visited_living_room == False: # and check to see if it is your first itme here to decide whether to include the intro speech.
        line_1 = "\nYou walk into the Living Room.  There is a TV, a coffee table, a couch, and a window.\n" # If it is, print the intro speech
        typewriter() # use the typewriter function for the typewriter effect
        has_visited_living_room = True # change the variable to say that you have now visited the Living Room so that you can now travel here
        print_living_room_options() # then print the Living Room menu.
    else: # If it is your first time here
        line_1 = "\nYou enter the Living Room...\n" # print the default message for the Living Room
        typewriter() # use the typewriter function for the typewriter effect
        print_living_room_options() # then print the Living Room menu.
    
def Kitchen(): # When entering the Kitchen
    global line_1
    global has_visited_kitchen # access the global variables required to run the function
    if has_visited_kitchen == False: # and check to see if it is your first time here to decide whether to include the intro speech.
        line_1 = "\nYou walk into the Kitchen.  The back door is locked with a large bronze padlock, and there is a safe on the counter top.\n" # If it is, print the intro speech
        has_visited_kitchen = True # change the variable to say that you have now visited the Kitchen so that you can now travel here
        typewriter() # use the typewriter function for the typewriter effect
        print_kitchen_options() # then print the Kitchen menu
    else: # If it is your first time here
        line_1 = "\nYou enter the Kitchen...\n" # then print the default message for the Kitchen
        typewriter() # use the typewriter function for the typewriter effect
        print_kitchen_options() # then print the Kitchen menu
 
def Garden(): # When entering the Garden
    global line_1
    global has_visited_garden # access the global variables required to run the function
    if has_visited_garden == False: # and check to see if it is your first time here to decide whether to include the intro speech.
        line_1 = "\nYou come out into the Garden.  There is a car parked on the driveway.  There is long path with a rock on it which is fenced off with a large iron gate, and a lawn.\n" # If it is, print the intro speech
        typewriter() # use the typewriter function for the typewriter effect
        has_visited_garden = True # change the variable to say that you have now visited the Garden so that you can now travel here
        print_garden_options() # then print the Garden menu
    else: # If it is your first time here
        line_1 = "\nYou enter the Garden...\n" # then print the default message for the Garden
        typewriter() # use the typewriter function for the typewriter effect
        print_garden_options() # then print the Garden menu
  
def Car(): # When entering the Car
    global line_1
    global has_visited_car # access the global variables requierd to run the function
    if has_visited_car == False: # and check to see if it is your first time here to decide whether to include the intro speech.
        line_1 = "\nYou enter the Car.  It's finally time to leave this place and go home!\n" # If it is, print the intro speech
        typewriter() # use the typewriter function for the typewriter effect
        has_visited_car = True # change the variable to say that you have now visited the Garden so that you can now travel here
        print_car_options() # then print the Car menu.
    else: # If it is your first time here
        line_1 = "\nYou enter the Car...\n" # then print the default message for the Car
        typewriter() # use the typewriter function for the typewriter effect
        print_car_options() # then print the Car menu.
 
# Set the room change function
   
def room_change_check():
    global line_1
    global has_visited_bathroom
    global has_visited_landing
    global has_visited_bedroom
    global has_visited_hall
    global has_visited_living_room
    global has_visited_kitchen
    global has_visited_garden
    global has_visited_car    
    room = input("\n\nPlease enter the room you would like to travel to: ")
    room = room.lower()
    if room == "bathroom" and has_visited_bathroom == True:
        Bathroom()
    elif room == "landing" and has_visited_landing == True:
        Landing()
    elif room == "bedroom" and has_visited_bedroom == True:
        Bedroom()
    elif (room == "hall" or "hallway") and has_visited_hall == True:
        Hall()
    elif room == "living room" and has_visited_living_room == True:
        Living_Room()
    elif room == "kitchen" and has_visited_kitchen == True:
        Kitchen()
    elif room == "garden" and has_visited_garden == True:
        Garden()
    elif room == "car" and has_visited_car == True:
        Car()    
    else:
        line_1 = "\n\nYou cannot travel here.  If you are stuck, try Bathroom.\n\n"
        typewriter()
        room_change_check()

#  #   #  #####  #   #  #   #   ####
#  ## ##  #      ##  #  #   #  #
#  # # #  ###    # # #  #   #   ###
#  #   #  #      #  ##  #   #      #
#  #   #  #####  #   #   ###   ####
 
# Print the options for the places
 
def print_bathroom_options():
    global line_1 # access the global variables required to run the function
    line_1 = "\nWhat will you do?\n\n"
    typewriter() # use the typewriter function for the typewriter effect
    menu_choice = input("1 - Open the Bathroom Door\n2 - Check the Keyhole\n3 - Look under the door\n4 - Check the Bathroom Cabinet\n5 - Look out of the window\n6 - Look under the mat\n7 - Check the toilet\n8 - Look in the bath\n\nPlease enter a number: ")
    menu_choice = menu_choice.lower()
    if menu_choice == "1": # If the number entered is 1
        open_bathroom_door() # then open the Bathroom door.
    elif menu_choice == "2": # If the number entered is 2
        check_bathroom_keyhole() # then check the Bathroom keyhole.
    elif menu_choice == "3": # If the number entered is 3
        look_under_bathroom_door() # then look under the Bathroom door.
    elif menu_choice == "4": # If the number entered is 4
        check_bathroom_cabinet() # then check the Bathroom cabinet.
    elif menu_choice == "5": # if the menu choice is 5
        check_bathroom_window() # then check the Bathroom window.
    elif menu_choice == "6": # if the menu choice is 6
        check_bathroom_mat() # then check the Bathroom mat.
    elif menu_choice == "7": # If the number entered is 7
        check_toilet() # then check the toilet.
    elif menu_choice == "8": # If the numbeer entered is 8
        check_bath() # then check the bath.
    elif menu_choice == "r": # If the letter "r" is entered
        room_change_check() # then load the room change menu.
    elif menu_choice == "x": # if the letter x is entered
        exit_game() # then close the game
    else: # if anything else is entered
        print_bathroom_options() # return to the bathroom menu
            
def print_landing_options():
    global line_1 # access the global variables required to run the function
    line_1 = "\nWhat will you do?\n\n"
    typewriter() # use the typewriter function for the typewriter effect
    menu_choice = input("1 - Enter the Bathroom\n2 - Enter the Bedroom\n3 - Go downstairs\n4 - Check the table on the Landing\n5 - Check the vase on the table\n6 - Look out of the Landing window\n7 - Look underneath the rug\n\nPlease enter a number: ")
    menu_choice = menu_choice.lower()
    if menu_choice == "1": # If the number entered is 1
        Bathroom() # then enter the Bathroom.
    elif menu_choice == "2": # If the number entered is 2
        Bedroom() # then enter the Bedroom.
    elif menu_choice == "3": # If the number entered is 3
        Hall() # then go downstairs into the Hallway.
    elif menu_choice == "4": # If the number entered is 4
        check_landing_table() # then check the Landing table.
    elif menu_choice == "5": # If the number entered is 5
        check_vase() # then check the vase on the table.
    elif menu_choice == "6": # If the number entered is 6
        check_landing_window() # then look out of the Landing window.
    elif menu_choice == "7": # If the number entered is 7
        check_landing_rug() # then check underneath the Landing rug.
    elif menu_choice == "r": # If the letter "r" is entered
        room_change_check() # then load the room change menu.
    elif menu_choice == "x": # if the letter x is entered
        exit_game() # then close the game
    else: # If anything else is entered
        print_landing_options() # return to the Landing menu.
        
def print_bedroom_options():
    global line_1 # access the global variables required to run the function
    line_1 = "\nWhat will you do?\n\n"
    typewriter() # use the typewriter function for the typewriter effect
    menu_choice = input("1 - Enter the Landing\n2 - Check the bed\n3 - Check the mirror\n4 - Check the dresser\n5 - Check the wardrobe\n6 - Look out of the window\n\nPlease enter a number: ") # print the options, and let the user pick a number.
    menu_choice = menu_choice.lower()
    if menu_choice == "1": # If the number entered is 1
        Landing() # then enter the Landing.
    elif menu_choice == "2": # If the number entered is 2
        check_bed () # then check the bed.
    elif menu_choice == "3": # If the number entered is 3
        check_mirror() # then check the mirror.
    elif menu_choice == "4": # If the number entered is 4
        check_dresser() # then check the dresser.
    elif menu_choice == "5": # If the number entered is 5
        check_wardrobe() # then check the wardrobe.
    elif menu_choice == "6": # If the number entered is 6
        check_bedroom_window() # then check the bathroom window.
    elif menu_choice == "r": # If the letter "r" is entered
        room_change_check() # then load the room change menu.
    elif menu_choice == "x": # if the letter x is entered
        exit_game() # then close the game
    else: # If anything else is entered
        print_bedroom_options() # then return to the Bedroom menu.
        
def print_hall_options():
    global line_1 # access the global variables required to run the function
    line_1 = "\nWhat will you do?\n\n"
    typewriter() # use the typewriter function for the typewriter effect
    menu_choice = input("1 - Go Upstairs\n2 - Check the front door\n3 - Enter the Living Room\n4 - Enter the Kitchen\n5 - Check the painting\n6 - Check the radio\n\nPlease enter a number: ")
    menu_choice = menu_choice.lower()
    if menu_choice == "1": # If the number entered is 1
        Landing() # then enter the Landing.
    elif menu_choice == "2": # If the number entered is 2
        check_front_door() # then check the front door.
    elif menu_choice == "3": # If the number entered is 3
        Living_Room() # then enter the living room.
    elif menu_choice == "4": # If the number entered is 4
        check_kitchen_door() # then check the kitchen door.
    elif menu_choice == "5": # If the number entered is 5
        check_painting() # then check the painting.
    elif menu_choice == "6": # If the number entered is 6
        check_radio() # then check the radio.
    elif menu_choice == "r": # If the letter "r" is entered
        room_change_check() # then load the room change menu.
    elif menu_choice == "x": # if the letter x is entered
        exit_game() # then close the game
    else: # If anything else is entered
        print_hall_options() # then return to the Hallway menu.    
            
def print_living_room_options(): # When entering the living room
    global line_1 # access the global variables required to run the function
    line_1 = "\nWhat will you do?\n\n"
    typewriter() # use the typewriter function for the typewriter effect
    menu_choice = input("1 - Enter the Hallway\n2 - Check the Living Room window\n3 - Check the TV\n4 - Check the couch\n5 - Check the coffee table\n\nPlease enter a number: ")
    menu_choice = menu_choice.lower()
    if menu_choice == "1": # If the number entered is 1
        Hall() # then enter the Hallway.
    elif menu_choice == "2": # If the number entered is 2
        check_living_room_window() # then look out of the Living Room window.
    elif menu_choice == "3": # If the number entered is 3
        check_tv() # then check the TV.
    elif menu_choice == "4": # If the number entered is 4
        check_couch() # then check the couch.
    elif menu_choice == "5": # If the number entered is 5
        check_cofee_table() # then check the coffee table.
    elif menu_choice == "r": # If the letter "r" is entered
        room_change_check() # then load the room change menu.
    elif menu_choice == "x": # if the letter x is entered
        exit_game() # then close the game
    else: # If anything else is entered
        print_living_room_options() # Then return to the living room options
    
    
def print_kitchen_options(): # When entering the Kitchen
    global line_1 # access the global variables required to run the function
    line_1 = "\nWhat will you do?\n\n"
    typewriter() # use the typewriter function for the typewriter effect
    menu_choice = input("1 - Enter the Hallway\n2 - Check the Kitchen window\n3 - Enter the Garden\n4 - Check the safe\n5 - Check the fridge\n\nPlease enter a number: ") # print the options and allow the player to enter a number.
    menu_choice = menu_choice.lower()
    if menu_choice == "1": # If the number entered is 1
        Hall() # then enter the Hallway.
    elif menu_choice == "2": # If the number entered is 2
        check_kitchen_window() # then check the Kitchen window.
    elif menu_choice == "3": # If the number entered is 3
        check_back_door() # then check the back door.
    elif menu_choice == "4": # If the number entered is 4
        check_safe() # then check the safe.
    elif menu_choice == "5": # If the number entered is 5
        check_fridge() # then check the fridge.
    elif menu_choice == "r": # If the letter "r" is entered
        room_change_check() # then load the room change menu.
    elif menu_choice == "x": # if the letter x is entered
        exit_game() # then close the game
    else: # If anything else is entered
        print_kitchen_options() # then return to the Kitchen menu.
        
def print_garden_options():
    global line_1 # access the global variables required to run the function
    line_1 = "\nWhat will you do?\n\n"
    typewriter() # use the typewriter function for the typewriter effect
    menu_choice = input("1 - Enter Kitchen\n2 - Check the lawn\n3 - Check the gate\n4 - Check the rock\n5 - Get in the car\n\nPlease enter a number: ")
    menu_choice = menu_choice.lower()
    if menu_choice == "1": # If the number entered is 1
        Kitchen() # then enter the kitchen.
    elif menu_choice == "2": # If the number entered is 2
        check_lawn() # then check the lawn.
    elif menu_choice == "3": # If the number entered is 3
        check_iron_gate() # then check the gate.
    elif menu_choice == "4": # If the number entered is 4
        check_rock() # then check the rock.
    elif menu_choice == "5": # If the number entered is 5
        check_car_door() # then check the car door.
    elif menu_choice == "r": # If the letter "r" is entered
        room_change_check() # then load the room change menu.
    elif menu_choice == "x": # if the letter x is entered
        exit_game() # then close the game
    else: # If anything else is entered
        print_garden_options() # then return to the garden menu.
    
def print_car_options():
    global line_1 # access the global variables required to run the function
    line_1 = "\nWhat will you do?\n\n"
    typewriter() # use the typewriter function for the typewriter effect
    menu_choice = input("1 - Get out of the car\n2 - Start the car\n\nPlease enter a number: ")
    menu_choice = menu_choice.lower()
    if menu_choice == "1": # If the number entered is 1
        Garden() # Exit the car into the garden
    elif menu_choice == "2": # If the number entered is 2
        start_car() # then start the car.
    elif menu_choice == "r": # If the letter "r" is entered
        room_change_check() # then load the room change menu.
    elif menu_choice == "x": # if the letter x is entered
        exit_game() # then close the game
    else: # if anything else is entered
        print_car_options() # then return to the car menu

#   ###    ####  #####  #####   ###   #   #   ####
#  #   #  #        #      #    #   #  ##  #  #
#  #####  #        #      #    #   #  # # #   ###
#  #   #  #        #      #    #   #  #  ##      #
#  #   #   ####    #    #####   ###   #   #  ####

# Set the functions for the actions
   
    # Bathroom    
    
def open_bathroom_door(): #1 when checking the bathroom door
    global is_bathroom_door_locked # access the globals requierd to run the funcion
    global line_1
    if is_bathroom_door_locked == True: # Check to see if the door is locked
        line_1 = "\nThe door is locked.\n" # If it is, print a message to say that
        typewriter() # use the typewriter function for the typewriter effect
        print_bathroom_options() # Then print the Bathroom menu again
    else: # If the door is unlocked
        line_1 = "\nYou open the door and leave the Bathroom.\n" # print a message to say that
        typewriter() # add the typewriter function for the typewriter effect 
        Landing() # Exit onto the Landing
 
def check_bathroom_keyhole(): #2 when checking the keyhole
    global line_1
    global has_bathroom_key
    global has_bathroom_key_fallen   # access the global variables required within the function
    global has_screwdriver
    global is_bathroom_door_locked
    if has_bathroom_key == False and has_bathroom_key_fallen == True:
        # If you don't have the key,  and it is not in the lock
        line_1 = "\nYou can see out into the landing.\n" # You will be able to see out of the keyhole
        typewriter() # add the typewriter function for the typewriter effect
        print_bathroom_options() # Now return to the Bathroom menu
    elif has_bathroom_key == False and has_bathroom_key_fallen == False and has_screwdriver == False: # If you don't have the key yet, and it is still in the lock
        line_1 = "\nYou can see a key on the other side.\n" # You will be able to see it through the keyhole
        typewriter() # add the typewriter function for the typewriter effect
        print_bathroom_options() # Now return to the Bathroom menu
    elif has_bathroom_key == False and has_bathroom_key_fallen == False and has_screwdriver == True: # If you have the screwdriver
        line_1 = "\nYou push the key out of keyhole using the screwdriver.  It falls on the floor on the other side.\n" # You can push the Bathroom Key out on the other side, but make sure you have the toilet roll ready
        typewriter() # add the typewriter function for the typewriter effect
        has_bathroom_key_fallen = True # Change the parameter to say that the bathroom key has fallen
        print_bathroom_options()
    else:# If you have the Bathroom key
        line_1 = "\nNice! You have unlocked the door!\n" # You can unlock the bathroom door
        typewriter() # add the typewriter function for the typewriter effect
        is_bathroom_door_locked = False # This will now set the Bathroom door as unlocked
        print_bathroom_options() # And return to the Bathroom Menu
   
def look_under_bathroom_door(): #3
    global line_1
    global is_toilet_roll_under_door
    global has_bathroom_key_fallen # Access the global variables required within the function
    global has_bathroom_key
    
    if has_toilet_roll == False and has_bathroom_key_fallen == True: # If you don't have the toilet roll under the door, and you have already pushed the key out
        line_1 = "\nThe key has fallen with no way to catch it.  Now you will never escape.  Game Over.\n" # There is no way to complete the game, and you have lost.
        typewriter() # add the typewriter function for the typewriter effect
        exit_game() # This exits the game
    elif is_toilet_roll_under_door == False and has_toilet_roll == True: # If the toilet roll is not under the door, but you have toilet roll
        line_1 = "\nYou take the toilet roll from out of your pocket, and place it under the door\n" # place some of the toilet roll under the door
        typewriter() # add the typewriter function for the typewriter effect
        is_toilet_roll_under_door = True # change the variable to say the toilet roll is under the door
        print_bathroom_options() # and return to the Bathroom menu.
    elif is_toilet_roll_under_door == True and has_bathroom_key_fallen == True and has_bathroom_key == False: #If the toilet roll is under the door, the key has fallen, and you do not have it yet
        line_1 = "\nYou pull the toilet roll from back under the door, and retreive the fallen key.  Well Done!\n" #Then retrieve the key
        typewriter() # add the typewriter function for the typewriter effect
        has_bathroom_key = True # change the variable to say you now have the key in your posession
        print_bathroom_options() # and return to the Bathroom Menu.
    else: # For all other parameters
        line_1 = "\nYou look under the bathroom door.  You can't really see anything\n" # print the default message
        typewriter() # add the typewriter function for the typewriter effect
        print_bathroom_options() # then return to the Bathroom menu.
   
def check_bathroom_cabinet(): #4 When checking the Bathroom cabinet
    global line_1
    global has_screwdriver # access the global variables required to run the function.
    if has_screwdriver == False: # If you don't have the screwdriver yet
        line_1 ="\nYou look in the Bathroom cabinet.  There are some toiletries and a screwdriver.  You take the screwdriver and put it in your pocket.\n" # then take the screwdriver
        typewriter() # add the typewriter function for the typewriter effect
        has_screwdriver = True # change the variable to say the screwdriver is now in your possession
        print_bathroom_options() # and return to the Bathroom menu.
    else: # If you do have the screwdriver already
        line_1 = "\nYou look in the Bathroom cabinet.  There are some toiletries, but none of them are any use to you right now.\n" # print the default message
        typewriter() # add the typewriter function for the typewriter effect
        print_bathroom_options() # then return to the Bathroom menu.
 
def check_bathroom_window(): #5 when checking the window
    global line_1 # access the global variables required to run the function
    line_1 = "\nThe window is frosted, you cant really see outside.  It looks like it's night time.\n" # Print the default message for the Bathroom window
    typewriter() # add the typewriter function for the typewriter effect
    print_bathroom_options() # then return to the Bathroom menu.
   
 
def check_bathroom_mat(): #6 when checking the mat
    global line_1 # access the global variable required to run the function
    line_1 = "\nThere is nothing there.\n" # Print the default message for the Bathroom mat
    typewriter() # add the typewriter function for the typewriter effect
    print_bathroom_options() # then return to the bathroom menu.
 
def check_toilet(): #7 when checking the toilet
    global line_1
    global has_toilet_roll # Access the global variables necessary to run the function
    if has_toilet_roll == False: # and check to see if you already have toilet roll.
        line_1 = "\nYou take a few sheets of toilet roll fold them up, and put them in your pocket.\n" # If you dont have any, take some
        typewriter() # add the typewriter function for the typewriter effect
        has_toilet_roll = True # change the variale to say that you have it now
        print_bathroom_options() # then return to the Bathroom menu.
    else: # If you do already have the toilet roll
        line_1 = "\nWhy do you want to check again? Do you have some kind of a thing about toilets?!\n" # print the default message for the toilet
        typewriter() # add the typewriter function for the typewriter effect
        print_bathroom_options() # then return to the Bathroom menu.
 
 
def check_bath(): #8 when checking the bath
        global line_1 # access the global variables required for running the function
        line_1 = "\nYou check the bath.  There is nothing of any interest in here\n" # Print the default message for the bath
        typewriter() # add the typewriter function for the typewriter effect
        print_bathroom_options() # then return tothe Bathroom menu.
        
    # Landing
    
#1 will enter the bathroom
#2 will enter the bedroom
#3 will enter the hallway
		
def check_landing_table(): #4 when checking the landing table
    global line_1
    global is_landing_table_locked # access the global variables required for running the function
    global has_hair_pin
    global has_back_door_key
    if is_landing_table_locked == True and has_hair_pin == False: # If the drawer is locked and you don't yet have the hair pin
        line_1 = "\nThere is a vase on top of the table and a drawer on the front of it.  You try the drawer, but it is locked.  Maybe you can get it open with something?\n" # you cannot unlock the drawer yet
        typewriter() # add the typewriter function for the typewriter effect
        print_landing_options() # so return to landing menu
    elif is_landing_table_locked == True and has_hair_pin == True: # if the drawer is locked and you do have the hairpin
        line_1 = "\nYou use the hair pin to pick the lock\n" # use the hairpin to unlock the drawer
        typewriter() # add the typewriter function for the typewriter effect
        is_landing_table_locked = False # change the variable to mark the drawer as unlocked
        print_landing_options() # then print the landing options.
    elif is_landing_table_locked == False and has_back_door_key == False: # if the table is unlocked, and you havent yet taken the back door key
        line_1 = "\nYou open the draw and find a large bronze key.  You take it with you and close the drawer\n" # take the back door key from the drawer
        typewriter() # add the typewriter function for the typewriter effect
        has_back_door_key = True # change the variable to say we now have the back door key
        print_landing_options() # then return to the Landing menu.
    else: # If the table is unlocked and you have the key already
        line_1 = "\nThere is a vase on the top of the table and a drawer on the front of it, but the drawer is empty.\n"
        typewriter() # add the typewriter function for the typewriter effect
        print_landing_options() # then return to the Landing menu.
 
def check_vase(): #5 when checkin the vase
    global line_1 # access the global variable required for running the function
    line_1 = "\nThere is a vase on the table with some flowers in it.  They smell lovely\n" # Print the default message for the vase
    typewriter() # add the typewriter function for the typewriter effect
    print_landing_options() # then return to the Landing menu.
    
def check_landing_window(): #6 when checking the landing window
    global line_1 # access the global variables required for running the function
    line_1 = "\nYou look out of the landing window.  It's dark, and there is a treeline a few feet away from the window.\n" # Print the default message for the Landing window
    typewriter() # add the typewriter function for the typewriter effect
    print_landing_options() # then return to the Landing menu.
    
def check_landing_rug(): #7 when checking the landing rug
    global line_1
    global has_tin_foil # Access the global variable required for the function
    if has_tin_foil == False: # If you don't already have the tin foil
        line_1 = "\nYou find a sheet of tin foil underneath the rug.  This may come in handy.  You decide to take it with you.\n" # you take the tin foil from underneath the rug
        typewriter() # add the typewriter function for the typewriter effect
        has_tin_foil = True # change the variable to say you now have the tin foil
        print_landing_options() # and return to the Landing menu.
    else: # If you already have the tin foil
        line_1 = "\nYou already checked here.  Did you think something was going to magically appear?\n" # print the default message for the rug
        typewriter() # add the typewriter function for the typewriter effect
        print_landing_options() # then return to the Landing menu.
        
        
        # Bedroom
        
#1 will be to enter Landing
        
def check_bed(): #2 When checking the bed
    global line_1
    global has_tv_remote # Access the globals variable required to run the function.
    if has_tv_remote == False: # If you don't already have the TV remote
        line_1 = "\nYou find a remote control in the bed.  It could be useful, so you bring it with you.\n" # you take the tv remote with you
        typewriter() # add the typewriter function for the typewriter effect
        has_tv_remote = True # change the variable to say you now have the tin foil
        print_bedroom_options() # then return to the Bedroom menu.
    else: # If you do already have the TV remote
        line_1 = "\nYou already checked here.  I hope you weren't planning on snoozing off, you need to get out of here!\n" # Print the default message for the bed
        typewriter() # add the typewriter function for the typewriter effect
        print_bedroom_options() # and return to the Bedroom menu.
        
def check_mirror(): #3 When checking the mirror
    global line_1 # access the global variables required to run the function
    line_1 = "\nYou look rough.  Maybe you should concentrate on getting out of here instead of checking yourself out in the mirror.\n" # print the default message for the mirror
    typewriter() # add the typewriter function for the typewriter effect
    print_bedroom_options() # and return to the bedroom menu
    
def check_dresser(): #4 When checking the dresser
    global line_1
    global is_bedroom_light_on # Access the global variables required to run the function
    global has_hair_pin
    if is_bedroom_light_on == False: # If the light is off
        line_1 = "\nIt's dark, but it doesn't look like there is anything on here.\n" # You won't be able to see the hair pin, so print this message
        typewriter() # add the typewriter function for the typewriter effect
        print_bedroom_options() # and return to the bedroom menu.
    elif is_bedroom_light_on == True and has_hair_pin == False: # If the light is on, and you don't have the hair pin yet
        line_1 = "\nThere is a hair pin on here.  You take it with you\n" # take the hair pin with you
        typewriter() # add the typewriter function for the typewriter effect
        has_hair_pin = True # change the variable to say you now have the hair pin
        print_bedroom_options() # then return to the Bedroom menu.
    else: # For all other parameters
        line_1 = "\nThere is nothing on here.\n" # print the default message for the dresser
        typewriter() # add the typewriter function for the typewriter effect
        print_bedroom_options() # then return to the Bedroom menu.
        
def check_wardrobe(): #5 When checking the wardrobe
    global line_1
    global is_bedroom_light_on # access the global variables required to run the function.
    global are_wardrobe_doors_open
    if are_wardrobe_doors_open == True: # If the wardrobe doors are open
        line_1 = "\nThere wardrobe is empty.  You close the doors.\n" # you won't be able to see the light switch, so close the doors
        typewriter() # add the typewriter function for the typewriter effect
        are_wardrobe_doors_open = False # change the variable to mark the wardrobe doors as closed
        print_bedroom_options() # then return to the Bedroom menu.
    elif are_wardrobe_doors_open == False and is_bedroom_light_on == False: # If the wardrobe doors are shut, and the light is still off
        line_1 = "\nYou find a light switch behind where the door was.  You turn it on.  Its much brighter in here now.\n" # turn the light switch on
        typewriter() # add the typewriter function for the typewriter effect
        is_bedroom_light_on = True # change the variable to mark the bedroom light on
        print_bedroom_options() # then return to the Bedroom menu.
    else: # For all other parameters
        line_1 = "\nIt's just a wardrobe.  Whats your obsession with it?  Do you work for the Antiques Roadshow or something?\n" # print the default message for the wardrobe
        typewriter() # add the typewriter function for the typewriter effect
        print_bedroom_options() # then return to the Bedroom menu.
        
def check_bedroom_window(): #6 When checking the Bedroom window
    global line_1 # access the global variable required to run the function
    line_1 = "\nYou look out of the window.  There is a car parked outside.  You should try and find the keys so you can get away from here.\n" # print the default message for the Bedroom window
    typewriter() # add the typewriter function for the typewriter effect
    print_bedroom_options() # then return to the Bedroom menu
        
        #Hall
        
#1 Will be to enter the Landing

def check_front_door(): #2 When checking the front door
    global line_1 # access the global variable required to run the function
    line_1 = "\nThere are nails coming through the front door from where it is boarded up outside.  What on earth is going on here?!\n" # print the default message for the front door
    typewriter() # add the typewriter function for the typewriter effect
    print_hall_options() # then return to the Hallway menu.
    
#3 Will be to enter the Living Room

def check_kitchen_door(): #4 When checking the kictchen door
    global is_tv_on
    global line_1 # access the global variables required to run the function
    if is_tv_on == False: # check if the tv is on yet, so you know the code yet.
        line_1 = "\nThe door is locked, and there is a keypad next to it.  I wonder what the code could be?\n" # if the TV is off print the default message for the Kitchen door
        typewriter() # add the typewriter function for the typewriter effect
        print_hall_options() # then return to the Hallway menu.
    else: # If the TV is on, and you have the code
        line_1 = "\nThere is a keypad next to the door.  You enter the code and open it.\n"
        typewriter() # add the typewriter function for the typewriter effect
        Kitchen() # then enter the kitchen
        
def check_painting(): #5 When checking the painting
    global line_1 # access the global variable required to run the function
    line_1 = "\nThere is a painting on the wall of a person who looks eerily like you. This is starting to get creepy...\n" # print the default message for the painting
    typewriter() # add the typewriter function for the typewriter effect
    print_hall_options() # then return to the Hallway menu

def check_radio(): #6 When checking the radio
    global has_batteries # access the global variable required to run the function.
    global line_1
    if has_batteries == False: # If you don't already have the batteries
        line_1 = "\nThe radio isn't working but there are two batteries in it.  You take them out and put them in your pocket\n" # take the batteries out of the radio
        typewriter() # add the typewriter function for the typewriter effect
        has_batteries = True # change the variable to say that you now have the batteries
        print_hall_options() # then return to the Hallway Menu.
    else: # If you have the batteries already
        line_1 = "\nIt's just an old radio.\n" # print the default message for the Radio
        typewriter() # add the typewriter function for the typewriter effect
        print_hall_options() # then return to the hallway menu
        
        # Living Room
        
#1 Will be enter the hallway

def check_living_room_window(): #2 When checking the Living Room window
    print("\nYou look out of the living room window.  There is a car parked on the drive, and a long road stretching off into the distance.\n") # print the default message for the window
    print_living_room_options() # then return to the living room menu.
    
def check_tv(): #3 When checking the tv
    global has_tv_remote
    global has_batteries
    global has_tin_foil # access the global variables required to run the function
    global is_tv_on
    global line_1
    if has_tv_remote == False: # If you do not yet have the TV remote
        line_1 = "\nThe TV is switched off.  The remote control doesn't seem to be anywhere nearby\n" # let the player know they need the remote control still
        typewriter() # add the typewriter function for the typewriter effect
        print_living_room_options() # then return to the living room menu.
    elif has_tv_remote == True and has_batteries == False: # If you have the remote but not the batteries
        line_1 = "\nThe Tv is switched off.  You have the remote control, but there are no batteries inside it\n" # let the player know they need the batteries still
        typewriter() # add the typewriter function for the typewriter effect
        print_living_room_options() # then return to the living room menu.
    elif has_tv_remote == True and has_batteries == True and has_tin_foil == False: # if you have the remote and batteries, but no tin foil
        line_1 = "\nThe TV is switched off.  You have the remote control, but the batteries are too small.  Maybe you can bridge the gap with something?\n" # let the player know they need the tin foil still
        typewriter() # add the typewriter function for the typewriter effect
        print_living_room_options() # then return to the living room menu.
    elif has_tv_remote == True and has_batteries == True and has_tin_foil == True and is_tv_on == False: # if you have all 3 items and the TV is off
        line_1 = "\nYou place the batteries in the TV Remote, and ball up some of the tin-foil to bridge the gap.  You press a button and the TV comes on.  There is a code displayed on the screen.  What could this be for?\n"
        typewriter() # add the typewriter function for the typewriter effect
        is_tv_on = True # change the variable to say the livint room is now on
        print_living_room_options() # then return to the living room menu.
    else: # for any other parameters
        line_1 = "\nIt's just a TV.  You haven't got time to watch it, you need to get out of here.\n" # print a default message
        typewriter() # add the typewriter function for the typewriter effect
        print_living_room_options() # then return to the living room menu.
        
def check_couch(): #4 When checking the couch
    global line_1
    global has_gate_key # access the global variable required to run the function.
    if has_gate_key == False: # If you do not already have the gate key
        line_1 = "\nYou find an iron key down one of the couch cushions.  Well you're not just going to leave it here are you?\n" # take the key with you
        typewriter() # add the typewriter function for the typewriter effect
        has_gate_key = True # change the variable to say that you now have the gate key
        print_living_room_options() # then return to the living room menu.
    else: # If you already have the gate key
        line_1 = "\nDon't even think about sitting down.\n" # print the default message for the couch
        typewriter() # add the typewriter function for the typewriter effect
        print_living_room_options() # then return to the Living Room menu.
        
def check_cofee_table(): #5 When checking the coffee table
    global is_tv_on
    global has_combination # access the global variables required to run the function.
    global line_1
    if is_tv_on == False: # If the TV is off
        line_1 = "\nIt doesn't look like there is anthing on here.\n" # then you cannot see the writing on the table
        typewriter() # add the typewriter function for the typewriter effect
        print_living_room_options() # So return to the Living Room menu.
    elif is_tv_on == True and has_combination == False: # If the TV is on, and you haven't yet read the combination
        line_1 = "\nThere is some writing on the table reflecting the light from the TV.  It says 'The combination is 47843'.\n" # then print the combination
        typewriter() # add the typewriter function for the typewriter effect
        has_combination = True # change the variable to say that you have now read the combination
        print_living_room_options() # then return to the Living Room menu.
    else: # If the tv is on, and you have already seen the combination
        line_1 = "\nThere is a combination written on the table, you should look around for somewhere to use it.\n" # print a default message for the coffee table
        typewriter() # add the typewriter function for the typewriter effect
        print_living_room_options() # then return to the Living Room menu.
            
        # Kitchen
        
#1 Will be enter the Hallway

def check_kitchen_window(): #2 When checking the Kitchen window
    global line_1 # access the global variables required to run the function
    line_1 = "\nYou look out of the kitchen window.  It's just fields for as far as the eye can see from this side.\n" # print a default message for the window
    typewriter() # add the typewriter function for the typewriter effect
    print_kitchen_options() # then return to the Kitchen Menu
    
def check_back_door(): #3 When checking the garden door
    global has_back_door_key
    global is_back_door_locked # access the global variables necessary to run the function
    global line_1
    if has_back_door_key == False: # If you do not yet have the back door key
        line_1 = "\nThe door is locked with a bronze padlock.\n" # tell the user the door is locked
        typewriter() # add the typewriter function for the typewriter effect
        print_kitchen_options() # then return to the kitchen menu.
    elif has_back_door_key == True and is_back_door_locked == True: # If you have the back door key but the door is locked
        line_1 = "\nYou unlock the padlock with the bronze key, take it off, and open the door to the garden\n" # unlock the door and go outside.
        typewriter() # add the typewriter function for the typewriter effect
        Garden()
    else: # if you have the back door key and the door is unlocked
        line_1 = "\nYou open the door to the Garden and go outside\n"
        typewriter() # add the typewriter function for the typewriter effect
        Garden() # then go outside into the garden

def check_safe(): #4 When checking the safe
    global has_combination
    global has_car_keys # access the global variables required to run the function.
    global line_1
    if has_combination == False: # If you don't yet have the combination
        line_1 = "\nYou're not going to get it open without the combination.  Who do you think you are?  The Lockpicking Lawyer?\n" # Print a message to let the player know they need the combination
        typewriter() # add the typewriter function for the typewriter effect
        print_kitchen_options() # then return to the Kitchen Menu.
    elif has_combination == True and has_car_keys == False: # If you have the combination, but have not yet got the car keys
        line_1 = "\nYou enter the combination in the safe.  Great, the car keys are in here.  Lets get out of here!\n" # take the car keys from the safe
        typewriter() # add the typewriter function for the typewriter effect
        has_car_keys = True # change the variable to say that you now have the car keys
        print_kitchen_options() # then return to the Kitchen menu.
    else: # If you have the combination, and already have the car keys
        line_1 = "\nThere is a safe on the Kitchen side, but it is empty.\n" # then print the default message for the safe
        typewriter() # add the typewriter function for the typewriter effect
        print_kitchen_options() # then return to the Kitchen menu.
        
def check_fridge(): #5 When checking the fridge
    global line_1
    global has_sandwich # access the global required to run the function
    if has_sandwich == False: # If you havent yet eaten the sandwich
        line_1 = "\nThere is a sandwich in the fridge.  A nice little snacky-snack.  You go ahead and eat it.\n" # take the sandwich from the fridge and eat it
        typewriter() # add the typewriter function for the typewriter effect
        has_sandwich = True # change the variable to say that you now have the sandwich
        print_kitchen_options() # and return to the Kitchen menu.
    else: # If you have already eaten the sandwich
        line_1 = "\nWhy do we all just check the fridge every so often like food is going to have teleported into it from the fifth dimension whilst we weren't looking?\n" # print a default message for the fridge
        typewriter() # add the typewriter function for the typewriter effect
        print_kitchen_options() # then return to the Kitchen menu
           
        # Garden
        
#1 Will be enter kitchen

def check_lawn(): #2 When checking the lawn
    global line_1
    global stood_in_poop # access the global variables required to run the function
    if stood_in_poop == False: # if  you have not yet stood in the poop
        line_1 = "\nYou stand in some poop.  Lovely.  You're having a really good day today.\n" # run the poop sequence
        typewriter() # add the typewriter function for the typewriter effect
        stood_in_poop = True # change the variable to say you stood in the poop
        print_garden_options() # then return to the garden menu
    else: # if you have already stood in the poop
        line_1 = "\nEwww, did you just try to do it again?  Thats disgusting!\n" # print the default message for the lawn
        typewriter() # add the typewriter function for the typewriter effect
        print_garden_options() # then return to the main menu
    
def check_iron_gate(): #3 When checking the gate
    global is_gate_open
    global has_gate_key # access the global variables required to run the function
    global line_1
    if has_gate_key == False: # if you don't have the key yet
        line_1 = "\nThe gate is locked, you will have to find the key.\n" # print the default message for the gate
        typewriter() # add the typewriter function for the typewriter effect
        print_garden_options() # then return to the Garden menu.
    if has_gate_key == True and is_gate_open == False: # If you have the key, but the gate is still closed
        line_1 = "\nYou use the iron key to unlock the gate and open it.  It's time to drive out of here!\n" # unlock the gate, open it
        typewriter() # add the typewriter function for the typewriter effect
        is_gate_open = True # change the variable to say that the gate is now open
        print_garden_options() # then return to the Garden menu.
    else: # if you have the key and the gate is open
        line_1 = "\nIt's too far to walk! You'll have to take the car.\n" # print the default message for the gate being open
        typewriter() # add the typewriter function for the typewriter effect
        print_garden_options() # then return to the Garden menu.
            
def check_rock(): #4 When checking the rock
    global line_1
    global has_moved_rock #access the global variables required to run the function.
    if has_moved_rock == False: # If you have not yet moved the rock
        line_1 = "\nIt's just a rock, but you best move it out of the path of the car.\n"
        typewriter() # add the typewriter function for the typewriter effect
        has_moved_rock = True # change the variable to say that you have now moved the rock
        print_garden_options() # then return to the Garden menu.
    else: # if you have already moved the rock
        line_1 = "\nIt's just a rock.\n" # print the default message for the rock.
        typewriter() # add the typewriter function for the typewriter effect
        print_garden_options() # then return to the Garden menu
    
def check_car_door(): #5 When checking the car door
    global line_1
    global has_car_keys # access the global variable required to run the function.
    if has_car_keys == False: #If you don't have the car keys yet
        line_1 = "\nYou need to find the keys.\n" # print the default message for the car door
        typewriter() # add the typewriter function for the typewriter effect
        print_garden_options() # then return to the Garden menu.
    else: # if you already have the car keys
        Car() # then get in the car.
        
        # Car
        
#1 Will be get out of car
        
def start_car(): # 2 When starting the car
    global is_gate_open
    global has_moved_rock # access the global variables required to run the function.
    global line_1
    if is_gate_open == False: # If the gate is not open yet
        line_1 = "\nYou can't go anywhere until you open the gate.\n" # tell the player they need to open the gate
        typewriter()
        print_car_options() # then return to the Car menu.
    elif is_gate_open == True and has_moved_rock == False: # If you have opened the gate, but not moved the rock
        line_1 = "\nYou start the car, but as try to drive off you blow your tyre on the rock. Now you're stuck.  Game Over.\n" # you will blow your tyre and get Game over message
        typewriter()
        exit_game() # then exit the game
    else: # If the gate is open, and you have moved the rock already
        line_1 = "\n\n\nCongratulations.  You have completed the game.\n\nThank you for playing.  I hope you had fun!\n\n" # congratulate the player for winning the game
        typewriter()
        exit # and exit the game
        
 
         
def exit_game():
    global line_1 #access the global required to run the function
    line_1 = "\nThe game will now close\n" # print to say that the game will now close
    typewriter() # add the typewriter function for the typewriter effect
    exit # exit the game
    
intro() # Run the intro


#
#  ###   ####    ###   #####   #      #####  #####    ####
# #      #   #  #   #    #     #      #      #    #  #    
#  ###   ####   #   #    #     #      ###    #####    ###
#     #  #      #   #    #     #      #      #    #      #
# ####   #       ###   #####   #####  #####  #    #  ####
#
#            ####   #####  #       ###   #   #
#            #   #  #      #      #   #  #   #
#            ####   ###    #      #   #  # # #
#            #   #  #      #      #   #  ## ##
#            ####   #####  #####   ###   #   #
# 
# In order to complete the game you must do the following:
#
# #4 - check the bathroom cabinet to retrieve the screwdrver
# #7 - check the toilet to retrieve the toilet paper
# #3 - place the toilet paper under the door 
# #2 - push the key out of the other side with the screwdriver
# #3 - pull the toilet paper back from under the door to get the Bathroom key
# #2 - unlock the bathroom door
# #1 - open the bathroom door and enter the landing
# #7 - look under the rug to get the tin foil
# #2 - go into the bedroom
# #5 - check the wardrobe to close the doors
# #5 - check the wardrobe again and you will see the light switch and turn it on
# #4 - check the dresser now the light is on to find the hair pin
# #2 - check the bed to find the remote control
# #1 - go back out onto the landing
# #4 - check the table to pick the lock with the hair pin
# #4 - open the draw and take the bronze key
# #3 - go downstairs
# #6 - take the batteries out of the radio
# #3 - go into the living room
# #4 - check the couch to find the iron key
# #3 - now you have the remote, batteries, and tin foil, you can turn the tv on to get the code
# #5 - now that the TV is on, you can see the combination in the light
# #1 - go back out into the hallway
# #4 - enter the kitchen know you know the code
# #4 - open the safe to get the car keys now you know the combination
# #3 - go out into the garden now you have the bronze key
# #4 - to move the rock out of the path of the car
# #3 - to unlock the gate
# #5 - to get in the car
# #2 - to start the car
#
#  ###   ####    ###   #####   #      #####  #####    ####
# #      #   #  #   #    #     #      #      #    #  #    
#  ###   ####   #   #    #     #      ###    #####    ###
#     #  #      #   #    #     #      #      #    #      #
# ####   #       ###   #####   #####  #####  #    #  ####
#
#            ###   ####    ###   #   #  #####
#           #   #  #   #  #   #  #  #   #
#           #####  ####   #   #  # #    ###
#           #   #  #   #  #   #  ##     #
#           #   #  ####    ###   #      #####