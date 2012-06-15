# from tsp.tour import Tour
import random
import logging
import math
logger = logging.getLogger(__name__)


class SimulatedAnnealing(object):
    NAME = 'Simulated Annealing'
    
    def probability(self, current_score, proposed_scored, temperature):
        """Returns the probability that we'll select a worse path"""
        if proposed_score < current_score:
            return 1.0 # always move to a better place
        else:
            return math.exp(-abs(proposed_score-current_score)/temperature)
    
    def cooling_schedule(self, start, alpha=0.9995):
        """Produces a linearly decreasing temperature"""
        t = start
        while True:
            yield t
            t = alpha * t
            
    def solve(self, starting_path):
        pass