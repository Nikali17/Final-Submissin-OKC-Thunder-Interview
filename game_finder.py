"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
	
	# Dictionary to store the number of qualifying players for each game
    games_dict = {}

    # Use a for loop to go through each player's data
    for player in game_data:
        game_id = player["gameID"]

        # Calculate the total points, field goal attempts, and free throw attempts
        total_points = player["fieldGoal2Made"] * 2 + player["fieldGoal3Made"] * 3 + player["freeThrowMade"]
        total_field_goal_attempts = player["fieldGoal2Attempted"] + player["fieldGoal3Attempted"]
        total_freethrow_attempts = player["freeThrowAttempted"]

        # Calculate True Shooting percentage for the player
        ts_percentage = (0.5 * total_points) / (total_field_goal_attempts + (0.44 * total_freethrow_attempts)) * 100

        # If the player meets the True Shooting cutoff, count them for the game
        if ts_percentage >= true_shooting_cutoff:
            # Increment the count of qualifying players for this game
            if game_id in games_dict:
                games_dict[game_id] += 1
            else:
                games_dict[game_id] = 1

    #  find the games where the number of qualifying players is at least player_count
    qualified_game_ids = [game_id for game_id, count in games_dict.items() if count >= player_count]

    # Return the list of qualified games sorted from most to least recent 
    return sorted(qualified_game_ids, reverse=True)
