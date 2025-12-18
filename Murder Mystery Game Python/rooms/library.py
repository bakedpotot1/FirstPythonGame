import state
import data
import utils


def lib_menu_1():
    while True:
        choice = utils.choice_menu(
            "What would you like to do? \nOPTIONS:",
            [
                "Study",
                "Leave"
            ]
        )

        if choice == "Study":
            if state.key_found == True and state.study_locked == True:
                utils.clear_screen()
                print("You take the key from your pocket and unlock the study door.")
                state.mitsy_current = 3
                state.study_locked = False
                print("You walk into the study.")
                utils.press_to_continue()
                state.current_room = "study"
                break
            elif state.key_found == True and state.study_locked == False:
                utils.clear_screen()
                print("You walk into the study.")
                utils.press_to_continue()
                state.current_room = "study"
                break
            elif state.key_found == False and state.study_locked == True:
                utils.clear_screen()  
                print("\nYou try to open the door, but the Study door is locked tight." \
                "\nWhatever Archibald kept in there, he wanted private.")
                utils.press_to_continue()
                state.study_open_attempted = True
                if "mitsy" in state.visited:
                    state.mit_fail_safe = False
                    return
                else:
                    state.mit_fail_safe = True
            


        elif choice == "inspect bookcase":
            utils.clear_screen()
            print("Among the shelves, one book sits misaligned, its spine worn more than the rest." \
            "\nWhen you open it, a folded slip of paper falls out." \
            "\n\nFour numbers are written in steady handwriting." \
            "\nWhoever hid this expected someone to come looking.")
            utils.press_to_continue()
            state.safe_code_found = True
            state.current_room = "library"
            break
        elif choice == "Leave":
            state.current_room = "foyer"
            break
        else: print(f"{choice} not recognised")


def lib_menu_2():
    while True:
        choice = utils.choice_menu(
            "What would you like to do? \nOPTIONS:",
            [
                "Inspect the Bookcase",
                "Study",
                "Leave"
            ]
        )

        if choice == "Study":
            if state.key_found == True and state.study_locked == True:
                utils.clear_screen()
                print("You take the key from your pocket and unlock the study door.")
                state.mitsy_current = 3
                state.study_locked = False
                print("You walk into the study.")
                utils.press_to_continue()
                state.current_room = "study"
                break
            elif state.key_found == True and state.study_locked == False:
                utils.clear_screen()
                print("You walk into the study.")
                utils.press_to_continue()
                state.current_room = "study"
                break
            elif state.key_found == False and state.study_locked == True:
                utils.clear_screen()  
                print("You try to open the door, but the Study door is locked tight." \
                "\nWhatever Archibald kept in there, he wanted private.")
                utils.press_to_continue()
                state.study_open_attempted = True
                if "mitsy" in state.visited:
                    state.mit_fail_safe = False
                    return
                else:
                    state.mit_fail_safe = True
                    return


        elif choice == "Inspect the Bookcase":
            utils.clear_screen()  
            print("Among the shelves, one book sits misaligned, its spine worn more than the rest." \
            "\nWhen you open it, a folded slip of paper falls out." \
            "\n\nFour numbers are written in steady handwriting." \
            "\nWhoever hid this expected someone to come looking.")
            utils.press_to_continue()
            state.safe_code_found = True
            state.current_room = "library"
            break
        elif choice == "Leave":
            state.current_room = "foyer"
            break
        else: print(f"{choice} not recognised")



def enter():

    state.current_room = "library"

    utils.clear_screen()

    if "library" not in state.visited:
        
        print("Tall shelves line the walls, packed tightly with old books." \
        "\nA single lamp glows on a side table. It’s unusually quiet here.")
        utils.press_to_continue()
        state.visited.append("library")

        lib_menu_1()
    else:

        print("\nWhat would you like to do?")
        if state.library_hint == False and state.safe_code_found == False:
            lib_menu_1()
        elif state.library_hint == True and state.safe_code_found == True:
            lib_menu_1()
        elif state.library_hint == True and state.safe_code_found == False:
            lib_menu_2()

 