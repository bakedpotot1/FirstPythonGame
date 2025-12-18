import readchar
from readchar import key
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def choice_menu(title, options):

    selected = 0

    while True:

        clear_screen()
        print(title)
        print()

        for i, option in enumerate(options):

            if i == selected:
                print(f"> {option}")
            else:
                print(f"  {option}")

            
        pressed = readchar.readkey()

        if pressed == key.UP:
            selected = (selected - 1) % len(options)
        elif pressed == key.DOWN:
            selected = (selected + 1) % len(options)
        elif pressed == key.ENTER:
            return options[selected]
        


def press_to_continue():

    print("\nPress any key to continue...")
    readchar.readkey()


