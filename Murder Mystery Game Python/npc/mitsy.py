import state
import data
from rooms import sitting_room
import utils

def stage_1():
    utils.clear_screen()
    print("[Mitsy Bell:]"f"\n\"I’m Mitsy Bell, Detective {data.player_name.title()}." \
        "\nI’ve worked in this kitchen longer than I care to count." \
        "\nYou notice every creak and crack when you’re in one place long enough.\"")
    utils.press_to_continue()

   
def stage_2():
    utils.clear_screen()
    print("[Mitsy Bell:]""\n\"The pantry wall’s been troublesome for years." \
        "\nOne brick near the floor keeps working loose." \
        "\nMr. Blackwood said he’d call someone to fix it - but he hated people meddling with his home.\"")
    utils.press_to_continue()

def stage_3():
    utils.clear_screen()
    print("[Mitsy Bell:]""\n\"I’d be lying if I said I wasn’t uneasy, Detective." \
        "\nI heard talk of changes being made." \
        "\nAfter twenty years, that kind of uncertainty weighs on you.\"")
    utils.press_to_continue()

def mitsy_dialog():

    state.current_room = "mitsy dialog"
    while True:
        if state.study_locked == False and state.mitsy_current == 3:
            stage_3()
            state.mitsy_stage = 3
            state.mitsy_current = 3
            state.current_room = "kitchen"
            return
        elif state.mitsy_current <= 2 and state.study_open_attempted == True and state.mit_fail_safe == False:
            stage_2()
            state.mitsy_stage = 2
            state.mitsy_current = 2
            state.brick_hint = True
            state.current_room = "kitchen"
            return
        elif state.mitsy_stage == 1 and state.mitsy_current < 2:
            stage_1()
            state.visited.append("mitsy")
            state.mitsy_current = 1
            state.mit_fail_safe = False
            state.current_room = "kitchen"
            return
