import random
import matplotlib.pyplot as plt
import seaborn as sns


class Maze:
    def __init__(self):
        self.width = 7
        self.height = 7
        self.start = (5, 1)
        self.finish = (6, 7)
        self.obstacles = {
            1: [2],
            2: [2, 3, 4, 6, 7],
            3: [],
            4: [2, 4, 6],
            5: [2, 4],
            6: [2, 4, 5],
            7: [2]
        }
        self.action_space = ['up', 'down', 'left', 'right']
        self.position = self.start

    def reset(self):
        self.position = self.start
        return self.position

    def step(self, action):
        row, col = self.position

        if action == 'up' and row > 1 and col not in self.obstacles[row - 1]:
            row -= 1
        elif action == 'down' and row < self.height and col not in self.obstacles[row + 1]:
            row += 1
        elif action == 'left' and col > 1 and col - 1 not in self.obstacles[row]:
            col -= 1
        elif action == 'right' and col < self.width and col + 1 not in self.obstacles[row]:
            col += 1

        self.position = (row, col)

        observation = self.position
        reward = 5 if self.position == self.finish else -1
        terminated = self.position == self.finish

        return observation, reward, terminated

    def __str__(self):
        maze = ''
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                if (i, j) == self.start:
                    maze += 'S'
                elif (i, j) == self.finish:
                    maze += 'F'
                elif (i, j) == self.position:
                    maze += 'A'
                elif i in self.obstacles and j in self.obstacles[i]:
                    maze += 'X'
                else:
                    maze += ' '
            maze += '\n'
        return maze


class Agent:
    def __init__(self, env):
        self.env = env
        self.actions = env.action_space
        self.state = env.reset()
        self.state_values = {}

        for i in range(1, env.height + 1):
            for j in range(1, env.width + 1):
                if i in env.obstacles and j in env.obstacles[i]:
                    continue
                self.state_values[(i, j)] = 0

    def choose_action(self, epsilon):
        if random.uniform(0, 1) < epsilon:
            return random.choice(self.actions)
        else:
            neighboring_states = {}
            for action in self.actions:
                row, col = self.state
                if action == 'up' and row > 1 and col not in self.env.obstacles[row - 1]:
                    neighboring_states['up'] = (row - 1, col)
                elif action == 'down' and row < self.env.height and col not in self.env.obstacles[row + 1]:
                    neighboring_states['down'] = (row + 1, col)
                elif action == 'left' and col > 1 and col - 1 not in self.env.obstacles[row]:
                    neighboring_states['left'] = (row, col - 1)
                elif action == 'right' and col < self.env.width and col + 1 not in self.env.obstacles[row]:
                    neighboring_states['right'] = (row, col + 1)

            neighboring_states_values = {action: self.state_values[state] for action, state in neighboring_states.items()}
            max_value = max(neighboring_states_values.values())
            best_actions = [action for action, value in neighboring_states_values.items() if value == max_value]

            return random.choice(best_actions)

    def train(self, episodes, alpha, gamma, epsilon):
        for _ in range(episodes):
            self.state = self.env.reset()
            terminated = False

            while not terminated:
                action = self.choose_action(epsilon)
                next_state, reward, terminated = self.env.step(action)

                self.state_values[self.state] += alpha * (reward + gamma * self.state_values[next_state] - self.state_values[self.state])
                self.state = next_state

        return self.state_values

    def print_values(self, save=False):
        values = []
        for i in range(1, self.env.height + 1):
            row = []
            for j in range(1, self.env.width + 1):
                if i in self.env.obstacles and j in self.env.obstacles[i]:
                    row.append(-10)
                else:
                    row.append(self.state_values[(i, j)])
            values.append(row)

        sns.heatmap(values, cmap='viridis', cbar=False, annot=True, fmt=".1f", annot_kws={"size": 10}, linewidths=0.1, linecolor='black')
        if save:
            plt.savefig('value_function.png')
        plt.show()

    def print_policy(self):
        actions = []
        for i in range(1, self.env.height + 1):
            maze_row = []
            for j in range(1, self.env.width + 1):
                if i in self.env.obstacles and j in self.env.obstacles[i]:
                    maze_row.append('X')
                else:
                    neighboring_states = {}
                    for action in self.actions:
                        row, col = (i, j)
                        if action == 'up' and row > 1 and col not in self.env.obstacles[row - 1]:
                            neighboring_states['up'] = (row - 1, col)
                        elif action == 'down' and row < self.env.height and col not in self.env.obstacles[row + 1]:
                            neighboring_states['down'] = (row + 1, col)
                        elif action == 'left' and col > 1 and col - 1 not in self.env.obstacles[row]:
                            neighboring_states['left'] = (row, col - 1)
                        elif action == 'right' and col < self.env.width and col + 1 not in self.env.obstacles[row]:
                            neighboring_states['right'] = (row, col + 1)

                    neighboring_states_values = {action: self.state_values[state] for action, state in neighboring_states.items()}
                    max_value = max(neighboring_states_values.values())
                    best_actions = [action for action, value in neighboring_states_values.items() if value == max_value]
                    maze_row.append(best_actions[0])
            actions.append(maze_row)

        print("Agent's policy:")
        for i in range(len(actions)):
            for j in range(len(actions[i])):
                if (i + 1, j + 1) == self.env.start:
                    print('S', end=' ')
                elif (i + 1, j + 1) == self.env.finish:
                    print('F', end=' ')
                elif actions[i][j] == 'up':
                    print('↑', end=' ')
                elif actions[i][j] == 'down':
                    print('↓', end=' ')
                elif actions[i][j] == 'left':
                    print('←', end=' ')
                elif actions[i][j] == 'right':
                    print('→', end=' ')
                else:
                    print('X', end=' ')
            print()


if __name__ == '__main__':
    random.seed(42)
    env = Maze()
    agent = Agent(env)
    state_values = agent.train(episodes=1000, alpha=0.1, gamma=0.9, epsilon=0.1)
    agent.print_values(True)
    agent.print_policy()
