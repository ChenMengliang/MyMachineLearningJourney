# -*- coding: UTF-8 -*-
# @Time             : 2019-03-01 21:29
# @Author           : Keith
# @File             : RL_brain.py
# @Software         : PyCharm
# @About            : 封装Q Table的类

import numpy as np
import pandas as pd


class QLearningTable:
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        """
        :param actions: a list
        :param learning_rate:
        :param reward_decay:
        :param e_greedy:
        """
        self.actions = actions
        self.learning_rate = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
        # self.q_table = pd.DataFrame(columns=self.actions, data=np.random.rand(3, 4))

    def choose_action(self, observation):
        self.check_state_exist(observation)
        #   action selection
        if np.random.uniform() < self.epsilon:
            # choose the best action
            state_action = self.q_table.loc[observation, :]
            # some actions may have the same value, randomly choose on in these actions
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
        else:
            action = np.random.choice(self.actions)
        return action

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state
                )
            )

    def learn(self,current_state,action,reward,next_state):
        self.check_state_exist(next_state)
        q_predict = self.q_table.loc[current_state,action]

        if next_state != 'terminal':
            q_target = reward + self.gamma*self.q_table.loc[next_state,:].max()
        else:
            q_target = reward
        self.q_table.loc[current_state,action] += self.learning_rate*(q_target - q_predict)


if __name__ == '__main__':
    q_table = QLearningTable(['up', 'down', 'left', 'right'])
    print(q_table.q_table.columns)
    q_table.check_state_exist(3)
    print()
    print(q_table.q_table.columns)
