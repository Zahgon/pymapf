import numpy as np
from math import sqrt
from typing import List, Tuple
from sys import stdout
import random
from termcolor import colored
from .cooperative_astar.node import Node


class World:
    def __init__(self, length: int, height: int, p_walls: float, allow_diagonals=False):
        self.length = length
        self.height = height
        self.p_walls = p_walls
        self.path_added = False
        self.walls = []
        self.allow_diagonals = allow_diagonals
        self.start_positions = []
        self.goal_positions = []
        self.grid = np.zeros((height, length), int)
        self.__generate_walls()

        if not allow_diagonals:
            # up, left, down, right
            self.delta = [[-1, 0, 1], [0, -1, 1], [1, 0, 1], [0, 1, 1], [0, 0, 1]]
        else:
            # up, left, down, right
            # upleft, upright, downleft, downright
            self.delta = [
                [-1, 0, 1],
                [0, -1, 1],
                [1, 0, 1],
                [0, 1, 1],
                [0, 0, 1],
                [-1, -1, sqrt(2)],
                [-1, 1, sqrt(2)],
                [1, -1, sqrt(2)],
                [1, 1, sqrt(2)],
            ]

    def add_path(self, path: List[Tuple[int]]):
        pass

    def plot_grid(self):
        pass

    def get_random_available_position(self) -> Tuple[int]:
        pass

    def get_start_goal(self, pHeuristic) -> Tuple[Tuple[int]]:
        pass

    def change_grid(self, position: Tuple[int], value: int):
        pass

    def __generate_walls(self):
        pass
