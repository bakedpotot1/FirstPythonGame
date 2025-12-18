import state
import data
from rooms import sitting_room
import utils

def yes_no():
    while True:

        choice = utils.choice_menu(
             "[Constable Bishop:]"f"\n\"Detective {data.player_name.title()}, are you ready to make your accusation?\"",
             [
                 "Yes",
                 "No"
             ]
        )
        if choice == "No":
                    state.current_room = "foyer"
                    return
        elif choice == "Yes":
                    stage_3()
                    return

def who_did_it():
     while True:
          
        choice = utils.choice_menu(
               "Choose Carefully",
               [
                    "Bernard Finch",
                    "Mitsy Bell",
                    "Pearl Hawthorne",
                    "Tallulah Blackwood"
               ]
          )
        
        if choice == "Bernard Finch":
            bernard_ending()
            return
        elif choice == "Mitsy Bell":
            other_ending()
            return
        elif choice == "Pearl Hawthorne":
            other_ending()
            return    
        elif choice == "Tallulah Blackwood":
            other_ending()
            return
    


        

def stage_1():
    state.const_not_ready = True
    utils.clear_screen()
    print("[Constable Bishop:]"f"\n\"Not yet." \
        "You don’t have enough to stand on." \
        "\nKeep looking. When you’re certain, then we’ll talk.\"")
    utils.press_to_continue()

def stage_2():
    utils.clear_screen()
    print("[Constable Bishop:]"f"\n\"Detective {data.player_name.title()}, are you ready to make your accusation?\"")
    utils.press_to_continue()
    return

def stage_3():
    utils.clear_screen()
    print("[Constable Bishop:]"f"\n\"All right, Detective." \
        "\nChoose carefully.\"")
    utils.press_to_continue()
    
def bernard_ending():
    utils.clear_screen()
    print("The house falls silent as Bernard looks at you. " \
    "\n\nHe doesn’t resist. His hand brushes the crest pin on his coat," \
    "\nthe same design engraved on the letter opener." \
    "\nThe weight of the moment is heavy, but his voice is calm.")
    utils.press_to_continue()
    utils.clear_screen()  
    print(f"[Bernard Finch:]\n\"I suppose it’s time you knew the truth, Detective {data.player_name.title()}.\""
        
    "\n\n\"Archibald… he was like a brother to me."
    "\nI even gave him this, — he gestures at the letter opener — " \
    "\nas a token of what I felt. That I accepted him as family.\"" 
    
    "\n\n\"But when I found out the partnership was ending…"
    "\nwhen I saw him turn away from what we built together…"
    "\nsomething inside me snapped.\""
    
    "\n\n\"I didn’t mean for it to come to this." 
    "\nI only wanted him to understand what betrayal feels like.\"")

    utils.press_to_continue()
    utils.clear_screen()  
    print("The documents from the safe, the letter in the study, "
    "\nand the engraved crest all fall into place in your mind. " \
    "\nEverything - motive, opportunity, betrayal - aligns." \
    "\nThe case is closed. The house is heavy with grief, but finally, the truth is known." \
    
    f"\n\n\"[Constable Bishop:] \nWell done, Detective {data.player_name.title()}"
    "You’ve seen the truth, even when it was hidden in plain sight.\"")
    utils.press_to_continue()

    exit()

def other_ending():

    print("\nConstable Bishop’s expression hardens."
          
          "\n\n[Constable Bishop:]\n\"No.\"" \
          
          "\n\nHe closes his notebook." \
          
          "\n\n[Constable Bishop:]\n\"That doesn’t fit the truth of it.\"" \
          
          "\n\nThe real killer remains in the house," \
          "\nand the chance to stop them is gone. " \
          
          "\n\nGAME OVER")
    
    space = input( )

    exit()

def constable_dialog():

    state.current_room == "constable dialog"

    while True:
        
        if state.documents_found == True and state.family_letter_found == True and state.bathroom_weapon_found == True:
                
            yes_no()
                
            who_did_it()
        else:
            stage_1()
            state.current_room = "foyer"
            break