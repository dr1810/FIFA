import streamlit as st
from data import teams,data,predict_home,predict_away,predict_unrelated_home,predict_unrelated_away,tim,winner
import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
st.title("FIFA: Matches Goal Predictions, Insights")
tabs = st.tabs(["Goals","Win"])
tabs[0].subheader("Goal Predictor")
home = tabs[0].selectbox("Select the Home team",teams)
away = tabs[0].selectbox("Select the Away team",teams)
if home == away:
    tabs[0].write("Enter a valid combination")
elif len(data(home,away)) == 0:
    tabs[0].write(f"{home} will score {predict_unrelated_home(home,away)} goals")
    tabs[0].write(f"{away} will score {predict_unrelated_away(home, away)} goals")
else:
    tabs[0].write(f"{home} will score {predict_home(data(home, away), home,away)} goals")
    tabs[0].write(f"{away} will score {predict_away(data(home, away), home, away)} goals")
tabs[0].subheader("Insights")
if tim(data(home,away)) == None:
    tabs[0].write("These teams haven't encountered each other")
    tabs[0].write(f"{home} scores mean {round(data(home, away)['home_team_score'].mean(), 2)} goals on home turf")
    tabs[0].write(f"{away} scores mean {round(data(home, away)['away_team_score'].mean(), 2)} goals on {home}\'s turf")
else:
    tabs[0].write(f"The first time when both of these teams have encountered was in {tim(data(home,away))}")
    tabs[0].write(f"{home} scores mean {round(data(home,away)['home_team_score'].mean(),2)} goals on home turf")
    tabs[0].write(f"{away} scores mean {round(data(home,away)['away_team_score'].mean(),2)} goals on {home}\'s turf")
h1 = tabs[1].selectbox("Select preferred home team",teams)
a1 = tabs[1].selectbox("Select the preferred  away team",teams)
if h1 == a1:
    tabs[1].write("Enter a valid combination")
else:
    tabs[1].write(f"{h1} will {winner(h1,a1)[0]} with {a1}")
