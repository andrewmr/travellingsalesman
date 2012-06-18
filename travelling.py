#!/usr/bin/env python

from optparse import OptionParser
from tsp.solver import Solver
import logging

FORMAT = '%(asctime)s %(levelname)s | %(name)s | %(message)s'

def main(options):
    """Starts the solver"""
    level = logging.DEBUG if options.verbose else logging.INFO
    logging.basicConfig(level=level, format=FORMAT, 
                        datefmt='%Y-%m-%d %I:%M:%S %p')
                        
    solver = Solver(options)
    solver.run()

if __name__ == '__main__':
    default_file = "problems/file012.txt"
    default_dir = None
    default_algo = 'bfs'
    
    parser = OptionParser()
    parser.add_option('-f', '--file', dest='file_name',
                      help='path to the file to be solved', metavar='FILE',
                      default=default_file)
    parser.add_option('-d', '--dir', dest='dir_name',
                      help='path to the directory of files to be solved', metavar='DIR',
                      default=default_dir)
    parser.add_option('-a', '--algo', dest='algorithm',
                      help='algorithm to be used', metavar='NAME',
                      default=default_algo)                      
    parser.add_option('-v', '--verbose', dest='verbose', action="store_true",
                      help='print status messages to stdout', default=False)

    options, args = parser.parse_args()
    
    if 'help' in args:
        print 'Possible algorithms:'
        print '\tbfs'
        print '\thillclimb'
        print '\thillclimb-restart'
        print '\tsimulated-annealing'
    else:
        main(options)
