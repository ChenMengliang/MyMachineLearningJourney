# -*- coding: UTF-8 -*-
# @Time             : 2019-03-01 21:30
# @Author           : Keith
# @File             : main.py
# @Software         : PyCharm
# @About            : 迷宫游戏的入口

from maze_env import Maze
from RL_brain import QLearningTable


def update():
    print('update')
    for episode in range(100):
        # initialize observation
        observation = env.reset()

        while True:
            # fresh env
            env.render()
            action = RL.choose_action(str(observation))
            observation_, reward, done = env.step(action)

            RL.learn(str(observation), action, reward, str(observation_))

            observation = observation_

            if done:
                break
    print('game over')

    env.destroy()


if __name__ == '__main__':
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)),e_greedy=0.9)
    print(RL.q_table)

    env.after(100, update)

    env.mainloop()
