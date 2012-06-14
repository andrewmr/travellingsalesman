from tsp.tour import Tour
import random
import logging
logger = logging.getLogger(__name__)


class RestartingHillClimb(object):
    NAME = 'Restarting Hill Climb'
    
    def __init__(self, tour, iterations=10000): # lower number of iterations
        self.tour = tour
        self.path_cost = 0
        self.iterations = iterations
        self.restarts = 5
        
    def solve(self):
        logger.info('Hill climbing (%r restarts)' % (self.restarts))

        path = []
        for i in xrange(self.restarts):
            if i == 0:
                path = HillClimbing(self.tour, self.iterations).solve()
            else:
                path = HillClimbing(self.tour, self.iterations).solve(path)
                
        return path


class HillClimbing(object):
    NAME = 'Hill Climbing'
    
    def __init__(self, tour, iterations=100000):
        self.tour = tour
        self.path_cost = 0
        self.iterations = iterations
        
    def solve(self, starting_path=None):
        logger.info('Hill climbing (%r iterations)' % self.iterations)
        
        if starting_path == None:
            start = [i for i in range(1,self.tour.size+1)]
            random.shuffle(start)
            self.path_cost = self.tour.get_length(start)
            
            logger.info('Random path with cost of %r' % self.path_cost)
        else:
            start = starting_path
            self.path_cost = self.tour.get_length(start)
            
            logger.info('Starting w/ cost of %r' % self.path_cost)
        
        for i in xrange(1,self.iterations):
            temp = start[:]
            rand_x = random.randint(1,self.tour.size)
            rand_y = random.randint(1,self.tour.size)
            
            choice = random.randint(1,2)
            if choice == 1: # for this we just swap the values in two locations
                cur_x = temp[rand_x - 1]
                temp[rand_x - 1] = temp[rand_y - 1] 
                temp[rand_y - 1] = cur_x
                
            if choice == 2: # for this we reverse an entire sub-path
                if rand_x >= rand_y:
                    temp2 = temp[rand_y:(rand_x - rand_y)+1]
                else:
                    temp2 = temp[rand_x:(rand_y - rand_x)+1]
                
                temp2.reverse() 
                
                if rand_x >= rand_y:
                    temp[rand_y:(rand_x - rand_y)+1] = temp2
                else:
                    temp[rand_x:(rand_y - rand_x)+1] = temp2

            if self.tour.get_length(temp) <= self.path_cost:
                start = temp[:]
                self.path_cost = self.tour.get_length(start)

        return start
        
        