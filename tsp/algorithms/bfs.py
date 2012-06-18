from tsp.tour import Tour
import random
import logging
logger = logging.getLogger(__name__)


class BestFirstSearch(object):
    """Best First Search is a greedy search algorithm; always making the best local
    decision, even if it's not globally optimum"""
    NAME = 'Best First Search'
    
    def __init__(self, tour, options=None):
        self.tour = tour
        self.path_cost = 0
    
    def solve(self):
        logger.info('Starting search')
        # pick a random start node
        current_node = random.randint(1, self.tour.size)
        # set up the nodes that CAN be visited, and those that have
        nodes = [i for i in range(1,self.tour.size+1)]
        nodes.remove(current_node)
        path = [current_node]
        while nodes != []:
            # include the path as a list of nodes that SHOULDNT be considered
            current_node = self.tour.get_nearest(current_node, path)
            path.append(current_node)
            nodes.remove(current_node)
        return path
        
        
