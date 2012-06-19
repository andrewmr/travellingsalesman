#!/usr/bin/env python

from optparse import OptionParser
from tsp.solver import Solver
import logging

FORMAT = '%(asctime)s %(levelname)s | %(name)s | %(message)s'

def main(options):
    """Starts the solver"""
    # we usually want INFO level, unless we're in verbose mode which wants DEBUG
    level = logging.DEBUG if options.verbose else logging.INFO
    # but if quiet is specified it trumps all
    if options.quiet:
        level = logging.ERROR
    # we set error as we want INFO/WARNING/DEBUG ignored, but we're still interested in 
    # errors and critical messages
        
    logging.basicConfig(level=level, format=FORMAT, 
                        datefmt='%Y-%m-%d %I:%M:%S %p')
                        
    solver = Solver(options)
    solver.run()

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--alpha', dest='alpha',
                      help='temperature decay. (used in Sim. Annealing)\
                            [default: 0.9995]',
                      metavar='ALPHA',
                      default=0.9995)

    parser.add_option('--temp', dest='temperature',
                      help='starting temperature. (used in Sim. Annealing)\
                            [default: 10.0]',
                      metavar='TEMP',
                      default=10.0)

    parser.add_option('--restarts', dest='restarts',
                      help='max iterations (used in Restarting Hill Climb)\
                            [default: 5]',
                      metavar='TEMP',
                      default=5)  
                                          
    parser.add_option('--iterations', dest='iterations',
                      help='max iterations (used in HC, RHC, SA) \
                            [default: 50,000]',
                      metavar='TEMP',
                      default=50000)                      

    parser.add_option('--operator', dest='operator',
                      help='action to be performed when improving a solution  \
                            [default: random | choices: random, reverse, switch]',
                      metavar='OP',
                      default='random')

    parser.add_option('-f', '--file', dest='file_name',
                      help='path to the file to be solved', metavar='FILE',
                      default='problems/file012.txt')
                      
    parser.add_option('-d', '--dir', dest='dir_name',
                      help='path to the directory of files to be solved', metavar='DIR',
                      default=None)
                      
    parser.add_option('-a', '--algo', dest='algorithm',
                      help='algorithm to be used \
                            [choices: bfs, hillclimb, hillclimb-restart, simanneal]', 
                      metavar='NAME', default='bfs')    
                                        
    parser.add_option('-v', '--verbose', dest='verbose', action="store_true",
                      help='print debug messages to stdout', default=False)  

    parser.add_option('-q', '--quiet', dest='quiet', action="store_true",
                      help='only output the result (no status messages)', default=False)  
                                          

    options, args = parser.parse_args()

    main(options)
