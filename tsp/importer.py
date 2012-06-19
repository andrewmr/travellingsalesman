import re
from tour import Tour
import logging
from algorithms import utils

logger = logging.getLogger(__name__)

class Importer:
	def __init__(self):
		self.regex = re.compile("[^a-zA-Z0-9,=]", re.UNICODE)
		self.tour_name = ""
		self.tour_size = 0
		self.tour_nodes = []
		self.success = False

	def load(self,f):
		"""Loads in the import data and returns a Tour instance"""
		open_file =	open(f, "r")
		self.contents = open_file.read()
		# clean up and extrace the base data
		self.clean_up()
		# put together the src-dst array map
		self.parse_nodes()
		return Tour(self.tour_name, self.tour_nodes)
		
	def clean_up(self):
		"""Cleans up the imported data and pulls out some metadata"""
		self.contents = self.regex.sub('', self.contents)
		self.contents = self.contents.split(",")
		# pull out the name
		self.tour_name = self.contents.pop(0)
		self.tour_name = self.tour_name.replace("NAME=", "")
		# pull out the tour size
		self.tour_size = self.contents.pop(0)
		self.tour_size = int(self.tour_size.replace("SIZE=", ""))
		# nodes time
		self.tour_nodes = self.contents
		self.contents = None
		
	def parse_nodes(self):
		if self.tour_size == 0: return
		
		expected = utils.n_choose_k(self.tour_size,2) 
		path_count = len(self.tour_nodes)
		
		if expected < len(self.tour_nodes):
		    logger.debug('Found %d paths, expecting %d - using expected' % (
		        len(self.tour_nodes), expected
		    ))
		    path_count = expected
		
		# let's go...
		x = 1
		y = 2
		j = 0
		
		# initialise a 0-array of the right size (the diagonal will be 0s)
		nodes = [[0 for col in range(self.tour_size)] for row in range(self.tour_size)]
		while j < path_count:
			nodes[x-1][y-1] = int(self.tour_nodes[j])
			nodes[y-1][x-1] = int(self.tour_nodes[j])
			
			# work out where in the distaince matrix we are
			if (y == self.tour_size):
				x += 1
				y = (x+1) % self.tour_size
			else:
				y += 1
			
			j += 1
			
		self.tour_nodes = nodes
