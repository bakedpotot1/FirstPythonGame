import state
import data
import utils

def study_menu_1():
    while True:
        choice = utils.choice_menu(
            "What would you like to do? \nOPTIONS:",
            [
                "Leave"
            ]
        )

        if choice == "Leave":
            utils.clear_screen()
            print("You walk back into the library")
            state.current_room = "library"
            break
        else: print(f"{choice} not recognised")

def study_menu_2():
    while True:
        choice = utils.choice_menu(
            "What would you like to do? \nOPTIONS:",
            [
                "Inspect the desk",
                "Leave"
            ]
        )

        if choice == "Leave":
            utils.clear_screen()
            print("You walk back into the library")
            state.current_room = "library"
            break
        if choice == "Inspect the desk":
            utils.clear_screen()
            state.family_letter_found = True
            print("The desk drawer sticks, then slides open." \
            "\nInside lies a single letter, carefully folded." \
            "\n\nIt speaks of loyalty, shared history, and being \"bound beyond blood.\"" \
            "\nInstead of a signature, a familiar crest has been drawn at the bottom.")
            utils.press_to_continue()
            state.current_room = "study"
            break
        else: print(f"{choice} not recognised")



def enter():
    state.current_room = "study"
    if "study" not in state.visited:

        utils.clear_screen()

        print("The Study smells of old paper and dust." \
        "\nA large desk dominates the room, its drawers slightly open."
        "\nShelves of books line the walls, and there’s a faint trace of ink on the floor."
        "\nYou sense that important clues could be hidden here.")

        utils.press_to_continue()

        state.visited.append("study")

        study_menu_2()

    else:
        study_menu_1()


#Letter in drawer - Study opened with key - Symbolic “family” letter, altered crest, emotional confirmation