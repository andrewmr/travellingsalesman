Travelling Salesman Problem
===========================

The classic NP-hard computer science problem. This is a collection of problem files and some various algorithms that attempt to solve an instance of the problem.

Algorithms
----------

This is an ever expanding list, but the basic ones covered so far are:

* [Best First Search](http://en.wikipedia.org/wiki/Best_first_search)
* [Hill Climbing](http://en.wikipedia.org/wiki/Hill_climbing)
* Hill Climb & Restart - A variant of the above that tries to find global maxima.
* [Simulated Annealing](http://en.wikipedia.org/wiki/Simulated_annealing)


Usage
-------

    $ python travelling.py -h

	Usage: travelling.py [options]

	Options:
	  -h, --help            show this help message and exit
	  --alpha=ALPHA         temperature decay. (used in Sim. Annealing)
	                        [default: 0.9995]
	  --temp=TEMP           starting temperature. (used in Sim. Annealing)
	                        [default: 10.0]
	  --restarts=TEMP       max iterations (used in Restarting Hill Climb)
	                        [default: 5]
	  --iterations=TEMP     max iterations (used in HC, RHC, SA)
	                        [default: 50,000]
	  --operator=OP         action to be performed when improving a solution
	                        [default: random | choices: random, reverse, switch]
	  -f FILE, --file=FILE  path to the file to be solved
	  -d DIR, --dir=DIR     path to the directory of files to be solved
	  -a NAME, --algo=NAME  algorithm to be used
	                        [choices: bfs, hillclimb, hillclimb-restart,
	                        simanneal]
	  -v, --verbose         print debug messages to stdout
	

Problem files
-------------

A small set of problem files can be found under the `problems` directory. These are all problems for an undirected graph.