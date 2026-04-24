import numpy as np
import time
import logging


class VelocityAgent:
    def __init__(
        self,
        ident,
        start,
        goal,
        number_of_timesteps,
        timestep,
        radius=0.5,
        vmax=2,
        vmin=0.2,
    ):
        # Agent Initialization
        self.ident = ident
        self.start = np.array([start.x, start.y])
        self.goal = np.array([goal.x, goal.y])

        # MAPF Velocity Obstacles Consts
        self.number_of_timesteps = number_of_timesteps
        self.timestep = timestep

        # Agent Consts
        self.radius = radius
        self.vmax = vmax
        self.vmin = vmin

        # Current State
        self.current_state = self.start
        self.state_history = np.empty((4, self.number_of_timesteps))
        self.total_computation_runtime = 0

    def simulate_step(self, step, obstacles, other_agents):
        # Predict Obstacles and Agents Positions in the Future
        pass

    def __compute_desired_velocity(self, current_pos, goal_pos):
        pass

    def __compute_velocity(self, state, obstacles, step, v_desired, other_agents):
        pass

    def __check_constraints(self, v_sample, Amat, bvec):
        pass

    def __check_inside(self, v, Amat, bvec):
        pass

    def __create_constraints(self, translation, angle, side):
        # create line
        pass

    def __translate_line(self, line, translation):
        pass

    def __update_state(self, x, v):
        pass
