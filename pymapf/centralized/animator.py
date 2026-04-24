#!/usr/bin/env python3
import matplotlib
from random import random
import os

if "DISPLAY" not in os.environ:
    matplotlib.use("agg")
else:
    matplotlib.use("TkAgg")
from matplotlib.patches import Circle, Rectangle, Arrow
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import math
import logging

logging.getLogger("matplotlib").setLevel(logging.WARNING)

Colors = ["skyblue", "blue", "orange"]


class Animator:
    def __init__(self, world, paths, agents, simulation_time):
        self.world = world
        self.paths = paths
        self.coop_agents = agents

        aspect = self.world.length / self.world.height
        self.fig = plt.figure(frameon=False, figsize=(4 * aspect, 4))
        self.ax = self.fig.add_subplot(111, aspect="equal")
        self.fig.subplots_adjust(
            left=0, right=1, bottom=0, top=1, wspace=None, hspace=None
        )
        self.patches = []
        self.artists = []
        self.agents = dict()
        self.agents_labels = dict()

        xmin = -0.5
        ymin = -0.5
        xmax = self.world.length - 0.5
        ymax = self.world.height - 0.5
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)

        self.__initialize_obstacles(xmin, ymin, xmax, ymax)
        self.__initialize_agents()
        self.simulation_time = simulation_time
        self.__animate()

    def __initialize_obstacles(self, xmin, ymin, xmax, ymax):
        pass

    def __initialize_agents(self):
        pass

    def __animate(self):
        pass

    def save(self, file_name):
        pass

    def show(self):
        pass

    def __initialize_animation(self):
        pass

    def __animations(self, i):
        pass
