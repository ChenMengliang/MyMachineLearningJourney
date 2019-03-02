# -*- coding: UTF-8 -*-
# @Time             : 2019-01-24 9:43
# @Author           : Keith
# @File             : QLearnging_command_line.py
# @Software         : PyCharm
# @About            : 使用QLearning 在控制台测试小例子

import numpy as np
import pandas as pd
import time

np.random.seed(2)  # 伪随机种子

N_STATES = 6  # the length of the one dimensional world

ACTIONS = ['left', 'right']  # actions the agent can take

EPSILON = 0.9  # greedy police
ALPHA = 0.1  # learning rate
GAMMA = 0.9  # discount factor

MAX_EPISODES = 13  # max episodes the agent take to move

FRESH_TIME = 0.01  # fresh time for one move


def build_q_tables(n_states, actions):
    '''
    init a q table
    :param n_states:
    :param actions:
    :return:
    '''
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),  # n_states row and len(sctions) columns
        columns=actions  # actions' name
    )
    print(table)
    return table


def choose_action(state, q_table):
    '''
    choose the actions through by the current state and q_table
    :param state:
    :param q_table:
    :return:
    '''
    # 取第 state行
    state_action = q_table.iloc[state,:]
    if np.random.uniform() > EPSILON or state_action.all() == 0:
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_action.idxmax()
    return action_name


def get_env_feedback(S, A):
    '''
    根据当前的state和action，与环境交互，获取当前action的reward和下一步state
    :param S: current state
    :param A: current action
    :return: reward R, next state S_
    '''
    if A == 'right':
        if S == N_STATES - 2:
            R = 1
            S_ = 'terminal'
        else:
            R = 0
            S_ = S + 1
    else:
        R = 0
        if S == 0:
            S_ = 0
        else:
            S_ = S - 1
    return S_, R


def update_env(S, episode, step_counter):
    '''
    update the environment,in this example is the command line
    :param S: current state
    :param EPISODE: current episode
    :param step_counter: current step counter
    :return:
    '''
    env_list = ['-'] * (N_STATES - 1) + ['T']
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode + 1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r                                ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)


def rl():
    '''
    the main loop of RL
    :return:
    '''
    q_table = build_q_tables(N_STATES,ACTIONS)

    for episode in range(MAX_EPISODES):
        step_count = 0
        S = 0
        is_terminated = False
        update_env(S,episode,step_count)

        while not is_terminated:
            A = choose_action(S,q_table)
            S_,R = get_env_feedback(S,A)
            q_predict = q_table.loc[S,A]

            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_,:].max()
            else:
                q_target = R
                is_terminated = True
            q_table.loc[S, A] += ALPHA * (q_target - q_predict)  # update
            S = S_  # move to next state

            update_env(S, episode, step_count + 1)
            step_count += 1
        print(q_table)


    return  q_table


if __name__ == '__main__':
    q_table = rl()
    # print(q_table)

