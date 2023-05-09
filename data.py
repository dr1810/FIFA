import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.tree import DecisionTreeClassifier
file = pd.read_csv("C:\\Users\\dharu\\PycharmProjects\\footballgoals\\new_data.csv")
teams = list(set(file["away_team"].unique()).union(set(file["home_team"].unique())))
year = list(file["date"].unique())

def data(home,away):
    data = file[(file["home_team"] == home) & (file["away_team"]==away)]
    return data
def predict_home(data,home,away):
    data = data[((data["home_team"] == home) & (data["away_team"] == away))]
    param1 = int(data[data["away_team"] == away]["away_team_fifa_rank"].mean())
    param2 = int(data[data["home_team"] == home]["home_team_total_fifa_points"].mean())
    param3 = int(data[data["home_team"] == home]["home_team_goalkeeper_score"].mean())
    param4 = int(data[data["home_team"] == home]["home_team_mean_defense_score"].mean())
    param5 = int(data[data["home_team"] == home]["home_team_mean_offense_score"].mean())
    param6 = int(data[data["home_team"] == home]["home_team_mean_midfield_score"].mean())
    pre = np.array([param1, param2, param3, param4, param5, param6]).reshape(1, -1)
    model = LinearRegression()
    stan = StandardScaler()
    model.fit(stan.fit_transform(data[["away_team_fifa_rank", "home_team_total_fifa_points", "home_team_goalkeeper_score",
                    "home_team_mean_defense_score", "home_team_mean_offense_score", "home_team_mean_midfield_score"]]),
              data["home_team_score"])
    return int(model.predict(stan.fit_transform(pre)))
def predict_away(data,home,away):
    data = data[((data["home_team"] == home) & (data["away_team"] == away))]
    param1 = int(data[data["home_team"] == home]["home_team_fifa_rank"].mean())
    param2 = int(data[data["away_team"] == away]["away_team_total_fifa_points"].mean())
    param3 = int(data[data["away_team"] == away]["neutral_location"].mean())
    param4 = int(data[data["away_team"] == away]["away_team_goalkeeper_score"].mean())
    param5 = int(data[data["away_team"] == away]["away_team_mean_defense_score"].mean())
    param6 = int(data[data["away_team"] == away]["away_team_mean_offense_score"].mean())
    param7 = int(data[data["away_team"] == away]["away_team_mean_midfield_score"].mean())
    pre = np.array([param1, param2, param3, param4, param5, param6, param7]).reshape(1, -1)
    model = LinearRegression()
    stan = StandardScaler()
    model.fit(stan.fit_transform(data[["home_team_fifa_rank", "away_team_total_fifa_points", "neutral_location",
                    "away_team_goalkeeper_score", "away_team_mean_defense_score", "away_team_mean_offense_score",
                    "away_team_mean_midfield_score"]]), data["away_team_score"])
    return int(model.predict(stan.fit_transform(pre)))
def predict_unrelated_home(home,away):
    data = file[((file["home_team"] == home) | (file["away_team"] == away))]
    param1 = int(data[data["away_team"] == away]["away_team_fifa_rank"].mean())
    param2 = int(data[data["home_team"] == home]["home_team_total_fifa_points"].mean())
    param3 = int(data[data["home_team"] == home]["home_team_goalkeeper_score"].mean())
    param4 = int(data[data["home_team"] == home]["home_team_mean_defense_score"].mean())
    param5 = int(data[data["home_team"] == home]["home_team_mean_offense_score"].mean())
    param6 = int(data[data["home_team"] == home]["home_team_mean_midfield_score"].mean())
    pre = np.array([param1, param2, param3, param4, param5, param6]).reshape(1, -1)
    model = LinearRegression()
    stan = StandardScaler()
    model.fit(
        stan.fit_transform(data[["away_team_fifa_rank", "home_team_total_fifa_points", "home_team_goalkeeper_score",
                                 "home_team_mean_defense_score", "home_team_mean_offense_score",
                                 "home_team_mean_midfield_score"]]),
        data["home_team_score"])
    return int(model.predict(stan.fit_transform(pre)))
def predict_unrelated_away(home,away):
    data = file[(file["home_team"] == home) | (file["away_team"] == away)]
    param1 = int(data[data["home_team"] == home]["home_team_fifa_rank"].mean())
    print(param1)
    param2 = int(data[data["away_team"] == away]["away_team_total_fifa_points"].mean())
    param3 = int(data[data["away_team"] == away]["neutral_location"].mean())
    param4 = int(data[data["away_team"] == away]["away_team_goalkeeper_score"].mean())
    param5 = int(data[data["away_team"] == away]["away_team_mean_defense_score"].mean())
    param6 = int(data[data["away_team"] == away]["away_team_mean_offense_score"].mean())
    param7 = int(data[data["away_team"] == away]["away_team_mean_midfield_score"].mean())
    pre = np.array([param1, param2, param3, param4, param5, param6, param7]).reshape(1, -1)
    model = LinearRegression()
    stan = StandardScaler()
    model.fit(stan.fit_transform(data[["home_team_fifa_rank", "away_team_total_fifa_points", "neutral_location",
                    "away_team_goalkeeper_score", "away_team_mean_defense_score", "away_team_mean_offense_score",
                    "away_team_mean_midfield_score"]]), data["away_team_score"])
    return int(model.predict(stan.fit_transform(pre)))
def tim(data):
    dat = data['date'].sort_values()
    if len(data) == 0:
        pass
    else:
        return (f"{dat.min()}")
def winner(home,away):
    data = file[(file["home_team"] == home) | (file["away_team"] == away)]
    param1 = int(file[file["away_team"] == away]["away_team_fifa_rank"].mean())
    lst = []
    features = dict(file.corr()["home_team_score"])
    for i in features:
        if features[i] > 0:
            lst.append(i)
    arr = [param1]
    for i in range(1, len(lst)):
        param = int(data[data["home_team"] == home][lst[i]].mean())
        arr.append(param)
    lab = LabelEncoder()
    labels = lab.fit_transform(data["home_team_result"])
    X = data[lst]
    y = labels
    model = DecisionTreeClassifier()
    model.fit(X,y)
    return lab.inverse_transform(model.predict(np.array(arr).reshape(1,-1)))

