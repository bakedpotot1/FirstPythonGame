import state
import data
import utils


def mitsy_menu_1():

    while True:
        choice = utils.choice_menu(
            "What would you like to do? \nOPTIONS:",
            [
                "Speak to Mitsy Bell",
                "Leave"
            ]
        )

        if choice == "Speak to Mitsy Bell":
            state.current_room = "mitsy dialog"
            break
        elif choice == "Leave":
            state.current_room = "foyer"
            break
        elif choice == "inspect wall":
            utils.clear_screen()
            print("One brick in the pantry wall gives slightly under your touch." \
            "\nYou work it free, revealing a narrow cavity behind it. " \
            "\n\nInside rests a small brass key, worn smooth from use." \
            "\nThis wasn’t hidden in a hurry - it was placed here carefully.")
            state.key_found = True
            state.current_room = "kitchen"
            break
        else: print(f"{choice} not recognised")

def mitsy_menu_2():

    while True:
        choice = utils.choice_menu(
            "What would you like to do? \nOPTIONS:",
            [
                "Inspect the Wall",
                "Speak to Mitsy Bell",
                "Leave"
            ]
        )

        if choice == "Speak to Mitsy Bell":
            state.current_room = "mitsy dialog"
            break
        elif choice == "Leave":
            state.current_room = "foyer"
            break
        elif choice == "Inspect the Wall":
            utils.clear_screen()
            print("One brick in the pantry wall gives slightly under your touch." \
            "\nYou work it free, revealing a narrow cavity behind it. " \
            "\n\nInside rests a small brass key, worn smooth from use." \
            "\nThis wasn’t hidden in a hurry - it was placed here carefully.")
            utils.press_to_continue()
            state.key_found = True
            state.current_room = "kitchen"
            break
        else: print(f"{choice} not recognised")



def enter():

    state.current_room = "kitchen"

    utils.clear_screen()

    if "kitchen" not in state.visited:

        print("The air smells faintly of herbs and damp stone." \
        "\nPots have been left soaking, as if someone was interrupted mid-task.")

        print("\nNear the stove, a plump woman carefully chops vegetables, glancing occasionally at the clock." \
        "\nThis is Mitsy Bell, the cook.")

        state.visited.append("kitchen")
        utils.press_to_continue()
        mitsy_menu_1()

    else:
        if state.brick_hint == False:
            mitsy_menu_1()
        elif state.key_found == True:
            mitsy_menu_1()
        elif state.brick_hint == True:
            mitsy_menu_2()



#Study Key - hidden beind a loose brick - player must inspect after misty hints at it