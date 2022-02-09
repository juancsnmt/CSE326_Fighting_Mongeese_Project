import paths.paths

class rooms:
    def __init__(self, *args, **kwargs):
        self.path_no = 0
        if 'above' in kwargs:
            self.paths[self.path_no] = copy.deepcopy(kwargs.get('above'))
            self.path_no += 1
            self.above_index = self.path_no
        if 'right' in kwargs:
            self.paths[self.path_no] = copy.deepcopy(kwargs.get('above'))
            self.path_no += 1
            self.right = copy.deepcopy(kwargs.get('right'))
        if 'below' in kwargs: 
            self.paths[self.path_no] = copy.deepcopy(kwargs.get('above'))
            self.path_no += 1
            self.below = copy.deepcopypaths(kwargs.get('below'))
        if 'left' in kwargs:
            self.paths[self.path_no] = copy.deepcopy(kwargs.get('above'))
            self.path_no += 1            
            self.left = copy.deepcopypaths(kwargs.get('left'))
 
