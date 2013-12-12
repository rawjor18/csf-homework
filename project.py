#the stats recorded for the players averages
p1_average = ['Tpm_p1','ast_p1','fgm_p1','ftm_p1','fta_p1','treb_p1','oreb_p1','stl_p1','blk_p1','to_p1','mp_p1','fga_p2','drb_p2']
p2_average = ['Tpm_p2','ast_p2','fgm_p2','ftm_p2','fta_p2','treb_p2','oreb_p2','stl_p2','blk_p2','to_p2','mp_p2','fga_p2','drb_p2']

  
number_of_players = 2
p = float(number_of_players)
number_of_games = 4
n = float(number_of_games)

#the stats recorded for the team averages 
team1_average = ['ast_t1','fga_t1','poss_t1','oposs_t1','mp_t1','fta_t1','orb_t1','drb_t1','fgm_t1','to_t1','drb_t1']
#the stats for the opposing team in each game
opp_game1 = ['fga_opp1','fta_opp1','orb_opp1','drb_opp1','fgm_opp1','to_opp1']
opp_game2 = ['fga_opp2','fta_opp2','orb_opp2','drb_opp2','fgm_opp2','to_opp2']
opp_game3 = ['fga_opp3','fta_opp3','orb_opp3','drb_opp3','fgm_opp3','to_opp3']
opp_game4 = ['fga_opp4','fta_opp4','orb_opp4','drb_opp4','fgm_opp4','to_opp4']

number_of_games = 4
n = float(number_of_games)


leauge_average = ['ppg','ast','fgm','fta','fga','oreb','treb','to','ftm']



#player 1's game statistics
game1_p1 = [16, 4, 8, 3, 3, 2, 2, 1, 4, 6, 30, 12] 
game2_p1 = [12, 5, 5, 1, 1, 3, 2, 2, 5, 3, 28, 14]
game3_p1 = [13, 4, 1, 3, 1, 0, 4, 1, 3, 1, 29, 10]
game4_p1 = [19, 7, 4, 2, 3, 1, 1, 3, 0, 4, 26, 17]

game1_p2 = [14, 3, 7, 4, 0, 4, 1, 6, 7, 1, 33, 18] 
game2_p2 = [21, 1, 7, 3, 1, 5, 0, 9, 5, 3, 35, 5]
game3_p2 = [23, 2, 9, 2, 1, 2, 1, 7, 7, 1, 34, 7]
game4_p2 = [23, 2, 8, 4, 0, 1, 1, 7, 8, 0, 36, 8]


#player's game averages
p1_average[0] = (game1_p1[0] + game2_p1[0] + game3_p1[0] + game4_p1[0]) / n
p1_average[1] = (game1_p1[1] + game2_p1[1] + game3_p1[1] + game4_p1[1]) / n
p1_average[2] = (game1_p1[2] + game2_p1[2] + game3_p1[2] + game4_p1[2]) / n
p1_average[3] = (game1_p1[3] + game2_p1[3] + game3_p1[3] + game4_p1[3]) / n
p1_average[4] = (game1_p1[4] + game2_p1[4] + game3_p1[4] + game4_p1[4]) / n
p1_average[5] = (game1_p1[5] + game2_p1[5] + game3_p1[5] + game4_p1[5]) / n
p1_average[6] = (game1_p1[6] + game2_p1[6] + game3_p1[6] + game4_p1[6]) / n
p1_average[7] = (game1_p1[7] + game2_p1[7] + game3_p1[7] + game4_p1[7]) / n
p1_average[8] = (game1_p1[8] + game2_p1[8] + game3_p1[8] + game4_p1[8]) / n
p1_average[9] = (game1_p1[9] + game2_p1[9] + game3_p1[9] + game4_p1[9]) / n
p1_average[10] = (game1_p1[10] + game2_p1[10] + game3_p1[10] + game4_p1[10]) / n
p1_average[11] = (game1_p1[11] + game2_p1[11] + game3_p1[11] + game4_p1[11]) / n

p2_average[0] = (game1_p2[0] + game2_p2[0] + game3_p2[0] + game4_p2[0]) / n
p2_average[1] = (game1_p2[1] + game2_p2[1] + game3_p2[1] + game4_p2[1]) / n
p2_average[2] = (game1_p2[2] + game2_p2[2] + game3_p2[2] + game4_p2[2]) / n
p2_average[3] = (game1_p2[3] + game2_p2[3] + game3_p2[3] + game4_p2[3]) / n
p2_average[4] = (game1_p2[4] + game2_p2[4] + game3_p2[4] + game4_p2[4]) / n
p2_average[5] = (game1_p2[5] + game2_p2[5] + game3_p2[5] + game4_p2[5]) / n
p2_average[6] = (game1_p2[6] + game2_p2[6] + game3_p2[6] + game4_p2[6]) / n
p2_average[7] = (game1_p2[7] + game2_p2[7] + game3_p2[7] + game4_p2[7]) / n
p2_average[8] = (game1_p2[8] + game2_p2[8] + game3_p2[8] + game4_p2[8]) / n
p2_average[9] = (game1_p2[9] + game2_p2[9] + game3_p2[9] + game4_p2[9]) / n
p2_average[10] = (game1_p2[10] + game2_p2[10] + game3_p2[10] + game4_p2[10]) / n
p2_average[11] = (game1_p2[11] + game2_p2[11] + game3_p2[11] + game4_p2[11]) / n

def game_average(player,game1,game2,game3,game4, index, n):
    player[index] = (game1[index] + game2[index] + game3[index] +game4[index] )

#a dictionary attatching the abreveation of each PLAYER'S statistic with its corrisponding average
stat_dict={}
stat_dict['tpm_p1'] = p1_average[0]
stat_dict['ast_p1'] = p1_average[1]
stat_dict['fgm_p1'] = p1_average[2]
stat_dict['ftm_p1'] = p1_average[3]
stat_dict['fta_p1'] = p1_average[4]
stat_dict['treb_p1'] = p1_average[5]
stat_dict['oreb_p1'] = p1_average[6]
stat_dict['stl_p1'] = p1_average[7]
stat_dict['blk_p1'] = p1_average[8]
stat_dict['to_p1'] = p1_average[9]
stat_dict['mp_p1'] = p1_average[10]
stat_dict['fga_p1'] = p1_average[11]

stat_dict['tpm_p2'] = p2_average[0]
stat_dict['ast_p2'] = p2_average[1]
stat_dict['fgm_p2'] = p2_average[2]
stat_dict['ftm_p2'] = p2_average[3]
stat_dict['fta_p2'] = p2_average[4]
stat_dict['treb_p2'] = p2_average[5]
stat_dict['oreb_p2'] = p2_average[6]
stat_dict['stl_p2'] = p2_average[7]
stat_dict['blk_p2'] = p2_average[8]
stat_dict['to_p2'] = p2_average[9]
stat_dict['mp_p2'] = p2_average[10]
stat_dict['fga_p2'] = p2_average[11]


#dictionary for the TEAM stats
team_dict={}
#team_dict['ast_t1']  = (p1_average[1] + p2_average[1]) / p
#team_dict['fga_t1']  = (p1_average[11] + p2_average[11]) / p
team_dict['poss_t1']  = 'unknown'
team_dict['oposs_t1']  = 'unknown'
team_dict['mp_t1']  = 200
#team_dict['fta_t1'] = (p1_average[7] + p2_average[7]) / p
#team_dict['orb_t1'] = (p1_average[8] + p2_average[8]) / p
#team_dict['drb_t1'] = (p1_average[9] + p2_average[9]) / p
#team_dict['fgm_t1'] = (p1_average[2] + p2_average[2]) / p
#team_dict['to_t1'] = (p1_average[11] + p2_average[11]) / p

def average(key,index,p):
    team_dict[key] = (p1_average[index] + p2_average[index]) / p

average('ast_t1',1, p)
average('fga_t1',11, p)
average('fta_t1',7, p)
average('orb_t1',8, p)
average('drb_t1',9, p)
average('fgm_t1',2, p)
average('to_t1',11, p) 



#dictionary for the OPPONENT stats
team_dict['fga_opp1'] = opp_game1[0] 
team_dict['fta_opp1'] = opp_game1[1]
team_dict['orb_opp1'] = opp_game1[2]
team_dict['drb_opp1'] = opp_game1[3]
team_dict['fgm_opp1'] = opp_game1[4]
team_dict['to_opp1'] = opp_game1[5]

team_dict['fga_opp2'] = opp_game2[0] 
team_dict['fta_opp2'] = opp_game2[1]
team_dict['orb_opp2'] = opp_game2[2]
team_dict['drb_opp2'] = opp_game2[3]
team_dict['fgm_opp2'] = opp_game2[4]
team_dict['to_opp2'] = opp_game2[5]

team_dict['fga_opp3'] = opp_game3[0] 
team_dict['fta_opp3'] = opp_game3[1]
team_dict['orb_opp3'] = opp_game3[2]
team_dict['drb_opp3'] = opp_game3[3]
team_dict['fgm_opp3'] = opp_game3[4]
team_dict['to_opp3'] = opp_game3[5]

team_dict['fga_opp4'] = opp_game4[0] 
team_dict['fta_opp4'] = opp_game4[1]
team_dict['orb_opp4'] = opp_game4[2]
team_dict['drb_opp4'] = opp_game4[3]
team_dict['fgm_opp4'] = opp_game4[4]
team_dict['to_opp4'] = opp_game4[5]


leauge_dict={}

leauge_dict['ppg'] = 

#a loop printing (name)key + '=' + the value of p1_average[] for all statistics
for name,value in team_dict.items():
    print name+'='+str(value)







