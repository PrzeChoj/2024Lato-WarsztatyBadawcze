import random
import numpy as np
import matplotlib.pyplot as plt


bandits = [(0,1) for i in range(10)]
bandits[0] = (1,1)
epsg_num_selections = np.zeros(10)
epsg_bandit_mean = np.zeros(10)
epsg_mean_reward = [0]
ucb_num_selections = np.ones(10)
ucb_bandit_mean = np.zeros(10)
ucb_mean_reward = [0]


def epsg_select_bandit(epsilon, epsg_bandit_mean):
    if np.random.random() < epsilon:
        return np.random.randint(10)
    else:
        return np.argmax(epsg_bandit_mean)
    
    
def ucb_select_bandit(ucb_bandit_mean,ucb_num_selections,c,step): 
    rewards = ucb_bandit_mean + c * np.sqrt(np.log(step)/ucb_num_selections)
    return np.argmax(rewards)
    
    

def play():
    for i in range(1000):
        epsg_choice = epsg_select_bandit(0.1,epsg_bandit_mean)
        epsg_reward = np.random.normal(bandits[epsg_choice][0],bandits[epsg_choice][1])
        epsg_num_selections[epsg_choice] += 1   
        epsg_bandit_mean[epsg_choice] = epsg_bandit_mean[epsg_choice] + (epsg_reward - epsg_bandit_mean[epsg_choice]) / (epsg_num_selections[epsg_choice])
        epsg_mean_reward.append(epsg_mean_reward[i] + (epsg_reward - epsg_mean_reward[i]) / (i+1)) 

    for i in range(10):
        ucb_reward = np.random.normal(bandits[i][0],bandits[i][1])
        ucb_bandit_mean[i] = ucb_reward
        ucb_mean_reward.append(ucb_mean_reward[i] + (ucb_reward - ucb_mean_reward[i]) / (i+1))

    for i in range(10,1000):
        ucb_choice = ucb_select_bandit(ucb_bandit_mean,ucb_num_selections,2,i+1)
        ucb_reward = np.random.normal(bandits[ucb_choice][0],bandits[ucb_choice][1])
        ucb_num_selections[ucb_choice] += 1
        ucb_bandit_mean[ucb_choice] = ucb_bandit_mean[ucb_choice] + (ucb_reward - ucb_bandit_mean[ucb_choice]) / ucb_num_selections[ucb_choice]
        ucb_mean_reward.append(ucb_mean_reward[i] + (ucb_reward - ucb_mean_reward[i]) / (i+1))



def main():
    play()
    plt.plot(np.arange(1,1001),epsg_mean_reward[1:], label = 'epsg', color = 'grey')
    plt.plot(np.arange(1,1001),ucb_mean_reward[1:], label = 'ucb', color = 'blue')
    plt.xlabel('Steps')
    plt.ylabel('Average reward')
    plt.title('UCB vs EPSG')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()