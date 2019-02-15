# -*- coding: UTF-8 -*-
# @Time             : 2019-01-14 21:46
# @Author           : Keith
# @File             : movanzhou.py
# @Software         : PyCharm
# @About            : movan python QLearning的小例子

import numpy as np
import pandas as pd
import time

np.random.seed(2)  # reproducible

N_STATES = 6  # the length of the 1 demensional world

ACTIONS = ['left', 'right']  # avalible actions
EPSILON = 0.9  # greedy police
ALPHA = 0.1  # learning rate
GAMMA = 0.9  # discount factor
MAX_EPISODES = 13  # maximun episodes
FRESH_TIME = 0.01  # fresh time for one move


# initial q table
def build_q_table(n_state, actions):
    table = pd.DataFrame(
        np.zeros((n_state, len(actions))),  # q_table initial values
        columns=actions,  # actions's name
    )
    print(table)
    return table


def choose_action(state, q_table):
    # This is how to choose an action
    state_action = q_table.iloc[state, :]
    if (np.random.uniform() > EPSILON or (state_action.all() == 0)):
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_action.idxmax()

    return action_name


def get_env_feedback(S, A):
    # This is how agent will interact with the environment
    if A == 'right':  # move right
        if S == N_STATES - 2:  # terminate
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else:  # move left
        R = 0
        if S == 0:
            S_ = S
        else:
            S_ = S - 1
    return S_, R


def update_env(S, episode, step_counter):
    # This is how environment be updated
    env_list = ['-'] * (N_STATES - 1) + ['T']  # '---------T' our environment
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode + 1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        # print('\r                                ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)


def rl():
    # main part of RL loop
    q_table = build_q_table(N_STATES, ACTIONS)
    for episode in range(MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminated = False
        update_env(S, episode, step_counter)
        while not is_terminated:

            A = choose_action(S, q_table)
            S_, R = get_env_feedback(S, A)  # take action & get next state and reward
            q_predict = q_table.loc[S, A]
            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_, :].max()  # next state is not terminal
            else:
                q_target = R  # next state is terminal
                is_terminated = True  # terminate this episode

            q_table.loc[S, A] += ALPHA * (q_target - q_predict)  # update
            S = S_  # move to next state

            update_env(S, episode, step_counter + 1)
            step_counter += 1
    return q_table


if __name__ == "__main__":
    q_table = rl()
    print('\r\nQ-table:\n')
    print(q_table)
