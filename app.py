from constants import *
import os

player_data = PLAYERS[:]
team_data = TEAMS[:]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def cleaned_player(players):
    """Cleans up player_data"""
    for player in players:
        for key, value in player.items():
            if key == "experience" and value == "YES":
                value = True
            if key == "experience" and value == "NO":
                value = False
            if key == "height":
                value = int(value[:2])
            if key == "guardians":
                value = [value.replace(' and', ',')]
            player.update({key: value})
    return players


def experienced_player(players):
    """Separates experienced players from clean_players via list index"""
    experienced = []
    for index, player in enumerate(players):
        if players[index]["experience"] is True:
            experienced.append(player)
    return experienced


def inexperienced_player(players):
    """Separates inexperienced players from clean_players via list index"""
    inexperienced = []
    for index, player in enumerate(players):
        if players[index]["experience"] is False:
            inexperienced.append(player)
    return inexperienced


def team_one():
    team_name = team_data[0]
    team = {team_name: experienced_players[:3] + inexperienced_players[:3]}
    return team


def team_two():
    team_name = team_data[1]
    team = {team_name: experienced_players[3:6] + inexperienced_players[3:6]}
    return team


def team_three():
    team_name = team_data[2]
    team = {team_name: experienced_players[6:] + inexperienced_players[6:]}
    return team


def team_stats(team):
    """Cleans up data into lists for team stats page."""
    clear_screen()
    player_list = []
    experienced = []
    inexperienced = []
    average_height_list = []
    guardians_list = []

    for key, value in team.items():
        print("Team: {} Stats".format(key))

    print("-" * 20)
    print("Total Players: {}".format(len(team[key])))

    for players in team.values():
        for player in players:
            player_list.append(player["name"])

            if player["experience"] is True:
                experienced.append("name")
                average_height_list.append(player["height"])
                guardians_list.extend(player["guardians"])
            elif player["experience"] is False:
                inexperienced.append("name")
                average_height_list.append(player["height"])
                guardians_list.extend(player["guardians"])

    print("\nPlayers on Team:")
    print(", ".join(player_list))
    print("\nExperienced Players: {}".format(len(experienced)))
    print("Inexperienced Players: {}".format(len(inexperienced)))

    average_height = sum(average_height_list) // 6

    print("Average Height: {}".format(average_height))
    print("\nPlayer Guardians: ")
    print(", ".join(guardians_list))

    input("\nPress Enter to continue...")
    clear_screen()


def main_menu():
    clear_screen()

    while True:

        print("\nBASKETBALL TEAM STATS TOOL")
        print("\n---- Menu ----\n")
        print("Here are your choices:\n")
        print("1) Display Team Stats")
        print("2) Quit")

        user_input = input("\nEnter an option > ").lower()

        if user_input == "1" or user_input == "display team stats":
            display_teams()
        elif user_input == "2" or user_input == "quit":
            clear_screen()
            print("Goodbye. Thank you for checking out our Basketball Team Stats Tool!\n")
            break
        else:
            clear_screen()
            print("\nI don't understand that. Please select option '1' or '2'")


def display_teams():
    clear_screen()

    while True:

        print("Teams:\n")
        index = 1

        for team in team_list:
            for keys, value in team.items():
                print("{}) {}".format(index, keys))
                index += 1

        print("\nEnter '4' or 'exit' to return to the main menu")

        user_input = input("\nEnter an option > ").lower()

        if user_input == "1" or user_input == "Panthers":
            team_stats(team_one)
        elif user_input == "2" or user_input == "Bandits":
            team_stats(team_two)
        elif user_input == "3" or user_input == "Warriors":
            team_stats(team_three)
        elif user_input == "4" or user_input == "exit":
            print("Okay, returning to the main menu")
            clear_screen()
            break
        else:
            clear_screen()
            print("\nUh-Oh! I don't understand that. Please select option '1', '2', '3', '4' or 'exit'\n")


if __name__ == "__main__":

    cleaned_players = cleaned_player(player_data)
    experienced_players = experienced_player(cleaned_players)
    inexperienced_players = inexperienced_player(cleaned_players)
    team_one = team_one()
    team_two = team_two()
    team_three = team_three()
    team_list = [team_one, team_two, team_three]

    main_menu()
