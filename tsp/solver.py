import os
from importer import Importer
from tour import Tour
from algorithms.bfs import BestFirstSearch
from algorithms.hillclimbing import HillClimbing, RestartingHillClimb
from algorithms.simanneal import SimulatedAnnealing
import logging
logger = logging.getLogger(__name__)


class Solver:
    def __init__(self, options):
        self.importer = Importer()

        # try read all the files in the dir
        if options.dir_name is not None:
            self._files = [f for f in self.get_files(options.dir_name)]
        else:
            self._files = [options.file_name] # only one file
        self._algo_name = options.algorithm if (options.algorithm is not None) else 'bfs'
        self.options = options
        
    def get_algo(self, name):
        """Return an instance of the algo specified"""
        name = name.lower()
        if name == 'bfs':
            return BestFirstSearch
        elif name in ['hillclimbing','hillclimb']:
            return HillClimbing
        elif name == 'hillclimb-restart':
            return RestartingHillClimb
        elif name in ['simanneal', 'simulated-annealing','annealing']:
            return SimulatedAnnealing
            
    def get_options(self):
        """Pull out the relevant (valid) options"""
        return {
            'alpha':float(self.options.alpha),
            'iterations':int(self.options.iterations),
            'temp':float(self.options.temperature),
            'restarts':int(self.options.restarts),
            'operator':str(self.options.operator),
        }
            
    def get_files(self, path):
        """Find all solvable files in a dir"""
        for top, dirs, files in os.walk('problems'):
            for nm in files:
                file_name = os.path.join(top, nm)
                if file_name[-4:] == '.txt':
                    yield file_name
                
    def solve_file(self, file_name):
        """Attempt to solve the file, with the given algo"""
        tour = self.importer.load(file_name)
        
        try:
            algo = self.get_algo(self._algo_name)
            algo = algo(tour, options=self.get_options())
        except Exception as e:
            logger.exception('No such algorithm %s' % self._algo_name)
            raise e
        
        logger.info("Loaded problem '%s' and algo '%s'" % (file_name, algo.NAME))
        
        path = algo.solve()
        length = tour.get_length(path)

        logger.info('Path found for %s. Cost: %r' % (tour.name,length))
        # print path
        
        return tour.name, path, length
    
    def run(self):
        """Run the solver over all provided files"""
        try:
            logger.info('Travelling Salesman Problem')
            
            results = []
            
            for file_name in self._files:
                results.append( self.solve_file(file_name) )
            
            for name, path, length in results:
                print 'FILE=%s,' % name
                print 'SIZE=%d,' % length
                print 'PATH=%s' % ','.join(map(str,path))
                # logger.info('%s\t%s' % (file_name.split('/')[1], length))
    
        except Exception as e:
            logging.info('------------------------------')
            logging.info('Encountered an error. Halting.')
            logging.exception(e)
