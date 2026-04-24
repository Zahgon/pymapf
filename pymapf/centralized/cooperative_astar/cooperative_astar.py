from .agent import Agent
from .astar import AStar
import time
from ..common import TIME
from ..world import World
from .state import State
from ..animator import Animator
import coloredlogs
import logging


class CooperativeAStar:
    def __init__(self, world, heuristic=0, log_level="WARNING"):
        self.world = world
        self.allow_diagonals = world.allow_diagonals
        self.heuristic = 0
        self.agents = dict()
        self.paths = dict()
        self.searches_sim_times = []

        # Flags
        self.simulation_complete = False
        self.__init_logger(log_level)
        coloredlogs.install(level=log_level)

    def register_agent(self, ident, start, goal):
        pass

    def run_simulation(self):
        pass

    def visualize(self, save_file):
        pass

    def __init_logger(self, log_level):
        pass
