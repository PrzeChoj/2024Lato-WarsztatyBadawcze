import numpy as np


class Board:
    def __init__(self, coin_location, exit_location):
        # Board initialization, we start without the coin present
        self.rewards = np.full((5, 5), -1)  # Standard reward for non-special cells
        self.coin_location = coin_location
        self.exit_location = exit_location
        self.rewards[4, 4] = 10  # Reward for the exit


def calculate_utilities_and_policy(gamma, board, with_coin, threshold=0.01, utility=np.zeros((5, 5))):
    policy = np.full((5, 5), ' ')
    actions = ['↑', '↓', '←', '→']
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right movements

    while True:
        delta = 0
        for i in range(5):
            for j in range(5):
                if (not with_coin and (i, j) == board.exit_location) or (with_coin and (
                        (i, j) == board.exit_location or (i, j) == board.coin_location)):  # Skip the exit (or coin if present)
                    # for utility update
                    continue
                max_utility = float('-inf')
                for action, (di, dj) in zip(actions, deltas):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 5 and 0 <= nj < 5:
                        temp_utility = board.rewards[ni, nj] + gamma * utility[ni, nj]
                    else:
                        temp_utility = board.rewards[i, j] + gamma * utility[i, j]  # Stay in place if out-of-bounds
                    if temp_utility > max_utility:
                        max_utility = temp_utility
                        policy[i][j] = action
                delta = max(delta, np.abs(max_utility - utility[i][j]))
                utility[i][j] = max_utility
        if delta < threshold:
            break

    return utility, policy


def run_solution(gamma, board):
    # Calculate utilities and policy with just the exit as reward
    utility_to_exit, policy_to_exit = calculate_utilities_and_policy(gamma, board=board, with_coin=False)

    # Adjust rewards to simulate adding a coin, this way for the option with coin our utilities will take
    # into account the benefit of going to the coin before going to the exit, because of the possibility to
    # reach the exit after collecting the coin, and no possibility of reaching the coin after reaching exit
    board.rewards[2, 2] = 10

    # Assign to temp to not lose the state of utility_to_exit which we want to print out at the end
    temp_utility_to_exit = utility_to_exit.copy()
    # Recalculate utilities and policy with added coin as reward
    utility_with_coin, policy_with_coin = calculate_utilities_and_policy(gamma, board=board, with_coin=True,
                                                                         utility=temp_utility_to_exit)

    print("\nSolution for gamma: ", gamma)

    print("\nPolicy without the coin present (towards exit):")
    print(policy_to_exit)
    print("Utilities\n", utility_to_exit)
    print("\nPolicy with coin present:")
    print(policy_with_coin)
    print("Utilities\n", utility_with_coin)


board1 = Board(coin_location=(2, 2), exit_location=(4, 4))
run_solution(gamma=0.999, board=board1)

board2 = Board(coin_location=(2, 2), exit_location=(4, 4))
run_solution(gamma=0.001, board=board2)
