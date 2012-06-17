import os
from importer import Importer
from tour import Tour
from algorithms.bfs import BestFirstSearch
from algorithms.hillclimbing import HillClimbing, RestartingHillClimb
import logging
logger = logging.getLogger(__name__)


class Solver:
    def __init__(self, options):
        self.importer = Importer()
        # self._dir = options.dir_name
        if options.dir_name is not None:
            self._files = [f for f in self.get_files(options.dir_name)]
        else:
            self._files = [options.file_name]
        self._algo_name = options.algorithm if (options.algorithm is not None) else 'bfs'
        
    def get_algo(self, name):
        name = name.lower()
        if name == 'bfs':
            return BestFirstSearch
        elif name == 'hillclimbing' or name == 'hillclimb':
            return HillClimbing
        elif name == 'hillclimb-restart':
            return RestartingHillClimb
            
    def get_files(self, path):
        for top, dirs, files in os.walk('problems'):
            for nm in files:
                file_name = os.path.join(top, nm)
                if file_name[-4:] == '.txt':
                    yield file_name
                
    def solve_file(self, file_name):
        tour = self.importer.load(file_name)
    
        algo = self.get_algo(self._algo_name)
        algo = algo(tour)
        
        logger.info("Loaded problem '%s' and algo '%s'" % (file_name, algo.NAME))
        
        path = algo.solve()
        length = tour.get_length(path)

        logger.info('Path found. Cost: %r' % length)
        print path
        
        return file_name, path, length
    
    def run(self):
        try:
            logger.info('Travelling Salesman Problem')
            
            results = []
            
            for file_name in self._files:
                results.append( self.solve_file(file_name) )
            
            logger.info('File\t\tCost')
            
            for file_name, path, length in results:
                logger.info('%s\t%s' % (file_name.split('/')[1], length))
        
        except Exception as e:
            logging.info('------------------------------')
            logging.info('Encountered an error. Halting.')
            logging.exception(e)
