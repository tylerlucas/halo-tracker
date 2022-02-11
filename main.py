from re import I
from lib import lib
from collections import namedtuple
import gamer as gm
import gather_stats as gs
import gamer_db
import sys

all_gamers = {} 
menu_cont = True

def main_menu():
    menu_select = input('1) Enter Gamertag\n2) Get Gamer DB\n3) Delete Gamer DB\n0) Quit\nSelection: ')
    if menu_select == '1':
        enter_gamertag()
    elif menu_select == '2':
        gamer_db.get_gamer_db()
        main_menu()
    elif menu_select == '3':
        gamer_db.recreate_gamer_db()
    elif menu_select == '0': 
        print('Goodbye!')
        sys.exit()

def enter_gamertag():
    stats = ()
    gamertag = input('Enter gamertag: ')
    current_gamer = gm.Gamer(gamertag)
    stats = gs.gather_all_stats(gamertag)
    current_gamer.set_stats(stats[0], stats[1], stats[2], stats[3], stats[4])

    all_gamers.update({gamertag: current_gamer})
    gamer_db.update_gamer_to_db(current_gamer)
    main_menu()

# Main function
main_menu()
