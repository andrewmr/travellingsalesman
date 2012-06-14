class Tour:
    def __init__(self, name, nodes):
        self.nodes = nodes
        self.size = len(nodes)
        self.name = name
        self.nearest_lookup = {}
        
    def get_distance(self, src, dst):
        """Distance between two nodes"""
        return self.nodes[src-1][dst-1]
    
    def get_nearest(self, src, banned = []):
        """Find a node's nearest neighbour"""
        try: # try find it in the lookup array
            return self.nearest_lookup[src]
        except: # its not in the lookup, better find it
            nearest = None
            nearest_dist = 0
            # build up a list of possible candidates
            nodes = [i for i in range(1,self.size+1)]
            for i in banned: # remove those in the banned list
                nodes.remove(i)
            # now we've got a candidate list, find the closest one
            for i in nodes:
                dist = self.get_distance(src, i)
                if ((dist < nearest_dist) or (nearest == None)):
                    nearest = i
                    nearest_dist = dist
            # cache it
            self.nearest_lookup[src] = nearest
            return nearest
            
    def get_length(self, path):
        """Return the cost (lenth) of a path"""
        distance = 0
        for i in xrange(0,self.size):
            distance += self.get_distance(path[i], path[((i+1) % self.size)])
        return distance
