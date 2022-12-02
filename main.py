def get_number_of_teams():
    while True:
        num_of_teams = input("Please enter the number of teams in the tournaments:")
        if num_of_teams > 2 :
            print("The amount of teams entered is invalid, please try again!")