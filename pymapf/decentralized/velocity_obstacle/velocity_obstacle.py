"""
Decentralized planning using velocity obstacles 
author: Erwin Lejeune (erwin.lejeune15@gmail.com)
"""

from ..obstacle import Obstacle
from .velocity_agent import VelocityAgent
import numpy as np
import matplotlib as mpl
from random import random
import os

if "DISPLAY" not in os.environ:
    mpl.use("agg")
else:
    mpl.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# import threading
from matplotlib.patches import Circle
import coloredlogs
import logging

logging.getLogger("matplotlib").setLevel(logging.WARNING)


class MultiAgentVelocityObstacle:
    def __init__(self, simulation_time=8.0, timestep=0.1, log_level="WARNING"):
        self.simulation_time = simulation_time
        self.timestep = timestep
        self.number_of_timesteps = int(simulation_time / timestep)

        # Agents
        self.agents = dict()
        self.global_state_history = dict()

        # Obstacles
        self.obstacles_objects = []

        # Flags
        self.simulation_complete = False
        self.__init_logger(log_level)
        coloredlogs.install(level=log_level)

    def register_agent(self, ident, start, goal, radius=0.5, vmax=2, vmin=0.2):
        pass

    def register_obstacle(self, velocity, theta, initial_position):
        pass

    def run_simulation(self):
        pass

    def visualize(self, saved_file, map_length, map_height):
        pass

    def __agent_step(self, key, agent, i, obstacles, other_agents_lst):
        # other_agents = self.other_agents.copy()
        # try:
        #     del other_agents[key]
        # except BaseException as e:
        #     logging.debug(e)
        #     pass
        # other_agents_lst = list(other_agents.values())
        pass

    def __agent_to_obstacle(self, velocity, pos):
        pass

    def __init_logger(self, log_level):
        pass

    def __plot(self, saved_file, map_length, map_height):
        pass
