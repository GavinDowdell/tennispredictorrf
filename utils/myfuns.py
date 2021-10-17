def update(probs,scores):
    global probs_cum,scores_cum
    probs_cum.append(probs)

    count = 1
    scorenew = scores
    while scorenew in scores_cum:
    	scorenew = scores + '_' + str(count)
    	count = count + 1
    else:
    	scores_cum.append(scorenew)
    
    print(probs_cum)
    print(scores_cum)


def remove_last_cum_val():
	global probs_cum,scores_cum
	probs_cum.pop()
	scores_cum.pop()


def next_point_win_fn(row_in):
    if ((int(row_in.points_for) == 3) & (int(row_in.points_against) < 3) 
    & (int(row_in.games_for) == 5) & (int(row_in.games_against) < 5)):
        row_in.loc[:,'sets_for'] = row_in.loc[:,'sets_for'] + 1
        row_in.loc[:,'games_for'] = 0
        row_in.loc[:,'games_against'] = 0
        row_in.loc[:,'points_for'] = 0
        row_in.loc[:,'points_against'] = 0
        row_in.loc[:,'serving'] =  (row_in.serving + 1)%2
    elif ((int(row_in.points_for) == 3) & (int(row_in.points_against) < 3) 
    & (int(row_in.games_for) == 6) & (int(row_in.games_against) == 5)):
        row_in.loc[:,'sets_for'] = row_in.loc[:,'sets_for'] + 1
        row_in.loc[:,'games_for'] = 0
        row_in.loc[:,'games_against'] = 0
        row_in.loc[:,'points_for'] = 0
        row_in.loc[:,'points_against'] = 0
        row_in.loc[:,'serving'] =  (row_in.serving + 1)%2
    elif ((int(row_in.points_for) == 6) & (int(row_in.points_against) < 6) 
    & (int(row_in.games_for) == 6) & (int(row_in.games_against) == 6)):
        row_in.loc[:,'sets_for'] = row_in.loc[:,'sets_for'] + 1
        row_in.loc[:,'games_for'] = 0
        row_in.loc[:,'games_against'] = 0
        row_in.loc[:,'points_for'] = 0
        row_in.loc[:,'points_against'] = 0
        row_in.loc[:,'serving'] =  (row_in.serving + 1)%2
    elif ((int(row_in.points_for) == 3) & (int(row_in.points_against) < 3)
    &(int(row_in.games_for) != 6)):
        row_in.loc[:,'games_for'] = row_in.loc[:,'games_for'] + 1
        row_in.loc[:,'points_for'] = 0
        row_in.loc[:,'points_against'] = 0
        row_in.loc[:,'serving'] =  (row_in.serving + 1)%2
    elif ((int(row_in.points_for) == 5) & (int(row_in.points_against) == 6) 
    & (int(row_in.games_for) == 6) & (int(row_in.games_against) == 6)):
        row_in.loc[:,'points_against'] = row_in.loc[:,'points_against'] -1
    elif ((int(row_in.points_for) < 6) & (int(row_in.points_against) <= 6) 
    & (int(row_in.games_for) == 6) & (int(row_in.games_against) == 6)):
        row_in.loc[:,'points_for'] = row_in.loc[:,'points_for'] + 1
    elif ((int(row_in.points_for) == 3) & (int(row_in.points_against) == 3)):
        row_in.loc[:,'points_against'] = row_in.points_against - 1
    elif ((int(row_in.points_for) == 2) & (int(row_in.points_against) == 3)):
        row_in.loc[:,'points_against'] = row_in.points_against - 1
    elif (int(row_in.points_for) < 3):
        row_in.loc[:,'points_for'] = row_in.loc[:,'points_for'] + 1

		
def next_point_lose_fn(row_in):
    if ((int(row_in.points_for) < 3) & (int(row_in.points_against) == 3) 
    & (int(row_in.games_for) < 5) & (int(row_in.games_against) == 5)):
        row_in.loc[:,'sets_against'] = row_in.loc[:,'sets_against'] + 1
        row_in.loc[:,'games_for'] = 0
        row_in.loc[:,'games_against'] = 0
        row_in.loc[:,'points_for'] = 0
        row_in.loc[:,'points_against'] = 0
        row_in.loc[:,'serving'] =  (row_in.serving + 1)%2
    elif ((int(row_in.points_for) < 3) & (int(row_in.points_against) == 3) 
    & (int(row_in.games_for) == 5) & (int(row_in.games_against) == 6)):
        row_in.loc[:,'sets_against'] = row_in.loc[:,'sets_against'] + 1
        row_in.loc[:,'games_for'] = 0
        row_in.loc[:,'games_against'] = 0
        row_in.loc[:,'points_for'] = 0
        row_in.loc[:,'points_against'] = 0
        row_in.loc[:,'serving'] =  (row_in.serving + 1)%2
    elif ((int(row_in.points_for) < 6) & (int(row_in.points_against) == 6) 
    & (int(row_in.games_for) == 6) & (int(row_in.games_against) == 6)):
        row_in.loc[:,'sets_against'] = row_in.loc[:,'sets_against'] + 1
        row_in.loc[:,'games_for'] = 0
        row_in.loc[:,'games_against'] = 0
        row_in.loc[:,'points_for'] = 0
        row_in.loc[:,'points_against'] = 0
        row_in.loc[:,'serving'] =  (row_in.serving + 1)%2
    elif ((int(row_in.points_for) < 3) & (int(row_in.points_against) == 3)
    &(int(row_in.games_against) != 6)):
        row_in.loc[:,'games_against'] = row_in.loc[:,'games_against'] + 1
        row_in.loc[:,'points_for'] = 0
        row_in.loc[:,'points_against'] = 0
        row_in.loc[:,'serving'] =  (row_in.serving + 1)%2
    elif ((int(row_in.points_for) == 6) & (int(row_in.points_against) == 5) 
    & (int(row_in.games_for) == 6) & (int(row_in.games_against) == 6)):
        row_in.loc[:,'points_for'] = row_in.loc[:,'points_for'] -1
    elif ((int(row_in.points_for) <= 6) & (int(row_in.points_against) < 6) 
    & (int(row_in.games_for) == 6) & (int(row_in.games_against) == 6)):
        row_in.loc[:,'points_against'] = row_in.loc[:,'points_against'] + 1
    elif ((int(row_in.points_for) == 3) & (int(row_in.points_against) == 3)):
        row_in.loc[:,'points_for'] = row_in.points_for - 1
    elif ((int(row_in.points_for) == 3) & (int(row_in.points_against) == 2)):
        row_in.loc[:,'points_for'] = row_in.points_for - 1
    elif (int(row_in.points_against) < 3):
        row_in.loc[:,'points_against'] = row_in.loc[:,'points_against'] + 1
