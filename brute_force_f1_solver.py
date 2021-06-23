import pandas as pd
import itertools


def find_best_team(df, budget, team_size):
    """
    Brute force implementation to find the best team combination with a set budget and team size

    :param df: DataFrame containing names, prices and scores of drivers
    :param budget: Float containing the budget limit
    :param team_size: The number of team members
    :return: A Tuple containing the team members, price and score of the best team combination
    """
    # find all possible team combinations
    combinations = itertools.combinations(df.index, team_size)

    # for tracking best scores
    best_score = 0
    best_price = budget
    best_combination = []

    for combination in combinations:

        sub_df = df.loc[list(combination)]
        price_sum = sub_df.price.sum()

        if price_sum < budget:
            score_sum = sub_df.score.sum()
            if score_sum > best_score:
                best_combination = combination
                best_price = price_sum
                best_score = score_sum

    # rounding due to floating point errors
    return best_combination, round(best_price, 2), round(best_score, 2)

# read data
df = pd.read_csv("data.csv")
df.columns = ['name', 'price', 'score']
df.set_index("name", inplace=True)

budget = 100
team_size = 5

# solve
best_combination, best_price, best_score = find_best_team(df, budget, team_size)

# print
msg = "Best team for a budget of " + str(budget)
msg = msg + " million dollars consists of " + str(best_combination)
msg = msg + " with a price of " + str(best_price)
msg = msg + " million dollars and a combined score of " + str(best_score)
print(msg)
