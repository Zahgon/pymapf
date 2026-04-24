"""
An agent is defined by an Id, a start position and a goal position. 
To do: add radius
"""

import logging


class Agent:
    def __init__(
        self, ident, init_pos, goal_pos, allow_diagonals=False, nodes_dict=None
    ):
        self.ident = ident
        self.init_pos = init_pos
        self.goal_pos = goal_pos
        self.nodes_dict = nodes_dict
        self.plan = []
        self.conflicts_found = 0
        self.opened_nodes = 0
        self.allow_diagonals = allow_diagonals

    def in_conflict(self, current_state, future_state, other_agents_paths):
        pass

    def __str__(self):
        return "Id: %d | Init: [%d;%d] | Goal: [%d;%d]" % (
            self.ident,
            self.init_pos[0],
            self.init_pos[1],
            self.goal_pos[0],
            self.goal_pos[1],
        )
