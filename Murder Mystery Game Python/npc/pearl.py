import state
import data
from rooms import sitting_room
import utils


def stage_1():
    utils.clear_screen()
    print("[Pearl Hawthorne:]"f"\n\"My name is Pearl Hawthorne, Detective {data.player_name.title()}." \
        "\nI’ve kept this house in order for decades." \
        "\nWhen something is out of place, I tend to notice.\"")
    utils.press_to_continue()   
def stage_2():
    utils.clear_screen()
    print("[Pearl Hawthorne:]""\n\"That night felt unsettled, Detective."
        "\nSomeone was moving about more than usual - " \
        "\nup and down the stairs, doors opening and closing." \
        "\nI remember the upstairs bathroom being used more than once, which struck me as odd.\"")
    utils.press_to_continue()    

def stage_3():
    utils.clear_screen()
    print("[Pearl Hawthorne:]"f"\n\"I didn’t see anything directly, Detective {data.player_name.title()}."
        "\nBut whoever moved about knew how to do so quietly." \
        "\nThat sort of confidence only comes from familiarity.\"")
    utils.press_to_continue()

def pearl_dialog():

    state.current_room == "pearl dialog"

    while True:
        if state.pearl_stage == 1 and state.total_current < 2 and state.key_found == False:
            stage_1()
            state.pearl_current = 1
            state.current_room = "sitting room"
            return
        elif state.pearl_current < 3 and state.key_found == True and state.bathroom_weapon_found == False:
            stage_2()
            state.pearl_stage = 2
            state.pearl_current = 2
            state.bathroom_hint = True
            state.current_room = "sitting room"
            return
        elif state.bathroom_weapon_found == True and state.pearl_current > 1:
            stage_3()
            state.pearl_stage = 3
            state.pearl_current = 3
            state.current_room = "sitting room"
            return
        else:
            print("error")
            break