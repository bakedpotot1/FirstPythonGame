import state
import data
from rooms import foyer, library, kitchen, study, sitting_room, corridor, master_bedroom, guest_bedroom, bathroom
from npc import bernard, constable_bishop, mitsy, pearl, tallulah

state.current_room = "foyer"

def game_loop():
    while True:
        if state.current_room == "foyer":
            foyer.enter()
        elif state.current_room == "library":
            library.enter()
        elif state.current_room == "study":
            study.enter()
        elif state.current_room == "sitting room":
            sitting_room.enter()
        elif state.current_room == "kitchen":
            kitchen.enter()
        elif state.current_room == "corridor":
            corridor.enter()
        elif state.current_room == "master bedroom":
            master_bedroom.enter()
        elif state.current_room == "guest bedroom":
            guest_bedroom.enter()
        elif state.current_room == "bathroom":
            bathroom.enter()
        elif state.current_room == "pearl dialog":
            pearl.pearl_dialog()
        elif state.current_room == "mitsy dialog":
            mitsy.mitsy_dialog()
        elif state.current_room == "tallulah dialog":
            tallulah.tallulah_dialog()
        elif state.current_room == "bernard dialog":
            bernard.bernard_dialog()
        elif state.current_room == "constable dialog":
            constable_bishop.constable_dialog() 
        else:
            pass

def intro():
    print("\nMurder Mystery: Shadows Over Blackwood Manor")
    print("\nRain beats against the iron gates as you step into Blackwood Manor." 
          "\n" 
        "\nArchibald Blackwood is dead."
        "\n" 
        "\nEveryone inside the house is a suspect." 
        "\n" 
        "\nNo one is allowed to leave. You have been asked to observe, listen, and uncover the truth.")
    
    user_name = input("Your name is? Detective ").lower()

    data.player_name = user_name

if __name__ == "__main__":
    intro()
    game_loop()