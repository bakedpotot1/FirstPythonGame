import state
import data
from rooms import sitting_room
import utils

def stage_1():
    utils.clear_screen()
    print("[Tallulah Blackwood:]"f"\n\"I’m Tallulah Blackwood, Detective {data.player_name.title()}." \
        "\nThis house raised me — though my uncle ruled it." \
        "\nNear the end, he trusted some people more than others.\"")
    utils.press_to_continue()
#Unlocks out of place book in the library containing the Safe code    
def stage_2():
    utils.clear_screen()
    print("[Tallulah Blackwood:]"f"\n\"My uncle listened to Bernard more than he listened to me." \
        "\nI didn’t like that — and I wasn’t the only one who noticed." \
        "\nHe even kept one of Bernard’s favorite books on the library shelf… " \
        "\nI never understood why he prized it so highly.\"")
    utils.press_to_continue()
#Safe hint unlcocks safe discovery in master bedroom    
def stage_3():
    utils.clear_screen()
    print("[Tallulah Blackwood:]"f"\n\"When something truly mattered to him, Detecitve," \
        "\nhe kept it upstairs, close enough to hear a floorboard creak." \
        "\nDocuments, agreements… things that could change lives.\"")
    utils.press_to_continue()


def tallulah_dialog():

    state.current_room == "tallulah dialog"

    while True:
        if state.tallulah_stage == 1 and state.key_found == False:
            stage_1()
            state.tallulah_current = 1
            state.tallulah_stage = 1
            state.current_room = "guest bedroom"
            return
        elif state.tallulah_stage <= 2 and state.key_found == True and state.safe_code_found == False:
            stage_2()
            state.tallulah_stage = 2
            state.tallulah_current = 2
            state.library_hint = True
            state.current_room = "guest bedroom"
            return
        elif state.tallulah_current >= 2 and state.safe_code_found == True:
            stage_3()
            state.tallulah_stage = 3
            state.tallulah_current = 3
            state.current_room = "guest bedroom"
            return
        else:
            print("error")
            break          