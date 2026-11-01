# Create dictionary that will accept cricket players name and scores in a match.Also we are retrieving runs by entering the player’s name. 

# def create_dict():
#     player_score = {}
#     while True:
#         key = input("Enter player name ('exit' for finish ) : ").strip()
#         if key.lower() == 'exit':
#             break
#         try:
#             value = int(input(f"Enter score for {key}: "))
#             player_score[key] = value
#         except ValueError:
#             print("Invalid score! Please enter a number.")
#     return player_score
    
# def display_dict(user_dict):
#     print("\n--- Player Scoreboard ---")
#     for key, value in user_dict.items():
#         print(f"{key} : {value}")
        
# def retrieve_score(user_dict):
#     name = input("\nEnter player's name to retrieve score: ").strip()
#     if name in user_dict:
#         print(f"{name}'s score is: {user_dict[name]}")
#     else:
#         print(f"No record found for player: {name}")
#         retrieve_score()

# def main():
#     user_dict = create_dict()
#     display_dict(user_dict)
#     retrieve_score(user_dict)
    
# main() 


# Create an empty dictionary
players = {}

# Accept player names and scores
n = int(input("Enter number of players: "))

for i in range(n):
    name = input("Enter player name: ")
    score = int(input("Enter score: "))
    players[name] = score

# Display dictionary
print("\nPlayers and Scores:", players)

# Search for a player's score
search_name = input("\nEnter player name to find score: ")

if search_name in players:
    print("Score of", search_name, "is:", players[search_name])
else:
    print("Player not found")