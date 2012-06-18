Travelling Salesman Problem
===========================

The classic NP-hard computer science problem. This is a collection of problem files and some various algorithms that attempt to solve an instance of the problem.

Algorithms
----------

This is an ever expanding list, but the basic ones covered so far are:

* [Best First Search](http://en.wikipedia.org/wiki/Best_first_search)
* [Hill Climbing](http://en.wikipedia.org/wiki/Hill_climbing)
* [Hill Climb & Restart] - A variant of the above that tries to find global maxima.
* [Simulated Annealing](http://en.wikipedia.org/wiki/Simulated_annealing)


Usage
-------

    $ python travelling.py -h

	Usage: travelling.py [options]

	Options:
	  -h, --help            show this help message and exit
	  --alpha=ALPHA         temperature decay. (used in Sim. Annealing)
	  --temp=TEMP           starting temperature. (used in Sim. Annealing)
	  --restarts=TEMP       max iterations (used in Restarting Hill Climb)
	  --iterations=TEMP     max iterations (used in HC, RHC, SA)
	  -f FILE, --file=FILE  path to the file to be solved
	  -d DIR, --dir=DIR     path to the directory of files to be solved
	  -a NAME, --algo=NAME  algorithm to be used
	  -v, --verbose         print status messages to stdout
	

Problem files
-------------

A small set of problem files can be found under the `problems` directory.