import state
import data
import utils

def guest_menu():
    while True:

        choice = utils.choice_menu(
            "What would you like to do? \nOPTIONS:",
            [
                "Speak to Tallulah Blackwood",
                "Leave"
            ]
        )

        if choice == "Leave":
            state.current_room = "corridor"
            break
        elif choice == "Speak to Tallulah Blackwood":
            state.current_room = "tallulah dialog"
            break
        else: print(f"{choice} not recognised")








def enter():
    state.current_room = "guest bedroom"

    utils.clear_screen()

    if "guest bedroom" not in state.visited:

        print("A young woman stands by the window, gazing outside." \
        "\nHer posture is tense, and she seems lost in thought. " \
        "\nThis is Tallulah Blackwood, Archibald’s niece.")

        utils.press_to_continue()

        state.visited.append("guest bedroom")

        guest_menu()

    else:
        
        guest_menu()
        
 