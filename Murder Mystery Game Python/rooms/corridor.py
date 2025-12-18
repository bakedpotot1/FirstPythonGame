import state
import data
import utils


def corr_menu():
    while True:

        choice = utils.choice_menu(
            "Where would you like to go? \nOPTIONS:",
            [
                "Go to the Master Bedroom",
                "Go to the Guest Bedroom",
                "Go to the Bathroom",
                "Go back down the Stairs"
            ]
        )

        if choice == "Go to the Master Bedroom":
            utils.clear_screen()
            print("You walk into the Master Bedroom.")
            utils.press_to_continue()
            state.current_room = "master bedroom"
            break
        elif choice == "Go to the Guest Bedroom":
            utils.clear_screen()
            print("You walk into the Guest Bedroom.")
            utils.press_to_continue()
            state.current_room = "guest bedroom"
            break
        elif choice == "Go to the Bathroom":
            utils.clear_screen()
            print("You walk into the Bathroom.")
            utils.press_to_continue()
            state.current_room = "bathroom"
            break
        elif choice == "Go back down the Stairs":
            utils.clear_screen()
            print("You walk down the stairs.")
            utils.press_to_continue()
            state.current_room = "foyer"
            break
        else: print(f"{choice} not recognised")






def enter():
    utils.clear_screen()
    state.current_room = "corridor"
    print("You walk into the corridor.")
    if "corridor" not in state.visited:

        print("The corridor creaks underfoot. Doors line the walls, all closed." \
        "\nThe air smells faintly of soap and polish.")
        utils.press_to_continue()

        state.visited.append("corridor")

        corr_menu()

    else:

        corr_menu()
