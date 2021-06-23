import knapsack
import pandas as pd

df = pd.read_csv("data.csv")
df.columns = ['name', 'price', 'score']
df.set_index("name", inplace=True)

budget = 100
team_size = 5

# merge constraints
constant = 1000000
df.price = df.price + constant
df.score = df.score + constant
capacity = 100 + team_size * constant
score, team_members_indexes = knapsack.knapsack(df.price, df.score).solve(capacity)

# unmerge contraints
score = score - team_size * constant
df.price = df.price - constant
df.score = df.score - constant

sub_df = df.iloc[team_members_indexes]
team_members = list(sub_df.index)
best_price = round(sub_df.price.sum(), 2)

msg = "Best team for a budget of " + str(budget)
msg = msg + " million dollars consists of " + str(team_members)
msg = msg + " with a price of " + str(best_price)
msg = msg + " million dollars and a combined score of " + str(score)
print(msg)
