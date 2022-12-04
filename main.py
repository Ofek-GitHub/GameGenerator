def get_number_of_teams():
    while True:
        num_of_teams = input("Please enter the number of teams in the tournaments:")
        if num_of_teams < 2 :
            print("The amount of teams entered is invalid, please try again!")
            break
        return num_of_teams


def get_teams_names(num_of_teams):
    team_names = []
    for i in range(num_of_teams):
        while True:
            team_name = input("Please enter the team name:")
            num_words = len(team_name.split(" "))
            if num_words > 2:
                print("Number of words must be 2 at most.")
            elif len(team_name) < 2:
                print("Team name must contain atleast 2 characters!")
            else:
                break
        team_names.append(team_name)
    return team_names

def get_number_of_games_played(num_teams):
    while True:
        games_played = int(
            input("Enter the number of games played by each team: "))

        if games_played >= num_teams - 1:
            break

        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")

    return games_played        

            


