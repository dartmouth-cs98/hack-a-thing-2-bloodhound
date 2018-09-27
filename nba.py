from nba_api.stats.endpoints import commonplayerinfo, boxscoreadvancedv2
import pandas

player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)


# Returns the data set in a pandas DataFrame.
avaliableSeasonDF = player_info.available_seasons.get_data_frame()
print (avaliableSeasonDF.at[0, 'SEASON_ID'])

playerInfoDF = player_info.common_player_info.get_data_frame()

boxScoreInfo = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id= "0021700807")

boxScoreDF = boxScoreInfo.player_stats.get_data_frame()
print(boxScoreDF)


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
