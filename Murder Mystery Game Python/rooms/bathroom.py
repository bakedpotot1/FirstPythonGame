import state
import data
import utils

def bath_menu_1():
    while True:
        choice = utils.choice_menu(
            "What would you like to do? \nOPTIONS:",
            [
                "Leave"
            ]
        )

        if choice == "Leave":
            state.current_room = "corridor"
            break
        else: print(f"{choice} not recognised")

def bath_menu_2():
    while True:
        choice = utils.choice_menu(
            "What would you like to do? \nOPTIONS:",
            [
                "Use the toilet",
                "Leave"
            ]
        )

        if choice == "Leave":
            state.current_room = "corridor"
            break
        elif choice == "Use the toilet":
            utils.clear_screen()
            print("You use the toilet and pull the handle." \
            "\nThe flush struggles, then stops short. " \
            "\nAs the tank refills, something inside shifts with a muted *clink*." \
            "\n\nCurious, you lift the lid." \
            "\nWrapped in cloth and wedged behind the mechanism is a metal letter opener." \
            "\nIts weight feels deliberate - not forgotten." \
            "\nAn unfamiliar crest is engraved into the handle.")
            utils.press_to_continue()
            state.bathroom_weapon_found = True
            state.current_room = "bathroom"
            break
        else: print(f"{choice} not recognised")






def enter():
    state.current_room = "bathroom"

    utils.clear_screen()

    if "bathroom" not in state.visited:

        print("The bathroom is spotless." \
        "\nA window stands slightly open, letting in the cold night air.")

        utils.press_to_continue()

        state.visited.append("bathroom")

        bath_menu_1()

    else:

        print("\nWhat would you like to do?")
        if state.bathroom_hint == False:
            bath_menu_1()
        elif state.bathroom_weapon_found == True:
            bath_menu_1()
        elif state.bathroom_hint == True:
            bath_menu_2()
        


#Weapon found here lodged in the cistern - Flushing reveals clinking; weapon found in cistern