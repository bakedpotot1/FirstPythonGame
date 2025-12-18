import state
import data
import utils

def bern_menu_1():
    while True:

        choice = utils.choice_menu(
            "What would you like to do? \nOPTIONS:",
            [
                "Speak to Bernard Finch",
                "Leave"
            ]
        )

        if choice == "Leave":
            state.current_room = "corridor"
            break
        elif choice == "Speak to Bernard Finch":
            state.current_room = "bernard dialog"
            break


def bern_menu_2():
    while True:

        choice = utils.choice_menu(
            "What would you like to do? \nOPTIONS:",
            [
                "Inspect the Safe",
                "Speak to Bernard Finch",
                "Leave"
            ]
        )

        if choice == "Leave":
            state.current_room = "corridor"
            break
        elif choice == "Speak to Bernard Finch":
            state.current_room = "bernard dialog"
            break
        elif choice == "Inspect the Safe":
            utils.clear_screen()
            print("The safe opens with a low metallic click." \
            "\n\nInside are neatly arranged documents - contracts, letters, financial records."
            "\nEach tells a different story;" \
            "\nunpaid debts, disputed inheritances, broken agreements, promises quietly withdrawn." \
            "\n\nEvery name in the house appears somewhere among the pages.")
            utils.press_to_continue()
            state.documents_found = True
            state.current_room = "master bedroom"
            break
        else: 
            print(f"{choice} not recognised")




def enter():
    state.current_room = "master bedroom"

    utils.clear_screen()
    if "master bedroom" not in state.visited:

        print("The Master Bedroom is immaculate. A man stands near the window, hands clasped behind his back," \
	    "\nneatly dressed as if habits matter to him." \
        "\nA small metal pin rests on his lapel - a crest you don’t recognise, worn smooth with age." \
        "\nHe turns as you approach, his expression polite but measured.")

        utils.press_to_continue()

        state.visited.append("master bedroom")

        bern_menu_1()

    else:
        print("\nWhat would you like to do?")
        if state.safe_code_found == False and state.documents_found == False:
            bern_menu_1()
        elif state.safe_code_found == True and state.documents_found == True:
            bern_menu_1()
        elif state.safe_code_found == True and state.documents_found == False:
            bern_menu_2()

#Safe - hidden - lockedL requires code from study note
#Financial Documents/contact - inside safe - found after code entered. Confirms motive