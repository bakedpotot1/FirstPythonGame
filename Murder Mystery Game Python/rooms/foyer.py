import state
import data
import utils

def foyer_choice():
    
    while True:

        choice = utils.choice_menu(
            "What would you like to do \nOPTIONS:", 
            [
                "Go to the Kitchen",
                "Go to the Library",
                "Go to the Sitting Room",
                "Walk up the Stairs",
                "Speak to Constable Bishop"
            ]
            )

        if choice == "Go to the Kitchen":
            utils.clear_screen()
            print("You walk into the Kitchen.")
            utils.press_to_continue()
            state.current_room = "kitchen"
            break
        elif choice == "Go to the Library":
            utils.clear_screen()
            print("You walk into the Library.")
            utils.press_to_continue()
            state.current_room = "library"
            break
        elif choice == "Go to the Sitting Room":
            utils.clear_screen()
            print("You walk into the Sitting Room.")
            utils.press_to_continue()
            state.current_room = "sitting room"
            break
        elif choice == "Walk up the Stairs":
            utils.clear_screen()
            print("You walk up the stairs.")
            utils.press_to_continue()
            state.current_room = "corridor"
            break
        elif choice == "Speak to Constable Bishop":
            state.current_room = "constable dialog"
            break
        else: 
            print(f"{choice} not recognised, please try again.")


def enter():
    state.current_room = "foyer"

    
    if state.first_time_foyer == True:
        utils.clear_screen()
        print("The front door closes behind you with a heavy thud. " \
        "\nWhatever happened here, it happened last night.")

        print("\nThe foyer is cold and echoing. Rainwater drips from coats hung by the door. " \
        "\nThe house feels tense - as though it’s holding its breath.")

        state.first_time_foyer = False

        print("\nYou notice a tall, stern figure standing near the door. " \
        "\nHis uniform is neat, but his eyes are tired and watchful. " \
        "\nHe straightens as he notices you, then approaches.")

        utils.press_to_continue()
        utils.clear_screen()

        print("[Constable Bishop:]"f"\n\"Ah, Detective {data.player_name.title()}, welcome to Blackwood Manor." \
        "\nI’ve secured the house - no one is leaving until we know what happened." \
        "\nArchibald Blackwood is dead. Everyone inside could be involved. " \
        "\nYou must speak to everyone here and gather clues. " \
        "\nPay attention to what they say. " \
        "\nWhen you think you know who the killer is, return to me and make your accusation. " \
        "\nBut remember, accuse the wrong person, and you’ll have to start over. " \
        f"\nTake your time, Detective {data.player_name.title()}. Observe, listen, and explore.\"")

        utils.press_to_continue()
        foyer_choice()
        
    elif state.const_not_ready == True:
        state.const_not_ready = False
        foyer_choice()
    else:
        utils.clear_screen()
        print("You walk back into the Foyer.")
        utils.press_to_continue()
        foyer_choice()
    
        

            
            






































# def enter():
#     state.current_room = "foyer"

    
#     if state.first_time_foyer == True:

#         print("\nThe front door closes behind you with a heavy thud. " \
#         "\nWhatever happened here, it happened last night.")

#         print("\nThe foyer is cold and echoing. Rainwater drips from coats hung by the door. " \
#         "\nThe house feels tense - as though it’s holding its breath.")

#         state.first_time_foyer = False

#         print("\nYou notice a tall, stern figure standing near the door. " \
#         "\nHis uniform is neat, but his eyes are tired and watchful. " \
#         "\nHe straightens as he notices you, then approaches.")

#         print("\n[Constable Bishop:]"f"\n\"Ah, Detective {data.player_name.title()}, welcome to Blackwood Manor." \
#         "\nI’ve secured the house - no one is leaving until we know what happened." \
#         "\nArchibald Blackwood is dead. Everyone inside could be involved. " \
#         "\nYou must speak to everyone here and gather clues. " \
#         "\nPay attention to what they say. " \
#         "\nWhen you think you know who the killer is, return to me and make your accusation. " \
#         "\nBut remember, accuse the wrong person, and you’ll have to start over. " \
#         f"\nTake your time, Detective {data.player_name.title()}. Observe, listen, and explore.\"")

#         print("\nWhat would you like to do?")

#         print("\nOPTIONS: \n Go to the: " \
#         "\n - Kitchen " \
#         "\n - Library " \
#         "\n - Sitting Room " \
#         "\n - Stairs" 
#         "\n Speak to:" 
#         "\n - Constable Bishop")
        
#     else:
#         print("\nYou walk back into the Foyer.")
#         print("\nWhat would you like to do?")
#         print("\nOPTIONS: \n Go to the: " \
#         "\n - Kitchen " \
#         "\n - Library " \
#         "\n - Sitting Room " \
#         "\n - Stairs" 
#         "\n Speak to:" 
#         "\n - Constable Bishop")
        

#     while True:

#         choice = input("Please enter: ").lower()

#         if choice == "kitchen":
#             print("\nYou walk into the Kitchen.")
#             state.current_room = "kitchen"
#             break
#         elif choice == "library":
#             print("\nYou walk into the Library.")
#             state.current_room = "library"
#             break
#         elif choice == "sitting room":
#             print("\nYou walk into the Sitting Room.")
#             state.current_room = "sitting room"
#             break
#         elif choice == "stairs":
#             print("\nYou walk up the stairs.")
#             state.current_room = "corridor"
#             break
#         elif choice == "constable bishop":
#             state.current_room = "constable dialog"
#             break
#         else: 
#             print(f"{choice} not recognised, please try again.")