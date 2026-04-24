import numpy as np
from scipy.optimize import minimize, Bounds
import time
import logging


class NMPCAgent:
    def __init__(
        self,
        ident,
        start,
        goal,
        number_of_timesteps,
        nmpc_timestep,
        timestep,
        qc=5.0,
        kappa=4.0,
        radius=0.5,
        vmax=2,
        vmin=0.2,
        horizon_length=4,
    ):
        # Initializations
        self.ident = ident
        self.start = np.array([start.x, start.y])
        self.goal = np.array([goal.x, goal.y])

        # Consts from NMPC Class
        self.number_of_timesteps = number_of_timesteps
        self.nmpc_timestep = nmpc_timestep
        self.timestep = timestep

        # Agent Constraints
        self.horizon_length = horizon_length
        self.vmax = vmax
        self.vmin = vmin
        self.qc = qc
        self.kappa = kappa
        self.upper_bound = [(1 / np.sqrt(2)) * self.vmax] * self.horizon_length * 2
        self.lower_bound = [-(1 / np.sqrt(2)) * self.vmax] * self.horizon_length * 2
        self.radius = radius

        # Current State
        self.current_state = self.start
        self.state_history = np.empty((4, self.number_of_timesteps))
        self.total_computation_runtime = 0

    def simulate_step(self, step, obstacles, other_agents):
        # Predict Obstacles and Agents Positions in the Future
        pass

    def __compute_velocity(self, robot_state, obstacle_predictions, xref):
        pass

    def __compute_xref(self):
        pass

    def __total_cost(self, u, robot_state, obstacle_predictions, xref):
        pass

    def __tracking_cost(self, x, xref):
        pass

    def __total_collision_cost(self, robot, obstacles):
        pass

    def __collision_cost(self, x0, x1):
        """
        Cost of collision between two robot_state
        """
        pass

    def __predict_obstacle_positions(self, obstacles, step, other_agents):
        pass

    def __update_state(self, x0, u):
        """
        Computes the states of the system after applying a sequence of control signals u on
        initial state x0
        """
        pass

    def __hash__(self):
        h = str(self.ident) + str(self.start) + str(self.goal) + str(self.radius)
        return h

    def __eq__(self, other):
        return self.ident == other.ident

    def __str__(self):
        return "=======AGENT=======\nID = %s\nSTART_POSITION = %s\nGOAL_POSITION = %s\nRADIUS = %s\nVMIN = %s\nVMAX = %s\nHORIZON_LENGTH = %s\nQC = %s\nKappa = %s\n===================" % (
            str(self.ident),
            str(self.start),
            str(self.goal),
            str(self.radius),
            str(self.vmin),
            str(self.vmax),
            str(self.horizon_length),
            str(self.qc),
            str(self.kappa),
        )
