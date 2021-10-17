import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils.indicators import *
from markdown_to_use.markdowns import *
from utils.myfuns import *
import pandas as pd
import numpy as np
import time
import os
import pathlib
'''
__file__ is a variable that contains the path to the module that is currently being imported. 
Python creates a __file__ variable for itself when it is about to import a module.
'''
DATA_PATH = pathlib.Path(__file__).parent.parent.joinpath("data").resolve()
df = pd.read_csv(DATA_PATH.joinpath('dataset.csv'))
combined = pd.read_csv(DATA_PATH.joinpath('ranking_diff_to_utr_diff.csv'))
utr_diff = np.array(combined['utr_diff'])
ranking_diff = np.array(combined['ranking_diff'])



def create_layout(app):
		print("Actual layout of the app\n\n")
		return html.Div([html.H1('UTR In-Match Win Predictor',style={'text-align':'center'}),dcc.Markdown(markdown_text1),html.Strong('TO USE'),
		html.P(),html.Strong('1. Estimate the Skill level of both players'),
		dcc.Markdown(markdown_text2),
		html.P(),html.Strong('2. Enter the current score of the match'),
		dcc.Markdown(markdown_text2a),
		html.P([
		html.Div([html.Span(html.Label('1.   First Enter Skill Level'),style={'text-decoration':'underline','color': '#ff0000'}),html.Br(), html.P('Use general comparisons OR the rankings. Note to use the general comparisons both UTR values need to be set to 0',style={'text-decoration':'underline'}),
			html.Div(html.Label('General Comparison. My Player, when compared to the opposition is')),html.P(),dcc.RadioItems(id='skill_level',options=[{'label': i, 'value': i} for i in available_skill_indicators],value='Equal',labelStyle={'display': 'inline-block'}),html.P(),
			html.Div([html.Div([html.Label("\nMy UTR"),html.Div(dcc.Input(id='myrank',value='0', type='text'))]),html.Br(),
					  html.Span(html.Label('2.   Now Enter the Match Score and Check Out the Probabilities'),style={'text-decoration':'underline','color': '#ff0000'}),html.Br(),html.Br(),
					  html.Label('My Sets'),dcc.RadioItems(id='mysets',options=[{'label': i, 'value': i} for i in available_set_indicators],value=0),
					  html.Label('My Games'),dcc.RadioItems(id='mygames',options=[{'label': i, 'value': i} for i in available_game_indicators],value=0),
					  html.Label('My Points within  a normal game'),dcc.RadioItems(id='mypoints',options=[{'label': i, 'value': i} for i in available_point_indicators],value='0'),
					  html.Label('My Points within a tiebreaker (only use at 6-6 game score)'),dcc.RadioItems(id='mytiebreakpoints',options=[{'label': i, 'value': i} for i in tiebreakpoinyts],value=0)],
					  style={'width': '48%', 'display': 'inline-block'}),
					  html.Div([html.Div([html.Label("Opposition UTR"),html.Div(dcc.Input(id='yourrank',value='0', type='text'))]),html.Br(),html.Br(),html.Br(),html.Br(),
					  html.Label('Opposition Sets'),dcc.RadioItems(id='yoursets',options=[{'label': i, 'value': i} for i in available_set_indicators],value=0),
					  html.Label('Opposition Games'),dcc.RadioItems(id='yourgames',options=[{'label': i, 'value': i} for i in available_game_indicators],value=0),
					  html.Label('Opposition Points'),dcc.RadioItems(id='yourpoints',options=[{'label': i, 'value': i} for i in available_point_indicators],value='0'),
					  html.Label('Opposition Points within a tiebreaker (only use at 6-6)'),dcc.RadioItems(id='yourtiebreakpoints',options=[{'label': i, 'value': i} for i in tiebreakpoinyts],value=0)],
					  style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
				]),
		html.Br(),html.Br(),
		html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
		html.H2(id='get_current_score',style={'text-align':'center'}),html.Br(),
		html.H2('CURRENT POINT GRAPH',style={'text-align':'center'}),
		html.Div(dcc.Graph(id='indicator-graphic')),html.Br(),html.Br(),
		html.Div([html.Div(html.H2(id='output-text'),style={'width': '48%', 'text-align': 'center', 'display': 'inline-block'}),html.Div(html.H2(id='output-text-ci'),style={'width': '48%', 'float': 'right', 'display': 'inline-block'})])])])


def demo_callbacks(app):
	print("callbacks of the app\n\n")
	@app.callback(
		dash.dependencies.Output('output-text', 'children'),
		[dash.dependencies.Input('skill_level', 'value'),
		 dash.dependencies.Input('myrank', 'value'),
		 dash.dependencies.Input('yourrank', 'value'),
		 dash.dependencies.Input('mysets', 'value'),
		 dash.dependencies.Input('yoursets', 'value'),
		 dash.dependencies.Input('mygames', 'value'),
		 dash.dependencies.Input('yourgames', 'value'),
		 dash.dependencies.Input('mypoints', 'value'),
		 dash.dependencies.Input('yourpoints', 'value'),
		 dash.dependencies.Input('mytiebreakpoints', 'value'),
		 dash.dependencies.Input('yourtiebreakpoints', 'value')])

	def update_score(skill_level,myrank, yourrank,mysets,yoursets,
					 mygames, yourgames,mypoints,yourpoints,
					 mytiebreakpoints,yourtiebreakpoints,serving='Yes'):
   
		
			if ((mytiebreakpoints == 0) & (yourtiebreakpoints == 0)):
				score_str = str(mysets) + ':' + str(yoursets) +  ',' + str(mygames) + ':' + str(yourgames) +  ',' + str(mypoints) + ':' + str(yourpoints)
			else:
				score_str = str(mysets) + ':' + str(yoursets) +  ',' + str(mygames) + ':' + str(yourgames) +  ',' + str(mytiebreakpoints) + ':' + str(yourtiebreakpoints)

			if ((myrank=='0') & (yourrank=='0')):
				ranking_diff_use = skills[skill_level]
			else:	
				input_utr_diff = float(myrank) - float(yourrank)
				print(input_utr_diff)
				ranking_diff_use = int(ranking_diff[(np.abs(utr_diff - input_utr_diff)).argmin()])
				ranking_diff_use = round((ranking_diff_use/5));
				ranking_diff_use = min(max(ranking_diff_use,-38),38)
				print(ranking_diff_use)
				

			mypoints = points[mypoints]
			yourpoints = points[yourpoints]
			serving = serve[serving]
			if 	((mypoints == 4) & (yourpoints == 3)):
				 mypoints = 3
				 yourpoints = 2
			elif ((mypoints == 3) & (yourpoints == 4)):
				 mypoints = 2
				 yourpoints = 3	
			elif ((mypoints == 3) & (yourpoints == 3)):
				 mypoints = 3
				 yourpoints = 3
				 
			
			idx =((df.serving == serving) & (df.sets_for == mysets) & (df.sets_against == yoursets) & (df.games_for == mygames) &
			(df.games_against == yourgames) & (df.points_for == mypoints) &(df.points_against == yourpoints) &(df.ranking_diff_use == ranking_diff_use));
			if ((mygames == 6) & (yourgames == 6)):
				if ((mytiebreakpoints > 6) & (mytiebreakpoints == yourtiebreakpoints)):
					mytiebreakpoints = 6
					yourtiebreakpoints = 6
				elif  ((mytiebreakpoints > 6) & (mytiebreakpoints > yourtiebreakpoints)):
					mytiebreakpoints = 6
					yourtiebreakpoints = 5
				elif  ((yourtiebreakpoints > 6) & (mytiebreakpoints < yourtiebreakpoints)):
					mytiebreakpoints = 5
					yourtiebreakpoints = 6
				idx =((df.serving == serving) & (df.sets_for == mysets) & (df.sets_against == yoursets) & (df.games_for == mygames) &
				(df.games_against == yourgames) & (df.points_for == mytiebreakpoints) &(df.points_against == yourtiebreakpoints) &(df.ranking_diff_use == ranking_diff_use));

			
			tmp = df.loc[idx,'prob_match_win']
			tmp1 = np.array(tmp)
			tmp1 = np.maximum(round(np.array(tmp1[0])*100,),1)
			print(tmp1,score_str)

			tmp2 = str(tmp1).split('.')[0]
			return 'Your Probability of Winning the match is  {}%'.format(tmp2)


	@app.callback(
		dash.dependencies.Output('output-text-ci', 'children'),
		[dash.dependencies.Input('skill_level', 'value'),
		 dash.dependencies.Input('myrank', 'value'),
		 dash.dependencies.Input('yourrank', 'value'),
		 dash.dependencies.Input('mysets', 'value'),
		 dash.dependencies.Input('yoursets', 'value'),
		 dash.dependencies.Input('mygames', 'value'),
		 dash.dependencies.Input('yourgames', 'value'),
		 dash.dependencies.Input('mypoints', 'value'),
		 dash.dependencies.Input('yourpoints', 'value'),
		 dash.dependencies.Input('mytiebreakpoints', 'value'),
		 dash.dependencies.Input('yourtiebreakpoints', 'value')])

	def update_score(skill_level,myrank, yourrank,mysets,yoursets,
					 mygames, yourgames,mypoints,yourpoints,
					 mytiebreakpoints,yourtiebreakpoints,serving='Yes'):
		if ((myrank=='0') & (yourrank=='0')):
			ranking_diff_use = skills[skill_level]
		else:	
			
			input_utr_diff = float(myrank) - float(yourrank)
			print(input_utr_diff)
			ranking_diff_use = int(ranking_diff[(np.abs(utr_diff - input_utr_diff)).argmin()])
			ranking_diff_use = round((ranking_diff_use/5));# remember the difference in rank must be divided by 5
			print(ranking_diff_use)
			ranking_diff_use = min(max(ranking_diff_use,-38),38)
			print(ranking_diff_use)
		mypoints = points[mypoints]
		yourpoints = points[yourpoints]
		serving = serve[serving]
		if 	((mypoints == 4) & (yourpoints == 3)):
			 mypoints = 3
			 yourpoints = 2
		elif ((mypoints == 3) & (yourpoints == 4)):
			 mypoints = 2
			 yourpoints = 3	
		elif ((mypoints == 3) & (yourpoints == 3)):
			 mypoints = 3
			 yourpoints = 3	
		idx =((df.serving == serving) & (df.sets_for == mysets) & (df.sets_against == yoursets) & (df.games_for == mygames) &
		(df.games_against == yourgames) & (df.points_for == mypoints) &(df.points_against == yourpoints) &(df.ranking_diff_use == ranking_diff_use));
		if ((mygames == 6) & (yourgames == 6)):
			if ((mytiebreakpoints > 6) & (mytiebreakpoints == yourtiebreakpoints)):
				mytiebreakpoints = 6
				yourtiebreakpoints = 6
			elif  ((mytiebreakpoints > 6) & (mytiebreakpoints > yourtiebreakpoints)):
				mytiebreakpoints = 6
				yourtiebreakpoints = 5
			elif  ((yourtiebreakpoints > 6) & (mytiebreakpoints < yourtiebreakpoints)):
				mytiebreakpoints = 5
				yourtiebreakpoints = 6
			idx =((df.serving == serving) & (df.sets_for == mysets) & (df.sets_against == yoursets) & (df.games_for == mygames) &
			(df.games_against == yourgames) & (df.points_for == mytiebreakpoints) &(df.points_against == yourtiebreakpoints) &(df.ranking_diff_use == ranking_diff_use));


		tmp = df.loc[idx,'prob_set_win']
		tmp1 = np.array(tmp)
		tmp1 = np.maximum(round(np.array(tmp1[0])*100),1)
		tmp2 = str(tmp1).split('.')[0]
		return 'Your Probability of Winning the set is  {}%.'.format(tmp2)


	@app.callback(
		dash.dependencies.Output('indicator-graphic', 'figure'),
		[dash.dependencies.Input('skill_level', 'value'),
		 dash.dependencies.Input('myrank', 'value'),
		 dash.dependencies.Input('yourrank', 'value'),
		 dash.dependencies.Input('mysets', 'value'),
		 dash.dependencies.Input('yoursets', 'value'),
		 dash.dependencies.Input('mygames', 'value'),
		 dash.dependencies.Input('yourgames', 'value'),
		 dash.dependencies.Input('mypoints', 'value'),
		 dash.dependencies.Input('yourpoints', 'value'),
		 dash.dependencies.Input('mytiebreakpoints', 'value'),
		 dash.dependencies.Input('yourtiebreakpoints', 'value')])

	def update_graph(skill_level,myrank, yourrank,mysets,yoursets,
					 mygames, yourgames,mypoints,yourpoints,
					 mytiebreakpoints,yourtiebreakpoints,serving='Yes'):
		if ((myrank=='0') & (yourrank=='0')):
			ranking_diff_use = skills[skill_level]
		else:	

			input_utr_diff = float(myrank) - float(yourrank)
			print(input_utr_diff)
			ranking_diff_use = int(ranking_diff[(np.abs(utr_diff - input_utr_diff)).argmin()])
			ranking_diff_use = round((ranking_diff_use/5));# remember the difference in rank must be divided by 5
			ranking_diff_use = min(max(ranking_diff_use,-38),38)
			print(ranking_diff_use)
		mypoints = points[mypoints]
		yourpoints = points[yourpoints]
		serving = serve[serving]
		if 	((mypoints == 4) & (yourpoints == 3)):
			 mypoints = 3
			 yourpoints = 2
		elif ((mypoints == 3) & (yourpoints == 4)):
			 mypoints = 2
			 yourpoints = 3	
		elif ((mypoints == 3) & (yourpoints == 3)):
			 mypoints = 3
			 yourpoints = 3	
		
		idx =((df.serving == serving) & (df.sets_for == mysets) & (df.sets_against == yoursets) & (df.games_for == mygames) &
		(df.games_against == yourgames) & (df.points_for == mypoints) &(df.points_against == yourpoints) &(df.ranking_diff_use == ranking_diff_use));
		if ((mygames == 6) & (yourgames == 6)):
			if ((mytiebreakpoints > 6) & (mytiebreakpoints == yourtiebreakpoints)):
				mytiebreakpoints = 6
				yourtiebreakpoints = 6
			elif  ((mytiebreakpoints > 6) & (mytiebreakpoints > yourtiebreakpoints)):
				mytiebreakpoints = 6
				yourtiebreakpoints = 5
			elif  ((yourtiebreakpoints > 6) & (mytiebreakpoints < yourtiebreakpoints)):
				mytiebreakpoints = 5
				yourtiebreakpoints = 6
			idx =((df.serving == serving) & (df.sets_for == mysets) & (df.sets_against == yoursets) & (df.games_for == mygames) &
			(df.games_against == yourgames) & (df.points_for == mytiebreakpoints) &(df.points_against == yourtiebreakpoints) &(df.ranking_diff_use == ranking_diff_use));

		tmp = df.loc[idx,'prob_match_win']
		tmp_all = df.loc[idx,:]
		tmp1 = np.array(tmp)
		tmp1 = np.maximum(round(np.array(tmp1[0])*100),1)
		tmp = df.loc[idx,'prob_set_win']
		tmp2 = np.array(tmp)
		tmp2 = np.maximum(round(np.array(tmp2[0])*100),1)
		tmp_win = tmp_all.iloc[:,:8]
		next_point_win_fn(tmp_win)
		tmp_win.reset_index(inplace=True,drop=True)	
		idxnext_point_win =((df.serving == tmp_win.loc[0,'serving']) & 
		  (df.sets_for == tmp_win.loc[0,'sets_for']) & 
		  (df.sets_against == tmp_win.loc[0,'sets_against']) & 
		  (df.games_for == tmp_win.loc[0,'games_for']) &
		  (df.games_against == tmp_win.loc[0,'games_against']) & 
		  (df.points_for == tmp_win.loc[0,'points_for']) &
		  (df.points_against == tmp_win.loc[0,'points_against']) &
		  (df.ranking_diff_use == tmp_win.loc[0,'ranking_diff_use']));
						
		tmp_win_next = df.loc[idxnext_point_win,'prob_match_win']                  
		tmp_win_next1 = np.array(tmp_win_next)
		if sum(idxnext_point_win) == 0:
			tmp_win_next1 = 100
			tmp_win_next_set1 = 100	
		else:
			tmp_win_next1 = np.maximum(round(np.array(tmp_win_next1[0])*100),1) 
			print(tmp_win_next1)
			tmp_win_next_set = df.loc[idxnext_point_win,'prob_set_win']                  
			tmp_win_next_set1 = np.array(tmp_win_next_set)
			tmp_win_next_set1 = np.maximum(round(np.array(tmp_win_next_set1[0])*100),1)
			print(tmp_win_next_set1)
			if(int(df.loc[idxnext_point_win,'sets_for']) > int(df.loc[idx,'sets_for'])):
				tmp_win_next_set1 = 100
				print(tmp_win_next_set1)
		tmp_lose = tmp_all.iloc[:,:8]
		next_point_lose_fn(tmp_lose)	
		tmp_lose.reset_index(inplace=True,drop=True)	
		idxnext_point_lose =((df.serving == tmp_lose.loc[0,'serving']) & 
		  (df.sets_for == tmp_lose.loc[0,'sets_for']) & 
		  (df.sets_against == tmp_lose.loc[0,'sets_against']) & 
		  (df.games_for == tmp_lose.loc[0,'games_for']) &
		  (df.games_against == tmp_lose.loc[0,'games_against']) & 
		  (df.points_for == tmp_lose.loc[0,'points_for']) &
		  (df.points_against == tmp_lose.loc[0,'points_against']) &
		  (df.ranking_diff_use == tmp_lose.loc[0,'ranking_diff_use']));
						
		tmp_lose_next = df.loc[idxnext_point_lose,'prob_match_win']                  
		tmp_lose_next1 = np.array(tmp_lose_next)
		if sum(idxnext_point_lose) == 0:
			tmp_lose_next1 = 0
			tmp_lose_next_set1 = 0
		else:
			tmp_lose_next1 = np.maximum(round(np.array(tmp_lose_next1[0])*100),1)
			print(tmp_lose_next1)
			tmp_lose_next_set = df.loc[idxnext_point_lose,'prob_set_win']                  
			tmp_lose_next_set1 = np.array(tmp_lose_next_set)
			tmp_lose_next_set1 = np.maximum(round(np.array(tmp_lose_next_set1[0])*100),1)
			print(tmp_lose_next_set1)
			if(int(df.loc[idxnext_point_lose,'sets_against']) > int(df.loc[idx,'sets_against'])):
				tmp_lose_next_set1 = 0
				print(tmp_lose_next_set1)
		
		data = [go.Bar(x=['YOUR CURRENT PROBABILITY OF WINNING THE MATCH IS {}%.'.format(tmp1),'YOUR CURRENT PROBABILITY OF WINNING THE SET IS {}%.'.format(tmp2)],y=[tmp1,tmp2],opacity=0.6,marker={'color':['rgb(58,200,225)','rgb(58,200,225)']}, name='Win Probabilities From The Current Point',text=[tmp1,tmp2], textposition = 'auto'),
				go.Bar(x=['YOUR CURRENT PROBABILITY OF WINNING THE MATCH IS {}%.'.format(tmp1),'YOUR CURRENT PROBABILITY OF WINNING THE SET IS {}%.'.format(tmp2)],y=[tmp_win_next1,tmp_win_next_set1],opacity=0.6,marker={'color':['rgba(204,204,204,1)','rgba(204,204,204,1)']}, name='Win Probabilities If You Win The Next Point',text=[tmp_win_next1,tmp_win_next_set1], textposition = 'auto'),
				go.Bar(x=['YOUR CURRENT PROBABILITY OF WINNING THE MATCH IS {}%.'.format(tmp1),'YOUR CURRENT PROBABILITY OF WINNING THE SET IS {}%.'.format(tmp2)],y=[tmp_lose_next1,tmp_lose_next_set1],opacity=0.6,marker={'color':['rgb(158,202,225)','rgb(158,202,225)']}, name='Win Probabilities If You Lose The Next Point',text=[tmp_lose_next1,tmp_lose_next_set1], textposition = 'auto')]
		layout = go.Layout(xaxis={'title': 'Player Win Probabilities'},yaxis={'title': 'win probability','range':[0,100],'visible':True,'mirror':'allticks', 'showline':True},legend=dict(x=0.40, y=1.2),barmode='group')
		fig = go.Figure(data=data,layout=layout)
		return fig

	@app.callback(
		dash.dependencies.Output('get_current_score', 'children'),
		[dash.dependencies.Input('skill_level', 'value'),
		 dash.dependencies.Input('myrank', 'value'),
		 dash.dependencies.Input('yourrank', 'value'),
		 dash.dependencies.Input('mysets', 'value'),
		 dash.dependencies.Input('yoursets', 'value'),
		 dash.dependencies.Input('mygames', 'value'),
		 dash.dependencies.Input('yourgames', 'value'),
		 dash.dependencies.Input('mypoints', 'value'),
		 dash.dependencies.Input('yourpoints', 'value'),
		 dash.dependencies.Input('mytiebreakpoints', 'value'),
		 dash.dependencies.Input('yourtiebreakpoints', 'value')])

	def update_score(skill_level,myrank, yourrank,mysets,yoursets,
					 mygames, yourgames,mypoints,yourpoints,
					 mytiebreakpoints,yourtiebreakpoints,serving='Yes'):
    
		
			if ((mytiebreakpoints == 0) & (yourtiebreakpoints == 0)):
				score_str = str(mysets) + ':' + str(yoursets) +  ',' + str(mygames) + ':' + str(yourgames) +  ',' + str(mypoints) + ':' + str(yourpoints)
			else:
				score_str = str(mysets) + ':' + str(yoursets) +  ',' + str(mygames) + ':' + str(yourgames) +  ',' + str(mytiebreakpoints) + ':' + str(yourtiebreakpoints)
			return 'CURRENT SCORE IS  {}.'.format(score_str)


