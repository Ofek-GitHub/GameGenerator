def get_number_of_teams():
    while True:
        num_teams = int(input("Enter the number of teams in the tournament: "))

        if num_teams >= 2 and num_teams % 2 == 0:
            break

        print("The minimum number of teams is 2 and it has to be an even, try again.")

    return num_teams

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
        games_played = num_of_teams -1
        return games_played
        

def get_num_of_wins(team_names, games_played):
    team_wins = []
    for team in team_names:
        while True:
            wins = int(input("Please enter the amount of wins " + team +" team has had:"))
            if wins > games_played:
                print("The amount of wins is bigger then games played, please try again.")
            elif wins < 0 :
                print("This number is invalid, team cant have a negetive amount of wins! try again!")
            else:
                break
        team_wins.append((team,wins))
    return team_wins

def get_second_item(teams):
    return teams[1]

num_of_teams = get_number_of_teams()
names = get_teams_names(num_of_teams)
games_played = get_number_of_games_played(num_of_teams)
wins = get_num_of_wins(names,games_played)
print(wins)
sorted_teams = sorted(wins,key = get_second_item)
print(sorted_teams)

print("Generating games for the first round...")

for i in range(int(num_of_teams/2)):
    Away = sorted_teams[i][0]
    Home = sorted_teams[-1][0]
    sorted_teams.pop() 
    print(f"Home: {Home} VS Away: {Away}")

            


