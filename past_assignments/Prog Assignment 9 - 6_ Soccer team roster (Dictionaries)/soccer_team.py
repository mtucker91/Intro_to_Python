# FIXME 1: This function takes the number of player (num) to be add to the team at the beginning. It should prompt the
# num times for player's jersey number and player's rating.
# Then returns a dictionary, where items are (jersey_num : rating_num)
def create_roster(num):
    soccer_team = {}
    i = 1
    info = ['','']
    while i <= num:
        info[0] = int(input(f'Enter player {i}\'s jersey number:\n'))
        info[1] = int(input(f'Enter player {i}\'s rating:\n'))
        soccer_team.update({ info[0] : info[1]})
        i += 1
    return soccer_team

# FIXME 2: This function takes in nothing and return nothing. It just output the menu items,
# so the user can see the options
def menu():
    print('MENU\na - Add player\nr - Remove player\nu - Update player rating\np - Print roster\nq - Quit')

# FIXME 3: This function takes in a dictionary (team_dict) and prompt the user for a new player's jersey number and
# rating, then add them to the dictionary. No print nor return. The dictionary should be updated already and seen
# outside the function.
def add_player(team_dict):
    info = ['','']
    info[0] = int(input(f'Enter a new player\'s jersey number:\n'))
    info[1] = int(input(f'Enter the player\'s rating:\n'))
    team_dict.update({ info[0] : info[1]})
# FIXME 4: This function takes in a dictionary (team_dict) and prompt the user for a player's jersey number, then
# delete the player from the dictionary. No return.
def remove_player(team_dict):
    info = ['']
    info[0] = int(input(f'Enter a jersey number:\n'))
    del team_dict[info[0]]
    pass
# FIXME 5: This function takes in a dictionary (team_dict) and prompt the user for a player's jersey number, then
# prompt the user for new rating. After that, update the dictionary. No return
def update_player(team_dict):
    info = ['','']
    info[0] = int(input(f'Enter a jersey number:\n'))
    info[1] = int(input(f'Enter a new rating for player:\n'))
    team_dict.update({ info[0] : info[1]})
    pass
# FIXME 6: This function takes in a dictionary (team_dict) and prints the team roster. No return.
def print_roster(team_dict):
    for player in team_dict:
        print(f'Jersey number: {player}, Rating: {team_dict[player]}')

if __name__ == "__main__":
    # FIXME 7a: Print the program name
    team_dict = {}
    print('Soccer team roster')
    # FIXME 7b: prompt the user for the number of players to be add to the roster at beginning of the program.
    create_num = int(input('How many players you want to create your team roster with?\n'))
    # FIXME 7c: Call the function create_roster with the number entered above. You should save the returned dictionary
    # from this call in a dict object, like team_dict
    team_dict = create_roster(create_num)


    # FIXME 7d: make a while loop that makes the program runs as long as the menu item picked is not q
    # for each choice, call the function that will perform the user choice.
    choice = ''
    while choice != 'q':
        menu()
        choice = str(input('Choose an option:\n'))
        if choice == 'a':
            add_player(team_dict)
        elif choice == 'r':
            remove_player(team_dict)
        elif choice == 'u':
            update_player(team_dict)
        elif choice == 'p':
            print_roster(team_dict)
        elif choice == 'q':
            pass