markdown_text = '''
### IN-MATCH TENNIS PREDICTOR FOR JUNIOR TENNIS

Many Historical Matches have been modelled to produce an in-match Tennis Predictor.
Since tennis has a well structured scoring system provided the probability of winning a point can be estimated the probability 
of winning the set and match from any point within the match can be calculated.
The skill level of both players can be used to estimate the point winning probabilities.
It is best if rankings are used.
The idea is that the rankings of both players, in a consistent ranking system (e.g. current national ranking system), can be entered.
However if rankings are not available the skill level can be estimated as equal, a lot better etc.
Then during the match the current score can be entered and a prediction will be made about
1. Who will win the match (assuming the match is 3 tie break sets)
2. Who will win the current set.

The importance of serving has been modified to make it consistent with Junior Tennis where serving is 
rarely an advantage - hence the current server cannot be entered. 

With that in mind these models are not suitable for predicting the outcomes of professional matches or tennis betting since serve would be an
important predictor in those cases. Hence the model should not be used for these purposes.

The results are meant to demonstrate how win probabilities vary throughout a match, depending upon the match score and how some points are more important than others.\n
With that in mind the probabilties of winning from the current point are shown as well as the probabilities if the next point is 
WON or LOST therefore showing where the key points are.

It is meant for 
1. Fun for parents, coaches or friends watching matches and 
2. As a learning tool where the importance and (lack of importance) of certain points in predicting the match and set outcomes can be understood.
   The idea that some points are more important than others can now be understood and actually quantified.
   With that in mind a cumulative graph is also updated as the match progresses showing the progression of probabilities through the match plotted against the match score.

I will probably be updating the model regularly
Enjoy!
'''
markdown_text1 = '''
Welcome to the UTR In-Match Win Predictor.
The predictor uses a Mathematical model, based upon many historical matches, to estimate the probability of a player winning both the match (assuming the match is 3 tie break sets) and the current set.
It is based upon \n
1. The current score within the match \n
2. The UTR of both players correct to two decimal places which is used to estimate the difference in ability of the two players\n
'''

#TO USE

markdown_text2 = '''
Simply enter the UTR values of both players to two decimal places. If UTR values are not available then use the General Comparison indicators Equal, Moderately Better etc.
This gives an estimate of the skill level of both players prior to the match. The model blends together the UTR information and the current match score to estimate the probability of winning. As the match develops the rankings become less important compared to the match score.
'''

markdown_text2a = '''
Now enter the current match score by using the appropriate radio buttons.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Based upon these pieces of information both the match and set winning probabilities will be updated.

Since it is anticipated the tool will often be used for Juniors and developing players where serving it less important the current server is not used to determine the probability.

The results show how win probabilities vary throughout a match depending upon the match score and demonstrate how some points are more important than others.\n
With that in mind the probabilties of winning from the current point are shown as well as the probabilities if the next point is 
WON or LOST. On key points these probabilities will vary significantly between winning and losing the current point, hence quantifying it as an important point.

It is meant for \n
1. Fun for parents or friends watching junior matches and \n
2. As a learning tool where the importance and (lack of importance) of certain points in predicting the match and set outcomes can be understood.
   The idea that some points are more important than others can now be understood and actually quantified.
   
'''

markdown_text3 = '''
I started this project when my daughter was playing junior tennis. Although she played nice tennis she seemed to inevitably lose key or big points. Interestingly, however when I mentioned this to her she did not really have a concept if what "big" points meant and certainly had no way to quantify them. Hence I decided to build a model to demonstrate these concepts to her.

My plan was to use lots of professional matches to build a statistical model to relate any particular match state (as given by match score) to the probability of winning the current set and the match. I also intended to incorporate the difference in rankings into the model to account for the difference in underlying abilities of the two players. Hence if a players is 20 ranking points below another but is up 3-1 40-15 the model would give the probability of this player going on win the set and match from this point. This is obviously going to be a different probability if the playing winning was the higher ranked player. Finally I wanted to modify this model so it could be applied to junior tennis as a learning tool.

To build such a model where each match state and ranking combination could be translated to the probability of winning the set and match a large amount of match point by point data would be required - this could be described as fully empirical approach. However to my surprise when I started looking for repositories of this type of data it became clear that this data is not readily publicly available. I am certain betting companies would have access to this data to help them set prices but it would be proprietary so it makes sense that it isn't easily available

Hence I decided upon an alternative model - a semi-empirical approach. Since tennis has a well structured scoring system, provided the probability of winning a single point can be estimated for each player (more on this later) then the probability of winning the set and match from any point within the match can be calculated via probability theory (For those with a mathematical inclination see Taking Chances by John Haigh for some details on how these probabilities are calculated). 

However, as alluded to above, to use this approach the estimated probability of both players winning a single point still needs to be calculated and this value must be dependent upon relative skill level. To do this I obtained some point winning ratio's and rankings from completed matches at various tennis sites - which do regularly provide this data for Grand Slam, ATP and WTA data. From this the data the winning probability vs ranking difference can be calculated as shown in the figure below. It is from this data the point winning probabilities are obtained when rankings from the same ranking system are entered. The idea is that the rankings of both players, in a consistent ranking system (e.g. current national ranking system), can be entered and this ranking difference will be used to obtain point winning probabilities from the professional data I obtained. However if rankings are not available the skill level can be estimated as equal, a lot better etc. It is obviously not perfect however it should provide a decent approximation of point winning probabilities.
If you are prepared to log points won during the match the skill level for that particular match should be more accurate if that information is used.
'''

markdown_text4 = '''
It may seem that these point winning probabilities exist in a fairly narrow range. For example even when the rankings are 100 places apart the higher ranked player has only a 52% chance of winning an individual point. However the interesting point about the tennis scoring system is the relationship between point winning, game winning, set winning and match winning probabilites. For example, if a player has an individual point winning probability of 55% then the probability of them winning a game based upon that point winning probability is 62%, the set is 82% and the match is 91%, assumming the match hasn't yet started. However these probabilities quickly change once the match starts and the current score gets factored in. For example for the above situation if the set score progresses to 1-3 the probability of winning the set becomes a 50-50 proposition.

 

Once the skill level has been estimated the current match score can be entered and a prediction will be made about

1. Who will win the match (assuming the match is 3 tie break sets)
2. Who will win the current set.
 

The results are meant to demonstrate how win probabilities vary through a match and how some points are more important than others. With that in mind the probabilties of winning from the current point are shown as well as the probabilities if the next point is won or lost, therefore showing where the key points are. For really important points the winning probabilities will vary a great deal between winning and losing the next point. An example of this is demonstrated in the graph below.
'''

markdown_text5 = '''
The importance of serving has been modified to make it consistent with Junior Tennis where serving is rarely an advantage and often a disadvantage.

With that in mind these models are not suitable for predicting the outcomes of professional matches or tennis betting since serve would be an
important predictor in those cases. Hence the model should not be used for these purposes.

 

In general the model is meant for 

 
1. Fun for parents or friends watching junior matches and 
2. As a learning tool where the importance and (lack of importance) of certain points in predicting the match and set outcomes can be understood and quantified.


I will probably be updating the model regularly
Enjoy!
'''