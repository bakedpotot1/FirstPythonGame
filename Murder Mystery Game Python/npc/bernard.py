import state
import data
from rooms import sitting_room
import utils

def stage_1():
    utils.clear_screen()
    print("[Bernard Finch:]"f"\n\"I'm Bernard Finch, Detective {data.player_name.title()}." \
        "\nArchibald and I worked together for many years." \
        "\nIn time… he became something like family to me.\"")
    utils.press_to_continue()

def stage_2():
    utils.clear_screen()
    print("[Bernard Finch:]"f"\n\"I don’t care for sentimentality, Detective." \
        "\nGifts, displays - they blur lines." \
        "\nIf something mattered, I believed in building it, not presenting it.\"")
    utils.press_to_continue()

def stage_3():
    utils.clear_screen()
    print("[Bernard Finch:]"f"\n\"Tensions existed yes, but anger is common." \
        "\nWhat matters is who keeps their head when others don’t.\"")
    utils.press_to_continue()


def bernard_dialog():

    state.current_room == "bernard dialog"

    while True:
        if state.bernard_stage == 1 and state.bernard_current < 2 and state.safe_code_found == False:
            stage_1()
            state.bernard_current = 1
            state.current_room = "master bedroom"
            return
                 
 
        elif state.bernard_current < 3 and state.safe_code_found == True and state.documents_found == False:
            stage_2()
            state.bernard_stage = 2
            state.bernard_current = 2
            state.current_room = "master bedroom"
            return
        elif state.documents_found == True and state.bernard_current >= 1:
            stage_3()
            state.bernard_stage = 3
            state.bernard_current = 3
            state.current_room = "master bedroom"
            return
        else:
            print("error")
            break 













