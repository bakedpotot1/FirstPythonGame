import state
import data
from npc import archibald, bernard, constable_bishop, mitsy, pearl, tallulah
import utils


def sit_menu():
    while True:
        choice = utils.choice_menu(
            "What would you like to do? \nOPTIONS:",
            [
                "Speak to Pearl Hawthorne",
                "Leave"
            ]
        )

        if choice == "Leave":
            state.current_room = "foyer"
            break
        if choice == "Speak to Pearl Hawthorne":
            state.current_room = "pearl dialog"
            break
        else: print(f"{choice} not recognised")








def enter():

    state.current_room = "sitting room"

    if "sitting room" not in state.visited:

        utils.clear_screen()

        print("The Sitting Room is dimly lit. An armchair sits slightly askew near the fireplace." \
        "\nThis is where Archibald Blackwood was found.")

        print("\nIn the Sitting Room, you notice a middle-aged woman tidying the fireplace mantel." \
        "\nShe pauses and looks up as you enter, her expression wary but polite. ")

        utils.press_to_continue()

        state.visited.append("sitting room")

        sit_menu()
    else:
        sit_menu()
    





