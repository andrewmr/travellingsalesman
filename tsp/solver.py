from importer import Importer
from tour import Tour
from algorithms.bfs import BestFirstSearch
from algorithms.hillclimbing import HillClimbing, RestartingHillClimb
import logging
logger = logging.getLogger(__name__)


class Solver:
    def __init__(self, file_name, algo_name):
        self.importer = Importer()
        self._algo_name = algo_name
        self._file = file_name
        
    def get_algo(self, name):
        name = name.lower()
        if name == 'bfs':
            return BestFirstSearch
        elif name == 'hillclimbing' or name == 'hillclimb':
            return HillClimbing
        elif name == 'hillclimb-restart':
            return RestartingHillClimb
    
    def run(self):
        try:
            logger.info('Travelling Salesman Problem')
            tour = self.importer.load(self._file)
        
            algo = self.get_algo(self._algo_name)
            algo = algo(tour)
            
            logger.info("Loaded problem '%s' and algo '%s'" % (self._file, algo.NAME))
            
            path = algo.solve()
            length = tour.get_length(path)

            logger.info('Path found. Cost: %r' % length)
            print path
        except Exception as e:
            logging.info('Encountered an error. Halting.')
            logging.exception(e)
