from nba_api.stats.endpoints import commonplayerinfo
import pandas

player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)



# Returns the data set in a pandas DataFrame.
seasonsDF = player_info.available_seasons.get_data_frame()
print seasonsDF

# # Returns the raw response of the request.
# print player_info.get_response()
#
# # Returns all data in a JSON string.
# player_info.get_json()
#
# # Returns all data in a dictionary.
# player_info.get_dict()
#
# # Returns all data in a normalized JSON string.
# player_info.get_normalized_json()
#
# # Returns all data in a normalized dictionary.
# player_info.get_normalized_dict()
#
# # Returns a list of all data in a pandas DataFrame structure.
# player_info.get_data_frames()
#
#
#
# # Find players by full name.
# players.find_players_by_full_name('james')
#
# # Find players by first name.
# players.find_players_by_first_name('lebron')
#
# # Find players by last name.
# players.find_players_by_last_name('^(james|love)$')
#
# # Get all players.
# players.get_players()