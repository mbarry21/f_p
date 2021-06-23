import knapsack
import pandas as pd


# read data
df = pd.read_csv("data.csv", header=None)
df.columns = ['name', 'price', 'score']
df.set_index("name", inplace=True)

budget = 100
team_size = 5


# Merging constraints. For this variation of the knapsack problem there exists two constraints: team size and budget.
# Here we merge them by adding a large constant.
constant = 1000000
df.price = df.price + constant
df.score = df.score + constant
capacity = 100 + team_size * constant

# Solve the knapsack problem
score, team_members_indexes = knapsack.knapsack(df.price, df.score).solve(capacity)

# separate constraints
score = score - team_size * constant
df.price = df.price - constant
df.score = df.score - constant

# extract relevant information
sub_df = df.iloc[team_members_indexes]
team_members = list(sub_df.index)
best_price = round(sub_df.price.sum(), 2)

# print
msg = "Best team for a budget of " + str(budget)
msg = msg + " million dollars consists of " + str(team_members)
msg = msg + " with a price of " + str(best_price)
msg = msg + " million dollars and a combined score of " + str(score) + " points"
print(msg)
