from tsp.tour import Tour
import random
import logging
logger = logging.getLogger(__name__)


class RestartingHillClimb(object):
    """Restart repeats the hill climbing process a number of times, helps to avoid
    getting stuck on a local maxima."""
    
    NAME = 'Restarting Hill Climb'
    
    def __init__(self, tour, options): # lower number of iterations
        self.tour = tour
        self.path_cost = 0
        self.iterations = options['iterations']
        self.restarts = options['restarts']
        
    def solve(self):
        logger.info('Hill climbing (%r restarts)' % (self.restarts))

        best_score, best_path = None, []
        for i in xrange(self.restarts):
            path = HillClimbing(self.tour, options).solve()
            score = self.tour.get_length(path)
            
            if best_score == None:
                best_score, best_path = score, path
            elif score <= best_score:
                best_score, best_path = score, path
            logger.info('Best cost so far: %d' % best_score)
            
        return best_path


class HillClimbing(object):
    """Stochastic optimisation process to minimise (or maximise) the cost of a solution.
    General gist is we start with a random route, and incrementally make improvements to
    it."""
    
    NAME = 'Hill Climbing'
    
    def __init__(self, tour, options):
        self.tour = tour
        self.path_cost = 0
        self.iterations = options['iterations']
        
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
            # randomly select two cities (could evaluate all the unique pairs in future)
            rand_x = random.randint(1,self.tour.size)
            rand_y = random.randint(1,self.tour.size)
            
            # randomly select how we modify the path
            if self.operator == 'random':
                choice = random.choice(['switch','reverse'])
            elif self.operator not in ['switch','reverse']:
                choice = random.choice(['switch','reverse'])
                logger.warning("Unknown operator parameter, using default ('random')")
            
            # for this we just swap the values in two locations
            if choice == 'switch':
                cur_x = temp[rand_x - 1]
                temp[rand_x - 1] = temp[rand_y - 1] 
                temp[rand_y - 1] = cur_x
            
            # for this we reverse an entire sub-path
            if choice == 'reverse': 
                if rand_x >= rand_y:
                    temp2 = temp[rand_y:(rand_x - rand_y)+1]
                else:
                    temp2 = temp[rand_x:(rand_y - rand_x)+1]
                
                temp2.reverse() 
                
                if rand_x >= rand_y:
                    temp[rand_y:(rand_x - rand_y)+1] = temp2
                else:
                    temp[rand_x:(rand_y - rand_x)+1] = temp2
            
            # update
            if self.tour.get_length(temp) <= self.path_cost:
                start = temp[:]
                self.path_cost = self.tour.get_length(start)

        return start
        
        