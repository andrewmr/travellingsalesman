import random
import logging
import math
logger = logging.getLogger(__name__)


class SimulatedAnnealing(object):
    """This algorithm simulates the metallurgic process of annealing. 
    
    Hill Climbing can get stuck on the locally optimal solution, SA aims to find the
    globally optimum solution for a given problem. 
    
    Finding the globally optimum solution is accomplished by sometimes allowing a poorer
    candidate solution to be chosen. We do this by using a 'temperature' that decreases
    over the duration of the solving process, when the temperature is still quite high we
    can make some large jumps, but when the temperature becomes lower there's a far
    smaller probability of a worse solution being chosen."""
    NAME = 'Simulated Annealing'
    
    def __init__(self, tour, options=None):
        self._iterations = options['iterations']
        self._alpha = options['alpha']
        self._temp = options['temp']
        self._operator = options['operator']
        self._tour = tour
    
    def probability(self, current_cost, proposed_cost, temperature):
        """Returns the probability that we'll select a worse path"""
        if proposed_cost < current_cost:
            return 1.0 # always move to a better place
        else:
            return math.exp(-abs(proposed_cost-current_cost)/temperature)
    
    def cooling_schedule(self, start, alpha=0.9995):
        """Produces a linearly decreasing temperature"""
        t = self._temp
        while True:
            yield t
            t = self._alpha * t
            
    def try_improving_path(self, path):
        rand_x = random.randint(1,self._tour.size)
        rand_y = random.randint(1,self._tour.size)

        # randomly select how we modify the path
        choice = self._operator
        if self._operator == 'random':
            choice = random.choice(['switch','reverse'])
        elif self._operator not in ['switch','reverse']:
            choice = random.choice(['switch','reverse'])
            logger.warning("Unknown operator parameter, using default ('random')")

        # for this we just swap the values in two locations
        if choice == 'switch':
            cur_x = path[rand_x - 1]
            path[rand_x - 1] = path[rand_y - 1] 
            path[rand_y - 1] = cur_x

        # for this we reverse an entire sub-path
        if choice == 'reverse':
            if rand_x >= rand_y:
                path2 = path[rand_y:(rand_x - rand_y)+1]
            else:
                path2 = path[rand_x:(rand_y - rand_x)+1]

            path2.reverse() 

            if rand_x >= rand_y:
                path[rand_y:(rand_x - rand_y)+1] = path2
            else:
                path[rand_x:(rand_y - rand_x)+1] = path2

        return path
            
    def solve(self, start_temp=10):  
        logger.info("Alpha: %.4f, Temp: %.1f, Iterations: %d" % (
                        self._alpha, self._temp, self._iterations))      
        current_candidate = [i for i in range(1,self._tour.size+1)]
        random.shuffle(current_candidate)

        current_cost = self._tour.get_length(current_candidate)
        current_path = current_candidate
        
        best_path = []
        best_cost = 10e1000 # TODO: this is bad, what if we have large path lengths?
        # we might reach our iteration limit when we exit out of the search, so we need 
        # to keep track of our absolute best path, in addition to our current candidate, as
        # the current one might be a 'worse' path. we don't want to return a worse one 
        # if we have knowledge of a better one.
        
        temp_gen = self.cooling_schedule(start_temp)
        
        for i in xrange(self._iterations):
            temperature = temp_gen.next()
            
            new_path = self.try_improving_path(current_path)
            new_cost = self._tour.get_length(new_path)

            p = self.probability(current_cost, new_cost, temperature)
                
            if random.random() < p:
                current_path = new_path[:]
                current_cost = new_cost
                
            if new_cost <= best_cost:
                best_path = new_path[:]
                best_cost = new_cost

        return best_path